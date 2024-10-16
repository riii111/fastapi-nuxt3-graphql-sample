from typing import AsyncGenerator

from db.session import client
from fastapi import Depends
from repositories.book import BookRepository
from strawberry.fastapi import BaseContext
from usecases.book import BookUseCase


class GraphQLContext(BaseContext):
    def __init__(self, book_usecase: BookUseCase):
        super().__init__()
        self.book_usecase = book_usecase


async def get_book_usecase() -> AsyncGenerator[BookUseCase, None]:
    book_repo = BookRepository(client.db)
    yield BookUseCase(book_repo)


async def get_context(
    book_usecase: BookUseCase = Depends(get_book_usecase),
) -> GraphQLContext:
    return GraphQLContext(book_usecase=book_usecase)
