import strawberry
from models.book import BookView
from models.core import PyObjectId

# PyObjectIdをスカラー型としてシリアライズ
PyObjectIdType = strawberry.scalar(PyObjectId, serialize=str, parse_value=PyObjectId)


# PydanticのモデルをGraphQLの型に変換
@strawberry.experimental.pydantic.type(model=BookView, all_fields=True)
class BookViewType:
    pass
