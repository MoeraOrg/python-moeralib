from base64 import b64encode
from typing import Any, cast, Sequence, Tuple, Mapping

import requests
from jsonschema.exceptions import ValidationError

from . import schemas, types
from ..pruning_validator import validate
from ..structure import structure_or_none, structure_list

MAIN_SERVER = 'https://naming.moera.org/moera-naming'
"""Main Moera naming server."""
DEV_SERVER = 'https://naming-dev.moera.org/moera-naming'
"""Moera developers' naming server."""


class MoeraNamingError(Exception):
    """Generic naming server error."""

    def __init__(self, method: str, message: str):
        """
        :param method: API method name
        :param message: error message
        """
        super().__init__(method + ': Naming server error: ' + message)


class MoeraNamingApiError(MoeraNamingError):
    """Naming server returned an error response."""
    error_code: int
    """Error code."""

    def __init__(self, name: str, response: Mapping[str, Any]):
        """
        :param method: API method name
        :param response: server response
        """
        super().__init__(name, response.get('message') if response.get('message') is not None else '')
        self.error_code = response.get('code', -1)


class MoeraNamingConnectionError(Exception):
    """Naming server connection error."""

    def __init__(self, message: str):
        """
        :param message: error message
        """
        super().__init__('Naming server connection error: ' + message)


class MoeraNaming:
    """Naming API interface."""
    _server: str
    _call_id: int

    def __init__(self, server: str = MAIN_SERVER):
        """
        :param server: the naming server URL
        """
        self._server = server
        self._call_id = 0

    def call(self, method: str, params: Sequence[Any], schema: Any = None):
        """
        Generic naming API call.

        :param method: name of the method to be called
        :param params: parameters of the call
        :param schema: JSON schema to validate the return value
        :return: the return value, if any
        """
        try:
            r = requests.post(
                self._server,
                json={
                    'method': method,
                    'params': params,
                    'jsonrpc': '2.0',
                    'id': self._call_id,
                }
            )
            self._call_id += 1

            response = r.json()
            if r.status_code not in [200, 201] or 'error' in response:
                if 'error' in response:
                    raise MoeraNamingApiError(method, response['error'])
                else:
                    raise MoeraNamingError(method, 'Invalid server response: ' + repr(response))
            if 'result' not in response:
                raise MoeraNamingError(method, 'Invalid server response: ' + repr(response))
            result = response['result']
            if schema is not None and result is not None:
                validate(result, schema=schema)

            return result
        except requests.exceptions.InvalidJSONError as e:
            raise MoeraNamingError(method, 'Invalid server response') from e
        except requests.exceptions.RequestException as e:
            raise MoeraNamingConnectionError(str(e)) from e
        except ValidationError as e:
            raise MoeraNamingError(method, 'Invalid server response: ' + repr(e)) from e

    def put(self, name: str, generation: int, updating_key: bytes | None = None, node_uri: str | None = None,
            signing_key: bytes | None = None, valid_from: types.Timestamp | None = None,
            previous_digest: bytes | None = None, signature: bytes | None = None) -> str:
        """
        Register or update the name. See Architecture Overview for the `detailed description
        <https://moera.org/overview/naming.html>`_ of the algorithm.

        :param name: the name to be registered/updated
        :param generation: the name generation to be registered/updated
        :param updating_key: the public key for verifying signatures of further updates of the name. May be ``None``
            if the current generation of the name is updated – the current key is preserved in this case.
        :param node_uri: URI of the REST API endpoint of the node to which the name is assigned. May be ``None`` -
            the current URI is preserved in this case.
        :param signing_key: the public key of the name owner. May be ``None`` – the current key is preserved in this
            case.
        :param valid_from: the moment in time the owner's key is valid from. May be ``None`` if ``signing_key`` is also
            ``None``.
        :param previous_digest: the unique identifier as reported by a naming server of the current state of the name.
            Used to detect the situations when the name was changed by someone else between sending the request and
            processing it. May be ``None`` if the name was never registered before.
        :param signature: the signature, if required, ``None`` otherwise
        :return: identifier of the operation that was created
        """
        return cast(str, self.call('put', [name, generation, _encode_bytes(updating_key), node_uri,
                                           _encode_bytes(signing_key), valid_from, _encode_bytes(previous_digest),
                                           _encode_bytes(signature)]))

    def get_status(self, operation_id: str) -> types.OperationStatusInfo | None:
        """
        Get the current status of the operation.

        :param operation_id:
        :return: the operation status or ``None``, if the operation ID is unknown
        """
        return structure_or_none(self.call('getStatus', [operation_id], schemas.OPERATION_STATUS_INFO_SCHEMA),
                                 types.OperationStatusInfo)

    def get_current(self, name: str, generation: int) -> types.RegisteredNameInfo | None:
        """
        Get current information about the given generation of the name.

        :param name:
        :param generation:
        :return: the information or ``None``, if the name/generation is not found
        """
        return structure_or_none(self.call('getCurrent', [name, generation], schemas.REGISTERED_NAME_INFO_SCHEMA),
                                 types.RegisteredNameInfo)

    def get_past(self, name: str, generation: int, at: types.Timestamp) -> types.RegisteredNameInfo | None:
        """
        Get past information about the given generation of the name.

        :param name:
        :param generation:
        :param at: the moment in time the information is related to
        :return: the information or ``None``, if the name/generation did not exist at the given moment
        """
        return structure_or_none(self.call('getPast', [name, generation, at], schemas.REGISTERED_NAME_INFO_SCHEMA),
                                 types.RegisteredNameInfo)

    def is_free(self, name: str, generation: int) -> bool:
        """
        Check if the given name is available for registration.

        :param name:
        :param generation:
        :return: ``True``, if the name is free, ``False`` otherwise
        """
        return cast(bool, self.call('isFree', [name, generation]))

    def get_similar(self, name: str) -> types.RegisteredNameInfo | None:
        """
        Find a name that is close to the given name.

        :param name:
        :return: information about the name or ``None``, if no name found that is close enough
        """
        return structure_or_none(self.call('getSimilar', [name], schemas.REGISTERED_NAME_INFO_SCHEMA),
                                 types.RegisteredNameInfo)

    def get_all_keys(self, name: str, generation: int) -> list[types.SigningKeyInfo]:
        """
        Get the whole history of signing keys for the given name.

        :param name:
        :param generation:
        :return: the keys
        """
        return structure_list(self.call('getAllKeys', [name, generation], schemas.SIGNING_KEY_INFO_ARRAY_SCHEMA),
                              types.SigningKeyInfo)

    def get_all(self, at: types.Timestamp, page: int, size: int) -> list[types.RegisteredNameInfo]:
        """
        Get the list of all registered names at the given moment. The list is returned in pages, one per call.

        :param at: the moment in time the information is related to
        :param page: number of the page to be returned (starting from 0)
        :param size: size of the page
        :return:
        """
        return structure_list(self.call('getAll', [at, page, size], schemas.REGISTERED_NAME_INFO_ARRAY_SCHEMA),
                              types.RegisteredNameInfo)

    def get_all_newer(self, at: types.Timestamp, page: int, size: int) -> list[types.RegisteredNameInfo]:
        """
        Get the list of all names registered after the given moment. The list is returned in pages, one per call.

        :param at: the moment in time the information is related to
        :param page: number of the page to be returned (starting from 0)
        :param size: size of the page
        :return:
        """
        return structure_list(self.call('getAllNewer', [at, page, size], schemas.REGISTERED_NAME_INFO_ARRAY_SCHEMA),
                              types.RegisteredNameInfo)


def _encode_bytes(b: bytes | None) -> str | None:
    return b64encode(b).decode() if b is not None else None


def node_name_parse(node_name: str) -> Tuple[str, int]:
    """
    Parse a node name and return its name and generation parts.

    If the node name does not include a generation, generation 0 is returned. If name syntax is invalid, ``ValueError``
    is raised.

    :param node_name: the node name to be parsed
    :return: tuple (name, generation)
    """
    name = node_name
    generation = 0

    pos = node_name.rfind('_')
    if pos >= 0:
        (name, gen) = (node_name[0:pos], node_name[pos + 1:])
        try:
            generation = int(gen)
        except ValueError:
            raise ValueError(f'invalid generation: "{gen}"')

    return name, generation


def shorten(node_name: str | None) -> str | None:
    """
    Converts the node name to the compact form, omitting generation 0.

    :param node_name: the node name in compact or full form
    :return: the node name in the compact form
    """
    if node_name is None:
        return None
    (name, gen) = node_name_parse(node_name)
    if gen == 0:
        return name
    else:
        return node_name


def expand(node_name: str | None) -> str | None:
    """
    Converts the node name to the full form, containing generation.

    :param node_name: the node name in compact or full form
    :return: the node name in the full form
    """
    if node_name is None:
        return None
    (name, gen) = node_name_parse(node_name)
    return f'{name}_{gen}'


def resolve(name: str, naming_server: str = MAIN_SERVER) -> str | None:
    """
    Shortcut function to resolve a node name and get the node URI.

    :param name: the node name
    :param naming_server: a naming server to be used
    :return: the node URI, or ``None`` if the name does not exist
    """
    (name, gen) = node_name_parse(name)
    naming = MoeraNaming(naming_server)
    info = naming.get_current(name, gen)
    return info.node_uri if info is not None else None
