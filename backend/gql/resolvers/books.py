import strawberry
from db.schema.core import PyObjectId
from models.book import CreateBookRequest, UpdateBookRequest
from strawberry.types import Info

from ..context import GraphQLContext
from ..types.books import (
    BookResponse,
    BookType,
    CreateBookInput,
    ListBookResponse,
    ListBookType,
    UpdateBookInput,
)


async def get_books(
    info: Info[GraphQLContext, None],
    limit: int | None = None,
    offset: int = 0,
) -> ListBookType:
    books = await info.context.book_usecase.get_all_books(limit=limit, offset=offset)
    book_responses = [BookResponse(**book.model_dump(by_alias=True)) for book in books]
    response = ListBookResponse(books=book_responses)
    return ListBookType.from_pydantic(response)


async def get_book_by_id(
    info: Info[GraphQLContext, None], book_id: PyObjectId
) -> BookType | None:
    book = await info.context.book_usecase.get_book_by_id(book_id)
    if book:
        book_response = BookResponse(**book.model_dump(by_alias=True))
        return BookType.from_pydantic(book_response)
    return None


async def create_book(
    info: Info[GraphQLContext, None], book_data: CreateBookInput
) -> BookType:
    pydantic_data = book_data.to_pydantic()
    create_request = CreateBookRequest(**pydantic_data.model_dump())
    created_book = await info.context.book_usecase.create_book(book=create_request)
    book_response = BookResponse(**created_book.model_dump(by_alias=True))
    return BookType.from_pydantic(book_response)


async def update_book(
    info: Info[GraphQLContext, None],
    book_id: PyObjectId,
    book_data: UpdateBookInput,
) -> BookType:
    pydantic_data = book_data.to_pydantic()
    update_request = UpdateBookRequest(**pydantic_data.model_dump())
    updated_book = await info.context.book_usecase.update_book(
        book_id=book_id, book_update=update_request
    )
    book_response = BookResponse(**updated_book.model_dump(by_alias=True))
    return BookType.from_pydantic(book_response)


async def delete_book(info: Info[GraphQLContext, None], book_id: PyObjectId) -> bool:
    return await info.context.book_usecase.delete_book(book_id)
