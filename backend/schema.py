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

schema = strawberry.Schema(query=Query)
        book_usecase = BookUseCase(book_repo)
        results = await book_usecase.get_all_books()
        return [Book.from_pydantic(book) for book in results]

    @strawberry.field
    async def book(self, id: str) -> Book:
        book_repo = BookRepository(client.db)
        book_usecase = BookUseCase(book_repo)
        result = await book_usecase.get_book_by_id(id)
        return Book.from_pydantic(result)
