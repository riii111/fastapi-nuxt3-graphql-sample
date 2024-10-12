from depends.common import ListQuery, list_query
from depends.database import get_repository
from fastapi import APIRouter, Depends
from functions.exceptions import NotFoundException, RouteErrorHandler
from models.book import (
    BookCreate,
    BookInDB,
    BookView,
    CreateBookRequest,
    ListBookResponse,
    UpdateBookRequest,
)
from models.core import PyObjectId
from repositories.book import BookRepository
from starlette.status import HTTP_200_OK

router = APIRouter(route_class=RouteErrorHandler)


@router.get(
    "/",
    description="Listメソッド: 本の一覧を取得する",
    response_model=ListBookResponse,
    response_description="本の一覧",
    status_code=HTTP_200_OK,
)
async def list_books(
    list_query: ListQuery = Depends(list_query),
    book_repo: BookRepository = Depends(get_repository(BookRepository)),
):
    results: list[BookInDB] = await book_repo.find_many(
        limit=list_query.limit, offset=list_query.offset
    )
    books: list[BookView] = [
        BookView(**result.model_dump(by_alias=True)) for result in results
    ]
    return ListBookResponse(books=books)


@router.get(
    "/{book_id}/",
    description="Getメソッド: 本を取得する",
    response_model=BookView,
    response_description="本の取得",
    status_code=HTTP_200_OK,
)
async def get_book(
    book_id: PyObjectId,
    book_repo: BookRepository = Depends(get_repository(BookRepository)),
) -> BookView:
    result: None | BookInDB = await book_repo.find_one_filter_by_id(_id=book_id)
    if not result:
        raise NotFoundException(message=f"Bookリソース 「book_id: {book_id}」 が見つかりません。")
    return BookView(**result.model_dump(by_alias=True), by_alias=True)


@router.post(
    "/",
    description="Createメソッド: 本を新規に登録する",
    response_model=BookView,
    response_description="本の新規登録",
    status_code=HTTP_200_OK,
)
async def create_book(
    request: CreateBookRequest,
    book_repo: BookRepository = Depends(get_repository(BookRepository)),
) -> BookView:
    book: BookCreate = BookCreate(**request.model_dump())
    created_id: PyObjectId = await book_repo.create_one(book=book)
    return await get_book(book_id=created_id, book_repo=book_repo)


@router.put(
    "/{book_id}/",
    description="Updateメソッド: 本情報を更新する",
    response_model=BookView,
    response_description="本情報を更新",
    status_code=HTTP_200_OK,
)
async def update_book(
    book_id: PyObjectId,
    request: UpdateBookRequest,
    book_repo: BookRepository = Depends(get_repository(BookRepository)),
) -> BookView:
    _ = await book_repo.update_one_filter_by_id(book=request, _id=book_id)
    return await get_book(book_id=book_id, book_repo=book_repo)


@router.delete(
    "/{book_id}/",
    description="Deleteメソッド: 本情報を削除する",
    response_model=None,
    response_description="本情報を削除",
    status_code=HTTP_200_OK,
)
async def delete_book(
    book_id: PyObjectId,
    book_repo: BookRepository = Depends(get_repository(BookRepository)),
) -> None:
    await book_repo.delete_one_filter_by_id(_id=book_id)
    return
