from typing import List
from strawberry.types import Info
from .types import BookType
from .context import GraphQLContext


async def get_books(info: Info[GraphQLContext, None]) -> List[BookType]:
    books = await info.context.book_usecase.get_all_books()
    return [BookType(**book.model_dump(exclude={"secret"})) for book in books]
