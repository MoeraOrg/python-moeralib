from typing import TypeAlias, Literal

from ..structure import Structure

Timestamp: TypeAlias = int
OperationStatus: TypeAlias = Literal['WAITING', 'ADDED', 'STARTED', 'SUCCEEDED', 'FAILED', 'UNKNOWN']


class OperationStatusInfo(Structure):
    operation_id: str
    name: str
    """the name that was created or updated by the operation"""
    generation: int
    """the generation of the name that was created or updated by the operation"""
    status: OperationStatus
    """the current status of the operation"""
    added: Timestamp | None = None
    """when the operation was added"""
    completed: Timestamp | None = None
    """when the operation was completed"""
    error_code: str | None = None
    """the error code, if the operation has been failed"""
    error_message: str | None = None
    """the human-readable error description, if the operation has been failed"""


class RegisteredNameInfo(Structure):
    name: str
    generation: int
    updating_key: bytes | None = None
    """the public key for verifying signatures of further updates of the name"""
    node_uri: str
    """URI of the REST API endpoint of the node to which the name is assigned"""
    created: Timestamp | None = None
    """when the name was created"""
    signing_key: bytes | None = None
    """the public key of the name owner. May be ``None``."""
    valid_from: Timestamp | None = None
    """the moment in time the owner's key is valid from. May be absent if ``signingKey`` is also absent."""
    digest: bytes | None = None
    """
    a unique identifier of the current state of the name. May be a transaction ID of the latest transaction with
    this name in the blockchain, or a cryptographic digest of the current state.
    """


class SigningKeyInfo(Structure):
    key: bytes
    """the public key"""
    valid_from: Timestamp
    """the moment in time the key is valid from"""
