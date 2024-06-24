# This file is generated

from typing import List

from ..crypto.crypto import fingerprint_bytes
from ..crypto.fingerprint import FingerprintSchema
from .types import Timestamp

ATTACHMENT_FINGERPRINT0_SCHEMA: FingerprintSchema = [
    ('version', 'number'),
    ('object_type', 'string'),
    ('digest', 'bytes'),
]


def create_attachment_fingerprint0(digest: bytes | None) -> bytes:
    return fingerprint_bytes({'version': 0, 'object_type': 'ATTACHMENT'} | locals(), ATTACHMENT_FINGERPRINT0_SCHEMA)


CARTE_FINGERPRINT1_SCHEMA: FingerprintSchema = [
    ('version', 'number'),
    ('object_type', 'string'),
    ('owner_name', 'string'),
    ('address', 'string'),
    ('beginning', 'number'),
    ('deadline', 'number'),
    ('node_name', 'string'),
    ('auth_category', 'number'),
    ('salt', 'bytes'),
]


def create_carte_fingerprint1(
    owner_name: str | None, address: str | None, beginning: Timestamp | None, deadline: Timestamp | None,
    node_name: str | None, auth_category: int | None, salt: bytes | None
) -> bytes:
    return fingerprint_bytes({'version': 1, 'object_type': 'CARTE'} | locals(), CARTE_FINGERPRINT1_SCHEMA)


CARTE_FINGERPRINT0_SCHEMA: FingerprintSchema = [
    ('version', 'number'),
    ('object_type', 'string'),
    ('owner_name', 'string'),
    ('address', 'string'),
    ('beginning', 'number'),
    ('deadline', 'number'),
    ('permissions', 'number'),
    ('salt', 'bytes'),
]


def create_carte_fingerprint0(
    owner_name: str | None, address: str | None, beginning: Timestamp | None, deadline: Timestamp | None,
    permissions: int | None, salt: bytes | None
) -> bytes:
    return fingerprint_bytes({'version': 0, 'object_type': 'CARTE'} | locals(), CARTE_FINGERPRINT0_SCHEMA)


COMMENT_FINGERPRINT0_SCHEMA: FingerprintSchema = [
    ('version', 'number'),
    ('object_type', 'string'),
    ('owner_name', 'string'),
    ('posting_fingerprint', 'bytes'),
    ('replied_to_fingerprint', 'bytes'),
    ('body_src_hash', 'bytes'),
    ('body_src_format', 'string'),
    ('body', 'string'),
    ('body_format', 'string'),
    ('created_at', 'number'),
    ('permissions', 'number'),
    ('attachments', 'bytes[]'),
]


def create_comment_fingerprint0(
    owner_name: str | None, posting_fingerprint: bytes | None, replied_to_fingerprint: bytes | None,
    body_src_hash: bytes | None, body_src_format: str | None, body: str | None, body_format: str | None,
    created_at: Timestamp | None, permissions: int | None, attachments: List[bytes] | None
) -> bytes:
    return fingerprint_bytes({'version': 0, 'object_type': 'COMMENT'} | locals(), COMMENT_FINGERPRINT0_SCHEMA)


NOTIFICATION_PACKET_FINGERPRINT1_SCHEMA: FingerprintSchema = [
    ('version', 'number'),
    ('object_type', 'string'),
    ('id', 'string'),
    ('node_name', 'string'),
    ('full_name', 'string'),
    ('created_at', 'number'),
    ('type', 'string'),
    ('notification', 'string'),
]


def create_notification_packet_fingerprint1(
    id: str | None, node_name: str | None, full_name: str | None, created_at: Timestamp | None, type: str | None,
    notification: str | None
) -> bytes:
    return fingerprint_bytes(
        {'version': 1, 'object_type': 'NOTIFICATION_PACKET'} | locals(), NOTIFICATION_PACKET_FINGERPRINT1_SCHEMA
    )


NOTIFICATION_PACKET_FINGERPRINT0_SCHEMA: FingerprintSchema = [
    ('version', 'number'),
    ('object_type', 'string'),
    ('id', 'string'),
    ('node_name', 'string'),
    ('created_at', 'number'),
    ('type', 'string'),
    ('notification', 'string'),
]


def create_notification_packet_fingerprint0(
    id: str | None, node_name: str | None, created_at: Timestamp | None, type: str | None, notification: str | None
) -> bytes:
    return fingerprint_bytes(
        {'version': 0, 'object_type': 'NOTIFICATION_PACKET'} | locals(), NOTIFICATION_PACKET_FINGERPRINT0_SCHEMA
    )


POSTING_FINGERPRINT1_SCHEMA: FingerprintSchema = [
    ('version', 'number'),
    ('object_type', 'string'),
    ('receiver_name', 'string'),
    ('owner_name', 'string'),
    ('body_src_hash', 'bytes'),
    ('body_src_format', 'string'),
    ('body', 'string'),
    ('body_format', 'string'),
    ('created_at', 'number'),
    ('permissions', 'number'),
    ('attachments', 'bytes[]'),
]


def create_posting_fingerprint1(
    receiver_name: str | None, owner_name: str | None, body_src_hash: bytes | None, body_src_format: str | None,
    body: str | None, body_format: str | None, created_at: Timestamp | None, permissions: int | None,
    attachments: List[bytes] | None
) -> bytes:
    return fingerprint_bytes({'version': 1, 'object_type': 'POSTING'} | locals(), POSTING_FINGERPRINT1_SCHEMA)


POSTING_FINGERPRINT0_SCHEMA: FingerprintSchema = [
    ('version', 'number'),
    ('object_type', 'string'),
    ('receiver_name', 'string'),
    ('owner_name', 'string'),
    ('body_src_hash', 'bytes'),
    ('body_src_format', 'string'),
    ('body', 'string'),
    ('body_format', 'string'),
    ('created_at', 'number'),
    ('permissions', 'number'),
    ('attachments', 'number'),
]


def create_posting_fingerprint0(
    receiver_name: str | None, owner_name: str | None, body_src_hash: bytes | None, body_src_format: str | None,
    body: str | None, body_format: str | None, created_at: Timestamp | None, permissions: int | None,
    attachments: int | None
) -> bytes:
    return fingerprint_bytes({'version': 0, 'object_type': 'POSTING'} | locals(), POSTING_FINGERPRINT0_SCHEMA)


REACTION_FINGERPRINT0_SCHEMA: FingerprintSchema = [
    ('version', 'number'),
    ('object_type', 'string'),
    ('owner_name', 'string'),
    ('entry_fingerprint', 'bytes'),
    ('negative', 'boolean'),
    ('emoji', 'number'),
]


def create_reaction_fingerprint0(
    owner_name: str | None, entry_fingerprint: bytes | None, negative: bool | None, emoji: int | None
) -> bytes:
    return fingerprint_bytes({'version': 0, 'object_type': 'REACTION'} | locals(), REACTION_FINGERPRINT0_SCHEMA)


SHERIFF_ORDER_FINGERPRINT0_SCHEMA: FingerprintSchema = [
    ('version', 'number'),
    ('object_type', 'string'),
    ('sheriff_name', 'string'),
    ('node_name', 'string'),
    ('feed_name', 'string'),
    ('entry_fingerprint', 'bytes'),
    ('category', 'string'),
    ('reason_code', 'string'),
    ('reason_details', 'string'),
    ('created_at', 'number'),
]


def create_sheriff_order_fingerprint0(
    sheriff_name: str | None, node_name: str | None, feed_name: str | None, entry_fingerprint: bytes | None,
    category: str | None, reason_code: str | None, reason_details: str | None, created_at: Timestamp | None
) -> bytes:
    return fingerprint_bytes(
        {'version': 0, 'object_type': 'SHERIFF_ORDER'} | locals(), SHERIFF_ORDER_FINGERPRINT0_SCHEMA
    )
