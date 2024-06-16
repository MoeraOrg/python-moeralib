from __future__ import annotations

from urllib.parse import quote, unquote, urlparse, urlunparse

from .naming.naming import shorten

REDIRECTOR = 'moera.page'


class UniversalLocation:
    """Represents location part of a universal Moera URL."""

    _node_name: str | None
    _scheme: str
    _authority: str | None
    _path: str | None

    query: str | None
    """Query component of the URL."""

    fragment: str | None
    """Fragment identifier of the URL."""

    def __init__(self, node_name: str | None = None, scheme: str | None = None, authority: str | None = None,
                 path: str | None = None, query: str | None = None, fragment: str | None = None):
        """
        :param node_name: the node name
        :param scheme: scheme specifier of the node location (``'https'``, if set to `None` or empty)
        :param authority: authority (host name and optional port) of the node location
        :param path: virtual path at the node (``'/'``, if set to `None` or empty)
        :param query: query component of the URL (without ``?``)
        :param fragment: fragment identifier of the URL (without ``#``)
        """
        self.node_name = node_name
        self.scheme = scheme
        self.authority = authority
        self.path = path
        self.query = query
        self.fragment = fragment

    @property
    def node_name(self) -> str | None:
        """
        The node name.
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name: str | None) -> None:
        self._node_name = shorten(node_name)

    @property
    def scheme(self) -> str:
        """
        Scheme specifier of the node location.
        """
        return self._scheme

    @scheme.setter
    def scheme(self, scheme: str | None) -> None:
        if scheme is None or scheme == '':
            self._scheme = 'https'
        else:
            self._scheme = scheme

    @property
    def authority(self) -> str | None:
        """
        Authority (host name and optional port) of the node location.
        """
        return self._authority

    @authority.setter
    def authority(self, authority: str | None) -> None:
        if authority is None or authority == '':
            self._authority = None
        else:
            self._authority = authority

    @property
    def path(self) -> str | None:
        """
        Virtual path at the node.
        """
        return self._path

    @path.setter
    def path(self, path: str | None) -> None:
        if path is not None and path.startswith('/moera'):
            path = path[6:]
        if path is not None and path != '':
            self._path = path
        else:
            self._path = '/'

    @property
    def location(self) -> str:
        """
        Universal Moera location (without query and fragment).
        """
        loc = '/@'
        if self._node_name is not None:
            loc += quote(self._node_name, safe='')
        loc += '/'
        if self._authority is not None:
            if self._scheme is not None and self._scheme.lower() != 'https':
                loc += self._scheme + ':'
            loc += self._authority
        else:
            loc += '~'
        loc += self._path
        return loc

    def __str__(self) -> str:
        return str(urlunparse(('', '', self.location, '', self.query, self.fragment)))

    def __repr__(self):
        return repr((self._node_name, self._scheme, self._authority, self._path, self.query, self.fragment))


def parse(url: str | None) -> UniversalLocation:
    """
    Parse the location part (including query and fragment) of a universal URL.

    :param url: the URL to be parsed
    :return: the parsed location
    """
    if url is None:
        return UniversalLocation()

    url_parts = urlparse(url)

    path = url_parts.path.removeprefix('/').removesuffix('/')
    if path == '':
        return UniversalLocation()

    dirs = path.split('/')
    if not dirs[0].startswith('@'):
        return UniversalLocation()

    node_name = None
    if len(dirs[0]) > 1:
        node_name = unquote(dirs[0][1:])

    scheme = None
    authority = None
    host = None
    port = None

    if len(dirs) > 1 and dirs[1] != '~':
        parts = dirs[1].split(':')
        i = 0
        if '.' not in parts[i]:
            scheme = parts[i]
            i += 1
        if i < len(parts):
            host = parts[i]
            i += 1
        if i < len(parts):
            port = parts[i]

    if host is not None and host != '':
        authority = host
        if port is not None and port != '':
            authority += ':' + port

    path = ''
    for dir in dirs[2:]:
        path += '/' + dir
    if path == '':
        path = '/'

    return UniversalLocation(node_name, scheme, authority, path, url_parts.query, url_parts.fragment)


def redirect_to_url(node_name: str | None, url: str | None = None) -> str:
    """
    Build a universal Moera URL from the direct URL of a page on a node, adding the node name provided.

    :param node_name: the node name
    :param url: the direct URL
    :return: the universal URL
    """
    try:
        if url is not None:
            url_parts = urlparse(url)
            uni = UniversalLocation(node_name, url_parts.scheme, url_parts.netloc, url_parts.path, url_parts.query,
                                    url_parts.fragment)
        else:
            uni = UniversalLocation(node_name)
        return str(urlunparse(('https', REDIRECTOR, uni.location, '', uni.query, uni.fragment)))
    except ValueError:
        return 'https://' + REDIRECTOR


def redirect_to(node_name: str | None, root_url: str | None, path: str | None = None, query: str | None = None,
                fragment: str | None = None) -> str:
    """
    Build a universal Moera URL from the node name, the Moera root URL of the node, virtual path and other components.

    :param node_name: the node name
    :param root_url: the Moera root URL of the node
    :param path: virtual path at the node (``'/'``, if set to `None` or empty)
    :param query: query component of the URL
    :param fragment: fragment identifier of the URL
    :return: the universal URL
    """
    try:
        if root_url is not None:
            url_parts = urlparse(root_url)
            uni = UniversalLocation(node_name, url_parts.scheme, url_parts.netloc, path, query, fragment)
        else:
            uni = UniversalLocation(node_name, None, None, path, query, fragment)
        return str(urlunparse(('https', REDIRECTOR, uni.location, '', uni.query, uni.fragment)))
    except ValueError:
        return 'https://' + REDIRECTOR
