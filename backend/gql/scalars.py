import strawberry
from models.core import PyObjectId


# PyObjectIdをGraphQLで使用するため、カスタムスカラー型として定義
@strawberry.scalar(
    description="Custom scalar for MongoDB ObjectId",
    serialize=str,
    parse_value=PyObjectId,
)
class ObjectIdScalar:
    @staticmethod
    def serialize(value: PyObjectId) -> str:
        return str(value)

    @staticmethod
    def parse_value(value: str) -> PyObjectId:
        return PyObjectId(value)
