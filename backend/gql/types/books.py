import strawberry
from models.book import CreateBookRequest, UpdateBookRequest
from api.schema.book import ListBookResponse, BookResponse


# PydanticのモデルをGraphQLの型に変換
@strawberry.experimental.pydantic.type(model=BookResponse, all_fields=True)
class BookType:
    @strawberry.field
    def price_with_tax(self) -> int:
        return int(self.price_without_tax * (1.0 + self.tax_rate))


@strawberry.experimental.pydantic.type(model=ListBookResponse, all_fields=True)
class ListBookType:
    @strawberry.field
    def counts(self) -> int:
        return len(self.books)


@strawberry.experimental.pydantic.input(model=CreateBookRequest, all_fields=True)
class CreateBookInput:
    pass


@strawberry.experimental.pydantic.input(model=UpdateBookRequest, all_fields=True)
class UpdateBookInput:
    pass
