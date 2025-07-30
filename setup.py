from setuptools import setup

setup(
    name='moeralib',
    version='0.17.1',
    install_requires=[
        "requests>=2.32.0",
        'camel-converter',
        'jsonschema>=4.19.0',
        "cryptography~=43.0.1",
        'mnemonic',
        'ecpy',
    ],
)
