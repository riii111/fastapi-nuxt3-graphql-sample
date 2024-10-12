from collections.abc import Callable
from datetime import datetime
from typing import Any, TypeVar

from bson import ObjectId
from functions.utils import get_now_utc
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    GetJsonSchemaHandler,
    field_serializer,
)
from pydantic.json_schema import JsonSchemaValue
from pydantic_core import core_schema

DataT = TypeVar("DataT")


class PyObjectId(ObjectId):
    @classmethod  # type: ignore
    def __get_validators__(cls):
        yield cls.validate

    @classmethod  # type: ignore
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod  # type: ignore
    def __get_pydantic_core_schema__(
        cls,
        _source_type: Any,
        _handler: Callable[[Any], core_schema.CoreSchema],
    ) -> core_schema.CoreSchema:
        from_str_schema = core_schema.chain_schema(
            [
                core_schema.str_schema(),
                core_schema.no_info_plain_validator_function(cls.validate),
            ]
        )

        return core_schema.json_or_python_schema(
            json_schema=from_str_schema,
            python_schema=core_schema.union_schema(
                [
                    core_schema.is_instance_schema(ObjectId),
                    from_str_schema,
                ]
            ),
            serialization=core_schema.to_string_ser_schema(),
        )

    @classmethod  # type: ignore
    def __get_pydantic_json_schema__(
        cls, _core_schema: core_schema.CoreSchema, handler: GetJsonSchemaHandler
    ) -> JsonSchemaValue:
        return handler(core_schema.str_schema())


class DateTimeModelMixin(BaseModel):
    created_time: datetime = Field(get_now_utc(), description="作成日時")
    updated_time: datetime = Field(get_now_utc(), description="更新日時")


class IDModelMixin(BaseModel):
    id: PyObjectId = Field(alias="_id", description="オブジェクトID")

    model_config = ConfigDict(arbitrary_types_allowed=True)

    @field_serializer("id")
    def serialize_dt(self, id: ObjectId):
        return str(id)
