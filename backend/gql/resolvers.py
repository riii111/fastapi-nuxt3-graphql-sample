from typing import List
from strawberry.types import Info
from .types import BookViewType
from .context import GraphQLContext


async def get_books(info: Info[GraphQLContext, None]) -> List[BookViewType]:
    books = await info.context.book_usecase.get_all_books()
    return [BookViewType(**book.model_dump(exclude={"secret"})) for book in books]
