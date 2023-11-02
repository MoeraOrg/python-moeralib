from __future__ import annotations

from base64 import b64decode
from typing import Any, TypeVar, get_type_hints, get_args, Mapping, List

from camel_converter import dict_to_snake, to_camel


class Structure:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    @classmethod
    def from_json(cls, data) -> Structure | None:
        if data is None:
            return None
        data = dict_to_snake(data)
        for (attr, value) in data.items():
            if value is not None:
                if is_bytes_attribute(cls, attr):
                    data[attr] = b64decode(value)
                else:
                    struct = get_structure_attribute_type(cls, attr)
                    if struct is not None and not isinstance(value, Structure):
                        if isinstance(value, list):
                            data[attr] = [struct.from_json(v) for v in value]
                        else:
                            data[attr] = struct.from_json(value)
        instance = cls()
        instance.__dict__.update(data)
        return instance

    @staticmethod
    def list_to_json(a_list):
        out = []
        for item in a_list:
            if isinstance(item, Structure):
                out.append(item.json())
            elif isinstance(item, list):
                out.append(Structure.list_to_json(item))
            else:
                out.append(item)
        return out

    def json(self):
        json = {}
        for name, value in self.__dict__.items():
            if name.startswith('_'):
                continue
            if isinstance(value, Structure):
                value = value.json()
            elif isinstance(value, list):
                value = Structure.list_to_json(value)
            json[to_camel(name)] = value
        return json

    def __repr__(self) -> str:
        return repr(self.json())


StructType = TypeVar('StructType', bound=Structure)


def is_bytes_attribute(struct_type: type[StructType], attr: str) -> bool:
    hints = get_type_hints(struct_type)
    return attr in hints and (hints[attr] == bytes or bytes in get_args(hints[attr]))


def is_structure(type_hint: Any) -> bool:
    return isinstance(type_hint, type) and issubclass(type_hint, Structure)


def is_list_generic(type_hint: Any) -> bool:
    return hasattr(type_hint, '__origin__') and type_hint.__origin__ == list


def get_structure_attribute_type(struct_type: type[StructType], attr: str) -> type[Structure] | None:
    hints = get_type_hints(struct_type)
    if attr not in hints:
        return None
    if is_structure(hints[attr]):
        return hints[attr]
    for hint in get_args(hints[attr]):
        if is_structure(hint):
            return hint
        if is_list_generic(hint):
            for list_hint in get_args(hint):
                if is_structure(list_hint):
                    return list_hint
    return None


def array_schema(schema: Any) -> Any:
    return {
        "type": "array",
        "items": schema
    }


def to_nullable_object_schema(schema: Any) -> Any:
    result = schema.copy()
    result.update(type=["object", "null"])
    return result


def structure_or_none(data, struct_type: type[StructType]) -> StructType | None:
    return struct_type.from_json(data) if data is not None else None


def structure_list(data, struct_type: type[StructType]) -> List[StructType]:
    return [struct_type.from_json(item) for item in data]


def comma_separated_flags(flags: Mapping[str, bool]) -> str | None:
    names = [name for name, value in flags.items() if value is not None]
    return ','.join(names) if len(names) > 0 else None
