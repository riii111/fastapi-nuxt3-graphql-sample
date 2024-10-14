import strawberry
from typing import List
from repositories.book import BookRepository
from db.session import client
from usecases.book import BookUseCase
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


# Pydanticのモデルをstrawberryの型に変換するためのクラス
@strawberry.experimental.pydantic.type(model=BookView)
class Book:
    id: ObjectIdScalar

    @classmethod
    def from_pydantic(cls, pydantic_model: BookView) -> "Book":
        book_dict = pydantic_model.dict()
        book_dict["id"] = ObjectIdScalar.serialize(pydantic_model.id)
        return cls(**book_dict)


@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello World"

    @strawberry.field
    async def books(self) -> List[Book]:
        book_repo = BookRepository(client.db)
        results: list[BookView] = await book_repo.find_many()
        books = [
            Book(
                id=str(book.id),
                name=book.name,
                price_without_tax=book.price_without_tax,
                tax_rate=book.tax_rate,
                price_with_tax=book.price_with_tax,
                created_at=book.created_at.isoformat(),
                updated_at=book.updated_at.isoformat(),
            )
            for book in results
        ]
        return books

schema = strawberry.Schema(query=Query)
