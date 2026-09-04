from __future__ import annotations

from collections.abc import Mapping
from enum import Enum, auto
from types import MappingProxyType
from urllib.parse import quote, unquote


class NodeSourceUri:
    """A node source URI with an ordered set of percent-encoded parameters."""

    class Service(Enum):
        """A service identified from a node source URI."""

        TELEGRAM = auto()
        """Telegram."""

    VIA_EMAIL = 'via_email'
    """The value of this parameter is the contact e-mail address of the importing service that delivers content for
    this node."""

    _uri: str
    _parameters: dict[str, str]

    def __init__(self, uri: str = '') -> None:
        """
        Create a node source URI.

        :param uri: URI part without a semicolon
        :raises TypeError: if ``uri`` is not a string
        :raises ValueError: if ``uri`` contains a semicolon
        """
        self._uri = ''
        self._parameters = {}
        self.uri = uri

    @classmethod
    def parse(cls, source_uri: str) -> NodeSourceUri:
        """
        Parse a serialized node source URI.

        :param source_uri: URI and parameter string
        :return: parsed node source URI
        """
        _require_string(source_uri, 'source_uri')
        parts = source_uri.split(';')
        result = cls(parts[0])
        for part in parts[1:]:
            encoded_name, separator, encoded_value = part.partition('=')
            name = unquote(encoded_name, errors='replace')
            value = unquote(encoded_value if separator else '', errors='replace')
            result.set_parameter(name, value)
        return result

    @property
    def uri(self) -> str:
        """URI part."""
        return self._uri

    @uri.setter
    def uri(self, uri: str) -> None:
        _require_string(uri, 'uri')
        if ';' in uri:
            raise ValueError('Node source URI must not contain a semicolon')
        self._uri = uri

    @property
    def parameters(self) -> Mapping[str, str]:
        """Read-only view of the parameters in insertion order."""
        return MappingProxyType(self._parameters)

    def set_parameters(self, parameters: Mapping[str, str]) -> None:
        """
        Replace all parameters with a copy of ``parameters``. Empty names are ignored.

        :param parameters: new parameters
        """
        if not isinstance(parameters, Mapping):
            raise TypeError('parameters must be a mapping')
        copied: dict[str, str] = {}
        for name, value in parameters.items():
            _require_string(name, 'parameter name')
            _require_string(value, 'parameter value')
            if name:
                copied[name] = value
        self._parameters = copied

    def has_parameter(self, name: str) -> bool:
        """Return whether the named parameter exists."""
        _require_string(name, 'name')
        return name in self._parameters

    def get_parameter(self, name: str) -> str | None:
        """Return a parameter value, or ``None`` if it does not exist."""
        _require_string(name, 'name')
        return self._parameters.get(name)

    def set_parameter(self, name: str, value: str) -> None:
        """Set a parameter. An empty name is ignored."""
        _require_string(name, 'name')
        _require_string(value, 'value')
        if name:
            self._parameters[name] = value

    def get_service(self) -> Service | None:
        """Return the service identified by the URI, or ``None`` if it is not supported."""
        if self._uri.startswith('https://t.me/'):
            return self.Service.TELEGRAM
        return None

    def __str__(self) -> str:
        result = self._uri
        for name, value in self._parameters.items():
            result += f';{quote(name, safe="-._~")}={quote(value, safe="-._~")}'
        return result


def _require_string(value: object, name: str) -> None:
    if not isinstance(value, str):
        raise TypeError(f'{name} must be a string')
