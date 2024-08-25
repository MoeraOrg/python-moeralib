import os
from base64 import urlsafe_b64encode
from time import time
from typing import List

from cryptography.hazmat.primitives.asymmetric import ec

from .caller import CarteSource
from .fingerprints import create_carte_fingerprint2
from .node import MoeraNode
from .types import CarteInfo, CarteAttributes, Scope, Timestamp, SCOPE_VALUES
from ..crypto import sign_fingerprint


class MoeraCartesError(Exception):
    """Error obtaining valid cartes."""
    pass


class MoeraCarteSource(CarteSource):
    """Class that gets cartes from the given node, caches them and supplies them for authentication."""
    _node: MoeraNode
    _client_scope: List[Scope]
    _admin_scope: List[Scope]
    _target_node_name: str | None
    _cartes: List[CarteInfo] = []

    def __init__(self, node: MoeraNode, client_scope: List[Scope] | None = None, admin_scope: List[Scope] | None = None,
                 target_node_name: str | None = None):
        """
        :param node: node to get cartes from
        """
        self._node = node
        self._client_scope = client_scope if client_scope is not None else ["all"]
        self._admin_scope = admin_scope if admin_scope is not None else []
        self._target_node_name = target_node_name

    def renew(self) -> None:
        """
        Force renewing the cached list of cartes.
        """
        attributes = CarteAttributes(client_scope=self._client_scope, admin_scope=self._admin_scope,
                                     node_name=self._target_node_name)
        self._cartes = self._node.create_cartes(attributes).cartes

    def get_carte(self) -> str:
        """
        Get a valid carte. Use one of the cached ones, if possible.

        :return: the carte
        """
        for renewed in [False, True]:
            now = int(time())
            self._cartes = [c for c in self._cartes if c.deadline > now]
            if len(self._cartes) == 0:
                if renewed:
                    raise MoeraCartesError("Could not obtain a valid carte from the node")
                self.renew()
                continue
            for c in self._cartes:
                if c.beginning <= now:
                    return c.carte
            raise MoeraCartesError("Could not obtain a carte valid for now")


def to_scope_mask(scope: List[Scope]) -> int:
    mask = 0
    for sc in scope:
        mask |= SCOPE_VALUES[sc]
    return mask


def generate_carte(owner_name: str | None, signing_key: ec.EllipticCurvePrivateKey, beginning: Timestamp | None,
                   address: str | None = None, ttl: int = 600, node_name: str | None = None,
                   client_scope: List[Scope] | int = SCOPE_VALUES["all"], admin_scope: List[Scope] | int = 0) -> str:
    if isinstance(client_scope, list):
        client_scope = to_scope_mask(client_scope)
    if isinstance(admin_scope, list):
        client_scope = to_scope_mask(admin_scope)
    fingerprint = create_carte_fingerprint2(owner_name, address, beginning, beginning + ttl, node_name, client_scope,
                                            admin_scope, os.urandom(8))
    signature = sign_fingerprint(fingerprint, signing_key)
    return urlsafe_b64encode(fingerprint + signature).decode('ascii')
