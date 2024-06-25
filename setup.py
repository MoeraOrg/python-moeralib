from setuptools import setup

setup(
    name='moeralib',
    version='0.15.4',
    install_requires=[
        'requests>=2.31.0',
        'camel-converter',
        'jsonschema>=4.19.0',
        'cryptography~=42.0.4',
        'mnemonic',
        'ecpy',
    ],
)
