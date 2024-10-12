from models.book import BOOK_COLLECTION, BookCreate, BookInDB, UpdateBookRequest
from models.core import PyObjectId
from pymongo.cursor import Cursor
from pymongo.database import Database
from repositories.base import BaseRepository

COLLECTION_NAME = BOOK_COLLECTION


class BookRepository(BaseRepository):
    def __init__(self, db: Database) -> None:
        super().__init__(db)

    async def find_many(self, *, limit: None | int, offset: int = 0) -> list[BookInDB]:
        result_iter: Cursor = super().find_many(
            collection_name=COLLECTION_NAME,
            offset=offset,
            limit=limit,
        )
        return [BookInDB(**result) for result in result_iter]

    async def find_one_filter_by_id(self, *, _id: PyObjectId) -> BookInDB | None:
        result: dict | None = super().find_one_filter_by_id(
            collection_name=COLLECTION_NAME,
            _id=_id,
        )
        return BookInDB(**result) if result else None

    async def create_one(
        self,
        *,
        book: BookCreate,
    ) -> PyObjectId:
        created_id: PyObjectId = super().insert_one(
            collection_name=COLLECTION_NAME,
            insert_dict=book.model_dump(),
        )
        return created_id

    async def update_one_filter_by_id(
        self,
        *,
        book: UpdateBookRequest,
        _id: PyObjectId,
    ) -> None:
        update_dict: dict = super().get_update_dict(model=book)
        super().update_one_filter_by_id(
            collection_name=COLLECTION_NAME, _id=_id, update_dict=update_dict
        )

    async def delete_one_filter_by_id(
        self,
        *,
        _id: PyObjectId,
    ) -> None:
        super().delete_one_filter_by_id(collection_name=COLLECTION_NAME, _id=_id)
