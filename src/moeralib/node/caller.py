import json
from copy import deepcopy
from enum import Enum
from typing import Any, IO, Mapping, Sequence

import requests
from jsonschema.exceptions import ValidationError

from . import schemas
from .types import Result, BodyFormat, SourceFormat, Body
from ..pruning_validator import validate
from ..structure import Structure


class MoeraNodeError(Exception):
    """Generic node error."""

    def __init__(self, name: str, message: str):
        """
        :param name: request name
        :param message: error message
        """
        super().__init__(name + ': Node error: ' + message)


class MoeraNodeApiError(MoeraNodeError):
    """Node returned an error response."""
    error_code: str
    """Error code."""

    def __init__(self, name: str, result: Result):
        """
        :param name: request name
        :param result: node response
        """
        super().__init__(name, result.message if result.message is not None else '')
        self.error_code = result.error_code


class MoeraNodeConnectionError(Exception):
    """Error while connecting the node."""

    def __init__(self, message: str):
        """
        :param message: error message
        """
        super().__init__('Node connection error: ' + message)


def encode_body(decoded: Body, format: BodyFormat | SourceFormat | None) -> str:
    if format is not None and format.lower() == "application":
        return decoded.text
    return json.dumps(decoded.json(), indent=None)


def encode_bodies(data: Structure | Sequence[Structure]) -> Structure | list[Structure]:
    if isinstance(data, Sequence):
        return [encode_bodies(item) for item in data]
    encoded = deepcopy(data)
    if getattr(data, 'body', None) is not None:
        encoded.body = encode_body(getattr(data, 'body'), getattr(data, 'body_format', None))
    if getattr(data, 'body_preview', None) is not None:
        encoded.body_preview = encode_body(getattr(data, 'body_preview'), getattr(data, 'body_format', None))
    if getattr(data, 'body_src', None) is not None:
        encoded.body_src = encode_body(getattr(data, 'body_src'), getattr(data, 'body_src_format', None))
    return encoded


def decode_body(name: str, encoded: str, format: BodyFormat | SourceFormat | None) -> Body:
    if format is not None and format.lower() == "application":
        return Body(text=encoded)
    try:
        body = json.loads(encoded)
        validate(body, schema=schemas.BODY_SCHEMA)
        return Body.from_json(body)
    except json.JSONDecodeError as e:
        raise MoeraNodeError(name, 'Invalid body encoding') from e
    except ValidationError as e:
        raise MoeraNodeError(name, 'Invalid body: ' + repr(e)) from e


def decode_bodies(name: str, data):
    if isinstance(data, Sequence):
        return [decode_bodies(name, item) for item in data]
    decoded = deepcopy(data)
    if data.get('stories', None) is not None:
        decoded['stories'] = [decode_bodies(name, item) for item in data['stories']]
    if data.get('comments', None) is not None:
        decoded['comments'] = [decode_bodies(name, item) for item in data['comments']]
    if data.get('comment', None) is not None:
        decoded['comment'] = decode_bodies(name, data['comment'])
    if data.get('posting', None) is not None:
        decoded['posting'] = decode_bodies(name, data['posting'])
    if data.get('body', None) is not None:
        decoded['body'] = decode_body(name, data['body'], data.get('bodyFormat', None))
    if data.get('bodyPreview', None) is not None:
        decoded['bodyPreview'] = decode_body(name, data['bodyPreview'], data.get('bodyFormat', None))
    if data.get('bodySrc', None) is not None:
        decoded['bodySrc'] = decode_body(name, data['bodySrc'], data.get('bodySrcFormat', None))
    return decoded


class NodeAuth(Enum):
    """Authentication type."""
    NONE = 0
    """No authentication."""
    PEER = 1
    """Carte authentication."""
    ADMIN = 2
    """Admin token authentication."""
    ROOT_ADMIN = 3
    """Root admin secret authentication."""


class CarteSource:
    def get_carte(self) -> str:
        raise NotImplemented


FETCH_TIMEOUT = 10 # seconds
UPDATE_TIMEOUT = 60 # seconds
LARGE_BODY_MIN = 65536

def timeout_duration(method: str, body_encoded: str | None, body_file: IO | None) -> int | None:
    if method == "POST" or method == "PUT":
        large_body = body_file is not None or body_encoded is not None and len(body_encoded) > LARGE_BODY_MIN
        duration =  UPDATE_TIMEOUT if large_body else FETCH_TIMEOUT
    else:
        duration = FETCH_TIMEOUT

    return duration

class Caller:
    root: str | None = None
    """API endpoint URL of the node."""
    _root_secret: str | None = None
    _token: str | None = None
    _carte: str | None = None
    _carte_source: CarteSource | None = None
    _auth_method: NodeAuth = NodeAuth.NONE

    def node_url(self, url: str) -> None:
        """Set node URL."""
        self.root = moera_root(url)

    def root_secret(self, secret: str) -> None:
        """Set root secret for authentication."""
        self._root_secret = secret

    def token(self, token: str) -> None:
        """Set admin token for authentication."""
        self._token = token

    def carte(self, carte: str) -> None:
        """Set carte for authentication."""
        self._carte = carte

    def carte_source(self, carte_source: CarteSource) -> None:
        """Set a source of cartes for authentication."""
        self._carte_source = carte_source

    def auth_method(self, auth_method: NodeAuth) -> None:
        """Select authentication method for the following requests."""
        self._auth_method = auth_method

    def no_auth(self) -> None:
        """Switch off authentication for the following requests."""
        self.auth_method(NodeAuth.NONE)

    def auth(self) -> None:
        """Select carte authentication for the following requests."""
        self.auth_method(NodeAuth.PEER)

    def auth_admin(self) -> None:
        """Select admin token authentication for the following requests."""
        self.auth_method(NodeAuth.ADMIN)

    def auth_root_admin(self) -> None:
        """Select root admin secret authentication for the following requests."""
        self.auth_method(NodeAuth.ROOT_ADMIN)

    def call(self, name: str, location: str, params: Mapping[str, str | int | None] | None = None, method: str = 'GET',
             body: Structure | Sequence[Structure] | None = None, body_file: IO | None = None,
             body_file_type: str | None = None, auth: bool = True, schema: Any = None,
             bodies: bool = False, src_bodies: bool = False):
        """
        Generic method for making node API requests.

        :param name: request name (for error messages)
        :param location: request path
        :param params: query parameters, mapping name to value, ``None`` values are skipped
        :param method: request method (one of 'GET', 'POST', 'PUT', 'DELETE')
        :param body: request body
        :param body_file: file to read the request body from
        :param body_file_type: content-type of the request body, when read from a file
        :param auth: `True` to authenticate the request, `False` otherwise
        :param schema: JSON schema to validate the response
        :param bodies: `True` to decode `Body` structures in the response, `False` otherwise
        :param src_bodies: `True` to encode `Body` structures in the request, `False` otherwise
        :return: the decoded response
        """
        response = None
        try:
            body_encoded = None
            if body is not None:
                if src_bodies:
                    body = encode_bodies(body)
                if isinstance(body, Sequence):
                    body_encoded = [b.json() for b in body]
                else:
                    body_encoded = body.json()

            headers = {
                'Accept': 'application/json',
                'Content-Type': 'application/json' if body_file_type is None else body_file_type
            }
            bearer: str | None = None
            if auth:
                match self._auth_method:
                    case NodeAuth.PEER:
                        if self._carte_source is not None:
                            bearer = 'carte:' + self._carte_source.get_carte()
                        elif self._carte is not None:
                            bearer = 'carte:' + self._carte
                        else:
                            raise ValueError('Carte is not set')
                    case NodeAuth.ADMIN:
                        if self._token is None:
                            raise ValueError('Token is not set')
                        bearer = 'token:' + self._token
                    case NodeAuth.ROOT_ADMIN:
                        if self._root_secret is None:
                            raise ValueError('Root secret is not set')
                        bearer = 'secret:' + self._root_secret
            if bearer is not None:
                headers['Authorization'] = f'Bearer {bearer}'

            if self.root is None:
                raise ValueError('Node URL is not set')

            r = requests.request(
                method=method,
                url=self.root + '/api' + location,
                params=params,
                headers=headers,
                json=body_encoded,
                data=body_file,
                stream=schema == "blob",
                timeout=timeout_duration(method, body_encoded, body_file)
            )

            response = r.json()
            if r.status_code not in [200, 201]:
                validate(response, schema=schemas.RESULT_SCHEMA)
                raise MoeraNodeApiError(name, Result.from_json(response))
            if schema is not None and schema != "blob":
                validate(response, schema=schema)

            if bodies:
                return decode_bodies(name, response)
            else:
                return response
        except requests.exceptions.RequestException as e:
            raise MoeraNodeConnectionError(str(e)) from e
        except (requests.exceptions.InvalidJSONError, ValidationError) as e:
            message = f'Invalid server response: {repr(e)}'
            if response is not None:
                message += f'\nResponse:\n{response}'
            raise MoeraNodeError(name, message) from e


def moera_root(url: str) -> str:
    """
    Convert partial node URL to a standardized form.

    :param url: partial URL
    :return: standard URL
    """
    if not url.startswith('http:') and not url.startswith('https:'):
        url = 'https://' + url
    url = url.removesuffix('/').removesuffix('/api')
    if not url.endswith('/moera'):
        url += '/moera'
    return url
