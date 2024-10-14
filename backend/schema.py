import strawberry
from typing import List
from models.core import PyObjectId
from repositories.book import BookRepository
from models.book import BookView
from db.session import client


@strawberry.type
class Book:
    id: str
    name: str
    price_without_tax: int
    tax_rate: float
    price_with_tax: int
    created_at: str
    updated_at: str


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
