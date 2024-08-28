from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from ecpy.curves import Curve
from mnemonic import Mnemonic

from .fingerprint import Fingerprint, FingerprintSchema, FingerprintWriter


def generate_key() -> ec.EllipticCurvePrivateKey:
    """
    Generate a pair of cryptographic keys.

    :return: the keys
    """
    return ec.generate_private_key(ec.SECP256K1())


def generate_mnemonic_key() -> (str, ec.EllipticCurvePrivateKey):
    """
    Generate a pair of cryptographic keys with a mnemonic for the private key.

    :return: the mnemonic and the keys
    """
    mnemonic = Mnemonic().generate(strength=256)
    private_key = mnemonic_to_private_key(mnemonic)
    return mnemonic, private_key


def mnemonic_to_private_key(mnemonic: str) -> ec.EllipticCurvePrivateKey:
    """
    Restore a private key from the given mnemonic.

    :param mnemonic: the mnemonic
    :return: the private key
    """
    seed = Mnemonic().to_seed(mnemonic)
    private_value = int.from_bytes(seed, 'big') % Curve.get_curve('secp256k1').field
    private_key = ec.derive_private_key(private_value, ec.SECP256K1())
    return private_key


def raw_public_key(public_key: ec.EllipticCurvePublicKey) -> bytes:
    """
    Convert a public key to the raw format used by the naming server.

    :param public_key: the public key
    :return: the raw public key
    """
    numbers = public_key.public_numbers()
    return numbers.x.to_bytes(32, 'big') + numbers.y.to_bytes(32, 'big')


def raw_to_public_key(raw_public_key: bytes) -> ec.EllipticCurvePublicKey:
    """
    Restore a public key from the raw format.

    :param raw_public_key: the raw public key
    :return: the public key
    """
    x = int.from_bytes(raw_public_key[:32], 'big')
    y = int.from_bytes(raw_public_key[32:], 'big')
    return ec.EllipticCurvePublicNumbers(x, y, ec.SECP256K1()).public_key()


def raw_private_key(private_key: ec.EllipticCurvePrivateKey) -> bytes:
    """
    Convert a private key to the raw format to pass to the client.

    :param private_key: the private key
    :return: the raw private key
    """
    return private_key.private_numbers().private_value.to_bytes(32, 'big')


def raw_to_private_key(raw_private_key: bytes) -> ec.EllipticCurvePrivateKey:
    """
    Restore a private key from the raw format.

    :param raw_private_key: the raw private key
    :return: the private key
    """
    return ec.derive_private_key(int.from_bytes(raw_private_key, 'big'), ec.SECP256K1())


def fingerprint_bytes(fingerprint: Fingerprint, schema: FingerprintSchema) -> bytes:
    """
    Encode a fingerprint in the binary form, using the given fingerprint data and schema.

    :param fingerprint: the fingerprint data
    :param schema: the fingerprint schema
    :return: the fingerprint in the binary form
    """
    writer = FingerprintWriter()
    writer.append(fingerprint, schema)
    return writer.to_bytes()


def digest_fingerprint(fingerprint: bytes) -> bytes:
    """
    Calculate a cryptographic digest of the fingerprint.

    :param fingerprint: the fingerprint
    :return: the digest
    """
    digest = hashes.Hash(hashes.SHA3_256())
    digest.update(fingerprint)
    return digest.finalize()


def sign_fingerprint(fingerprint: bytes, private_key: ec.EllipticCurvePrivateKey) -> bytes:
    """
    Sign a fingerprint with a private key.

    :param fingerprint: the fingerprint to be signed
    :param private_key: the private key
    :return: the signature
    """
    return private_key.sign(fingerprint, ec.ECDSA(hashes.SHA3_256()))


def verify_fingerprint_signature(fingerprint: bytes, signature: bytes, public_key: ec.EllipticCurvePublicKey) -> bool:
    """
    Verify a fingerprint signature with the given public key.

    :param fingerprint: the original fingerprint
    :param signature: the signature to be verified
    :param public_key: the public key for verification
    :return: `True`, if the signature is correct, `False` otherwise
    """
    try:
        public_key.verify(signature, fingerprint, ec.ECDSA(hashes.SHA3_256()))
        return True
    except InvalidSignature:
        return False
