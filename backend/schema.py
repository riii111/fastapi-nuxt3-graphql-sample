import strawberry
from typing import List
from repositories.book import BookRepository
from models.book import BookView
from db.session import client
from usecases.book import BookUseCase
from models.core import PyObjectId
from strawberry import auto, field


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


# Pydanticのモデルをstrawberryの型に変換するためのクラス
@strawberry.experimental.pydantic.type(model=BookView)
class Book:
    id: ObjectIdScalar
    name: auto
    price_without_tax: auto
    tax_rate: auto
    created_time: auto
    updated_time: auto

    @field
    def price_with_tax(self) -> int:
        return int(self.price_without_tax * (1.0 + self.tax_rate))


@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello World"

    @strawberry.field
    async def books(self) -> List[Book]:
        book_repo = BookRepository(client.db)
        book_usecase = BookUseCase(book_repo)
        results = await book_usecase.get_all_books()
        return [
            BookView(**{**book.model_dump(exclude={"secret"}), "_id": book.id})
            for book in results
        ]


schema = strawberry.Schema(query=Query)
