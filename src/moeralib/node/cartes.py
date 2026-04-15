import os
from base64 import urlsafe_b64encode
from time import time
from typing import Sequence

from cryptography.hazmat.primitives.asymmetric import ec

from .caller import CarteSource
from .fingerprints import create_carte_fingerprint3
from .node import MoeraNode
from .types import CarteInfo, CarteAttributes, Scope, Timestamp, SCOPE_VALUES
from ..crypto import sign_fingerprint


class MoeraCartesError(Exception):
    """Error obtaining valid cartes."""
    pass


class MoeraCarteSource(CarteSource):
    """Class that gets cartes from the given node, caches them and supplies them for authentication."""
    _node: MoeraNode
    _client_scope: list[Scope]
    _admin_scope: list[Scope]
    _target_node_name: str | None
    _cartes: list[CarteInfo]

    def __init__(self, node: MoeraNode, client_scope: list[Scope] | None = None, admin_scope: list[Scope] | None = None,
                 target_node_name: str | None = None):
        """
        :param node: node to get cartes from
        :param client_scope: permissions to be granted to the cartes; if not set, all permissions of the cartes' owner
               are granted
        :param admin_scope: additional administrative permissions (of those granted to the cartes' owner by the target
               node) to be granted to the cartes
        :param target_node_name: if set, the cartes are valid for authentication on the specified node only
        """
        self._node = node
        if client_scope is None:
            default_scope: Scope = "all"
            self._client_scope = [default_scope]
        else:
            self._client_scope = client_scope
        if admin_scope is None:
            self._admin_scope = []
        else:
            self._admin_scope = admin_scope
        self._target_node_name = target_node_name
        self._cartes = []

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
                    break
                self.renew()
                continue
            for c in self._cartes:
                if c.beginning <= now:
                    return c.carte
            raise MoeraCartesError("Could not obtain a carte valid for now")
        raise MoeraCartesError("Could not obtain a valid carte from the node")


def to_scope_mask(scope: Sequence[Scope]) -> int:
    mask = 0
    for sc in scope:
        mask |= SCOPE_VALUES[sc]
    return mask


def generate_carte(owner_name: str, signing_key: ec.EllipticCurvePrivateKey, beginning: Timestamp, ttl: int = 600,
                   address: list[str] | str | None = None, node_name: str | None = None,
                   client_scope: Sequence[Scope] | int = SCOPE_VALUES["all"],
                   admin_scope: Sequence[Scope] | int = 0) -> str:
    """
    Generate a carte with the given parameters and sign it with the provided private signing key.

    :param owner_name: name of the node authenticating with the carte
    :param signing_key: the private signing key to sign the carte
    :param beginning: timestamp of the beginning of the carte's life
    :param ttl: length of the carte's life, in seconds
    :param address: if set, the carte is valid for authentication from the given IP address(-es) only
    :param node_name: if set, the carte is valid for authentication on the specified node only
    :param client_scope: list of permissions granted to the carte
    :param admin_scope: list of additional administrative permissions (of those granted to the carte's owner by
           the target node) granted to the carte
    :return: the carte
    """
    client_scope_mask = to_scope_mask(client_scope) if not isinstance(client_scope, int) else client_scope
    admin_scope_mask = to_scope_mask(admin_scope) if not isinstance(admin_scope, int) else admin_scope
    if address is None:
        addresses: list[str] | None = None
    elif isinstance(address, list):
        addresses = address
    else:
        addresses = [address]
    fingerprint = create_carte_fingerprint3(owner_name, addresses, beginning, beginning + ttl, node_name,
                                            client_scope_mask, admin_scope_mask, os.urandom(8))
    signature = sign_fingerprint(fingerprint, signing_key)
    return urlsafe_b64encode(fingerprint + signature).decode('ascii')
