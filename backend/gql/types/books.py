import strawberry
from models.book import BookView, CreateBookRequest, ListBookResponse, UpdateBookRequest
from models.core import PyObjectId

# PyObjectIdをスカラー型としてシリアライズ
PyObjectIdType = strawberry.scalar(PyObjectId, serialize=str, parse_value=PyObjectId)


# PydanticのモデルをGraphQLの型に変換
@strawberry.experimental.pydantic.type(model=BookView, all_fields=True)
class BookViewType:
    @strawberry.field
    def price_with_tax(self) -> int:
        return self.price_with_tax


@strawberry.experimental.pydantic.type(model=ListBookResponse, all_fields=True)
class ListBookResponseType:
    @strawberry.field
    def counts(self) -> int:
        return len(self.books)


@strawberry.experimental.pydantic.input(model=CreateBookRequest, all_fields=True)
class CreateBookInput:
    pass


@strawberry.experimental.pydantic.input(model=UpdateBookRequest, all_fields=True)
class UpdateBookInput:
    pass
