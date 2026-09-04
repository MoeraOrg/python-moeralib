import unittest

from moeralib import NodeSourceUri


class NodeSourceUriTest(unittest.TestCase):

    def test_parses_parameters_and_uses_last_duplicate(self) -> None:
        source = NodeSourceUri.parse(
            'https://example/node?a=b;via_email;name=first;name=last;=ignored'
        )

        self.assertEqual('https://example/node?a=b', source.uri)
        self.assertEqual('', source.get_parameter(NodeSourceUri.VIA_EMAIL))
        self.assertEqual('last', source.get_parameter('name'))
        self.assertEqual(['via_email', 'name'], list(source.parameters))
        self.assertEqual('https://example/node?a=b;via_email=;name=last', str(source))
        self.assertFalse(source.has_parameter(''))
        self.assertIsNone(source.get_parameter('missing'))

    def test_applies_rfc3986_encoding_and_tolerant_decoding(self) -> None:
        source = NodeSourceUri.parse(
            'node;label=%D0%9C%D0%B8%D1%80%20%2B;reserved=%21%27%28%29%2A;equals=a=b;bad=%ZZ%2'
        )

        self.assertEqual('Мир +', source.get_parameter('label'))
        self.assertEqual("!'()*", source.get_parameter('reserved'))
        self.assertEqual('a=b', source.get_parameter('equals'))
        self.assertEqual('%ZZ%2', source.get_parameter('bad'))
        self.assertEqual(
            'node;label=%D0%9C%D0%B8%D1%80%20%2B;reserved=%21%27%28%29%2A;equals=a%3Db;bad=%25ZZ%252',
            str(source)
        )

    def test_supports_default_state_and_programmatic_updates(self) -> None:
        source = NodeSourceUri()

        self.assertEqual('', source.uri)
        self.assertEqual('', str(source))

        source.uri = 'https://example/node?a=b'
        source.set_parameter(NodeSourceUri.VIA_EMAIL, 'true')
        source.set_parameter('', 'ignored')

        self.assertTrue(source.has_parameter(NodeSourceUri.VIA_EMAIL))
        self.assertEqual('https://example/node?a=b;via_email=true', str(source))

    def test_rejects_semicolon_in_programmatic_uri(self) -> None:
        source = NodeSourceUri()

        with self.assertRaises(ValueError):
            source.uri = 'https://example/node;parameter'

    def test_copies_input_and_returns_read_only_view(self) -> None:
        parameters = {'first': 'one', '': 'ignored'}
        source = NodeSourceUri()
        source.set_parameters(parameters)
        view = source.parameters

        parameters['second'] = 'external'
        source.set_parameter('second', 'internal')

        self.assertEqual({'first': 'one', 'second': 'internal'}, view)
        self.assertEqual(view, source.parameters)
        self.assertEqual('internal', source.get_parameter('second'))
        with self.assertRaises(TypeError):
            view['third'] = 'three'  # type: ignore[index]

        source.set_parameters({'fourth': 'replacement'})

        self.assertIsNot(view, source.parameters)
        self.assertEqual({'fourth': 'replacement'}, source.parameters)

    def test_replaces_malformed_utf8_with_replacement_character(self) -> None:
        source = NodeSourceUri.parse('node;value=%FF%61')

        self.assertEqual('\uFFFDa', source.get_parameter('value'))

    def test_identifies_service_from_uri(self) -> None:
        self.assertEqual(
            NodeSourceUri.Service.TELEGRAM,
            NodeSourceUri.parse('https://t.me/moera').get_service()
        )
        self.assertIsNone(NodeSourceUri.parse('https://example.com/moera').get_service())


if __name__ == '__main__':
    unittest.main()
