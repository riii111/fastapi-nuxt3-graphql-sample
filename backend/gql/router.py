import strawberry

from .resolvers import get_books, get_book_by_id
from .types import BookViewType


# Queryのルーティング
@strawberry.type
class Query:
    books: list[BookViewType] = strawberry.field(resolver=get_books)
    book_by_id: BookViewType = strawberry.field(resolver=get_book_by_id)
