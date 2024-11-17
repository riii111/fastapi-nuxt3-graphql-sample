from depends.common import ListQuery, list_query
from depends.database import get_repository
from fastapi import APIRouter, Depends
from functions.exceptions import NotFoundException, RouteErrorHandler
from models.book import (
    BookCreate,
    CreateBookRequest,
    UpdateBookRequest,
)
from api.schema.book import ListBookResponse, BookResponse
from models.core import PyObjectId
from repositories.book import BookRepository
from usecases.book import BookUseCase
from starlette.status import HTTP_200_OK

router = APIRouter(route_class=RouteErrorHandler)


# BookUseCaseのDI
async def get_book_usecase(
    book_repo: BookRepository = Depends(get_repository(BookRepository)),
) -> BookUseCase:
    return BookUseCase(book_repo)


@router.get(
    "/",
    description="Listメソッド: 本の一覧を取得する",
    response_model=ListBookResponse,
    response_description="本の一覧",
    status_code=HTTP_200_OK,
)
async def list_books(
    list_query: ListQuery = Depends(list_query),
    book_usecase: BookUseCase = Depends(get_book_usecase),
) -> ListBookResponse:
    books = await book_usecase.get_all_books(
        limit=list_query.limit, offset=list_query.offset
    )
    return ListBookResponse(books=books)


@router.get("/{book_id}/", response_model=BookResponse, status_code=HTTP_200_OK)
async def get_book(
    book_id: PyObjectId,
    book_usecase: BookUseCase = Depends(get_book_usecase),
) -> BookResponse:
    try:
        return await book_usecase.get_book_by_id(str(book_id))
    except Exception as e:
        raise NotFoundException(
            message=f"Bookリソース 「book_id: {book_id}」 が見つかりません。"
        ) from e


@router.post("/", response_model=BookResponse, status_code=HTTP_200_OK)
async def create_book(
    request: CreateBookRequest,
    book_usecase: BookUseCase = Depends(get_book_usecase),
) -> BookResponse:
    book = BookCreate(**request.model_dump())
    return await book_usecase.create_book(book_data=book)


@router.put(
    "/{book_id}/",
    description="Updateメソッド: 本情報を更新する",
    response_model=BookResponse,
    response_description="本情報を更新",
    status_code=HTTP_200_OK,
)
async def update_book(
    book_id: PyObjectId,
    request: UpdateBookRequest,
    book_usecase: BookUseCase = Depends(get_book_usecase),
) -> BookResponse:
    return await book_usecase.update_book(book_id=str(book_id), book_update=request)


@router.delete(
    "/{book_id}/",
    description="Deleteメソッド: 本情報を削除する",
    response_model=None,
    response_description="本情報を削除",
    status_code=HTTP_200_OK,
)
async def delete_book(
    book_id: PyObjectId,
    book_usecase: BookUseCase = Depends(get_book_usecase),
) -> None:
    await book_usecase.delete_book(str(book_id))
    return
