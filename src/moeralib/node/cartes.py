from time import time
from typing import List

from .caller import CarteSource
from .node import MoeraNode
from .types import CarteInfo, CarteAttributes, Scope


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
