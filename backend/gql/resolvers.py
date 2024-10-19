from typing import List

from strawberry.types import Info

from .context import GraphQLContext
from .types import BookViewType, CreateBookInput, ListBookResponseType, UpdateBookInput


async def get_books(info: Info[GraphQLContext, None]) -> ListBookResponseType:
    books = await info.context.book_usecase.get_all_books()
    book_views = [BookViewType(**book.model_dump(exclude={"secret"})) for book in books]
    return ListBookResponseType(books=book_views)


async def get_book_by_id(
    info: Info[GraphQLContext, None], book_id: str
) -> BookViewType:
    book = await info.context.book_usecase.get_book_by_id(book_id)
    return BookViewType(**book.model_dump(exclude={"secret"}))
