import strawberry
from models.core import PyObjectId

# PyObjectIdをスカラー型としてシリアライズ
PyObjectIdType = strawberry.scalar(PyObjectId, serialize=str, parse_value=PyObjectId)
