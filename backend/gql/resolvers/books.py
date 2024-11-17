from models.core import PyObjectId
from models.book import CreateBookRequest, UpdateBookRequest
from strawberry.types import Info

from ..context import GraphQLContext
from gql.types.books import (
    BookType,
    CreateBookInput,
    ListBookType,
    UpdateBookInput,
)


async def get_books(
    info: Info[GraphQLContext, None],
    limit: int | None = None,
    offset: int = 0,
) -> ListBookType:
    books = await info.context.book_usecase.get_all_books(limit=limit, offset=offset)
    book_responses = [BookType.from_pydantic(book) for book in books]
    response = ListBookType(books=book_responses)
    return response


async def get_book_by_id(
    info: Info[GraphQLContext, None], book_id: PyObjectId
) -> BookType | None:
    book = await info.context.book_usecase.get_book_by_id(book_id)
    if book:
        return BookType.from_pydantic(book)
    return None


async def create_book(
    info: Info[GraphQLContext, None], book_data: CreateBookInput
) -> BookType:
    pydantic_data = book_data.to_pydantic()
    create_request = CreateBookRequest(**pydantic_data.model_dump())
    created_book = await info.context.book_usecase.create_book(book_data=create_request)
    return BookType.from_pydantic(created_book)


async def update_book(
    info: Info[GraphQLContext, None],
    book_id: PyObjectId,
    book_data: UpdateBookInput,
) -> BookType:
    pydantic_data = book_data.to_pydantic()
    update_request = UpdateBookRequest(**pydantic_data.model_dump())
    updated_book = await info.context.book_usecase.update_book(
        book_id=str(book_id), book_update=update_request
    )
    return BookType.from_pydantic(updated_book)


async def delete_book(info: Info[GraphQLContext, None], book_id: PyObjectId) -> bool:
    return await info.context.book_usecase.delete_book(book_id)
