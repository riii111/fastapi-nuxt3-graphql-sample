from enum import Enum


class SuperEnumMixIn(Enum):
    @classmethod  # type: ignore
    def to_dict(cls):
        return {e.name: e.value for e in cls}

    @classmethod  # type: ignore
    def items(cls):
        return [(e.name, e.value) for e in cls]

    @classmethod  # type: ignore
    def keys(cls):
        return [e.name for e in cls]

    @classmethod  # type: ignore
    def values(cls):
        return [e.value for e in cls]
