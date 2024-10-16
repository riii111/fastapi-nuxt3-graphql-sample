from models.book import BookCreate, BookView, UpdateBookRequest
from models.core import PyObjectId
from repositories.book import BookRepository


class BookUseCase:
    def __init__(self, book_repo: BookRepository):
        self.book_repo = book_repo

    async def get_all_books(self) -> list[BookView]:
        return await self.book_repo.find_many(limit=None)

    async def get_book_by_id(self, book_id: str) -> BookView:
        result = await self.book_repo.find_one_filter_by_id(_id=PyObjectId(book_id))
        if result is None:
            raise Exception(f"ID {book_id} の本が見つかりません")
        return result

    async def create_book(self, book_data: BookCreate) -> BookView:
        created_id = await self.book_repo.create_one(book=book_data)
        return await self.get_book_by_id(str(created_id))

    async def update_book(self, book_id: str, book_data: UpdateBookRequest) -> BookView:
        await self.book_repo.update_one_filter_by_id(
            book=book_data, _id=PyObjectId(book_id)
        )
        return await self.get_book_by_id(book_id)

    async def delete_book(self, book_id: str) -> bool:
        await self.book_repo.delete_one_filter_by_id(_id=PyObjectId(book_id))
        return True
