from ..crypto.crypto import fingerprint_bytes
from ..crypto.fingerprint import FingerprintSchema

PUT_CALL_FINGERPRINT0_SCHEMA: FingerprintSchema = [
    ('version', 'number'),
    ('name', 'string'),
    ('generation', 'number'),
    ('updating_key', 'bytes'),
    ('node_uri', 'string'),
    ('signing_key', 'bytes'),
    ('valid_from', 'number'),
    ('previous_digest', 'bytes'),
]


def create_put_call_fingerprint0(name: str, generation: int, updating_key: bytes, node_uri: str, signing_key: bytes,
                                 valid_from: int, previous_digest: bytes | None) -> bytes:
    return fingerprint_bytes({'version': 0} | locals(), PUT_CALL_FINGERPRINT0_SCHEMA)
