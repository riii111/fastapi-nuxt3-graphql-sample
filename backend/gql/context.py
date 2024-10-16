from typing import AsyncGenerator
from strawberry.fastapi import BaseContext
from db.session import client
from repositories.book import BookRepository
from usecases.book import BookUseCase
from fastapi import Depends
from starlette.requests import Request


class GraphQLContext(BaseContext):
    def __init__(self, book_usecase: BookUseCase):
        super().__init__()
        self.book_usecase = book_usecase


async def get_book_usecase() -> AsyncGenerator[BookUseCase, None]:
    book_repo = BookRepository(client.db)
    yield BookUseCase(book_repo)


async def get_context(
    request: Request,
    book_usecase: BookUseCase = Depends(get_book_usecase),
) -> GraphQLContext:
    return GraphQLContext(book_usecase=book_usecase)
