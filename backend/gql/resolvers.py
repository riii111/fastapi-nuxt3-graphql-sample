from models.book import CreateBookRequest, UpdateBookRequest
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


async def create_book(
    info: Info[GraphQLContext, None], book_data: CreateBookInput
) -> BookViewType:
    create_request = CreateBookRequest(**book_data.__dict__)
    created_book = await info.context.book_usecase.create_book(create_request)
    return BookViewType(**created_book.model_dump(exclude={"secret"}))


async def update_book(
    info: Info[GraphQLContext, None], book_id: str, book_data: UpdateBookInput
) -> BookViewType:
    update_request = UpdateBookRequest(
        **{k: v for k, v in book_data.__dict__.items() if v is not None}
    )
    updated_book = await info.context.book_usecase.update_book(book_id, update_request)
    return BookViewType(**updated_book.model_dump(exclude={"secret"}))


async def delete_book(info: Info[GraphQLContext, None], book_id: str) -> bool:
    return await info.context.book_usecase.delete_book(book_id)
