from models.book import BOOK_COLLECTION, BookCreate, BookInDB, UpdateBookRequest
from models.core import PyObjectId
from db.session import get_db
from pymongo.cursor import Cursor
from pymongo.database import Database

COLLECTION_NAME = BOOK_COLLECTION


class BookRepository:
    def __init__(self, db: Database) -> None:
        self.db: Database = get_db()
        self.collection = self.db["documents"]

    async def find_many(
        self,
        *,
        limit: int | None = None,
        offset: int = 0,
        filter_: dict = {},
        sorts: list[tuple[str, int]] = [("created_at", 1)],
    ) -> list[BookInDB]:
        cursor: Cursor = self.collection.find(filter=filter_, sort=sorts).skip(offset)
        if limit is not None and limit > 0:
            cursor = cursor.limit(limit)
        return [BookInDB(**book) for book in cursor]

    async def find_one(self, *, filter_: dict) -> BookInDB | None:
        book = self.collection.find_one(filter_)
        return BookInDB(**book) if book else None

    async def insert_one(self, *, book: BookCreate) -> BookInDB:
        result = self.collection.insert_one(book.model_dump())
        created_book = await self.find_one(filter_={"_id": result.inserted_id})
        if not created_book:
            raise InternalException("ドキュメントの作成に失敗しました")
        return created_book

    async def update_one(self, *, filter_: dict, update: UpdateBookRequest) -> BookInDB:
        result = self.collection.update_one(filter_, {"$set": update.model_dump()})
        if result.modified_count == 0:
            raise InternalException("ドキュメントの更新に失敗しました")
        updated_book = await self.find_one(filter_=filter_)
        if not updated_book:
            raise InternalException("更新後のドキュメントの取得に失敗しました")
        return updated_book

    async def delete_one(
        self,
        *,
        _id: PyObjectId,
    ) -> None:
        result = self.collection.delete_one({"_id": _id})
        if result.deleted_count == 0:
            raise InternalException("ドキュメントの削除に失敗しました")
