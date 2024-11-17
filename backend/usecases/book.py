from models.book import BookCreate, BookInDB, UpdateBookRequest
from api.schema.book import BookResponse
from models.core import PyObjectId
from repositories.book import BookRepository


class BookUseCase:
    def __init__(self, book_repo: BookRepository):
        self.book_repo = book_repo

    async def get_all_books(
        self,
        *,
        limit: int | None = None,
        offset: int = 0,
        filter_: dict = {},
        sorts: list[tuple[str, int]] = [("created_at", 1)],
    ) -> list[BookInDB]:
        active_filter = {**filter_, "deleted_at": None}
        return await self.book_repo.find_many(
            limit=limit, offset=offset, filter_=active_filter, sorts=sorts
        )

    async def get_book_by_id(self, book_id: str) -> BookResponse:
        result = await self.book_repo.find_one(filter_={"_id": PyObjectId(book_id)})
        if result is None:
            raise Exception(f"ID {book_id} の本が見つかりません")
        return result

    async def create_book(self, book_data: BookCreate) -> BookResponse:
        created_book = await self.book_repo.insert_one(book=book_data)
        return created_book

    async def update_book(
        self, *, book_id: str, book_update: UpdateBookRequest
    ) -> BookInDB:
        result = await self.book_repo.update_one(
            filter_={"_id": PyObjectId(book_id)}, update=book_update
        )
        if not result:
            raise Exception(f"ID {book_id} の本が見つかりません")
        return result

    async def delete_book(self, book_id: str) -> bool:
        await self.book_repo.delete_one(_id=book_id)
        return True
