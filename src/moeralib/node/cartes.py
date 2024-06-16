from time import time
from typing import List

from .caller import CarteSource
from .node import MoeraNode
from .types import CarteInfo


class MoeraCartesError(Exception):
    """Error obtaining valid cartes."""
    pass


def is_admin_carte(carte: CarteInfo) -> bool:
    return carte.permissions is None or "other" in carte.permissions


class MoeraCarteSource(CarteSource):
    """Class that gets cartes from the given node, caches them and supplies them for authentication."""
    _node: MoeraNode
    _cartes: List[CarteInfo] = []

    def __init__(self, node: MoeraNode):
        """
        :param node: node to get cartes from
        """
        self._node = node

    def renew(self) -> None:
        """
        Force renewing the cached list of cartes.
        """
        self._cartes = self._node.get_cartes().cartes

    def get_carte(self) -> str:
        """
        Get a valid carte. Use one of the cached ones, if possible.

        :return: the carte
        """
        for renewed in [False, True]:
            now = int(time())
            self._cartes = [c for c in self._cartes if c.deadline > now and is_admin_carte(c)]
            if len(self._cartes) == 0:
                if renewed:
                    raise MoeraCartesError("Could not obtain a valid carte from the node")
                self.renew()
                continue
            for c in self._cartes:
                if c.beginning <= now:
                    return c.carte
            raise MoeraCartesError("Could not obtain a carte valid for now")
