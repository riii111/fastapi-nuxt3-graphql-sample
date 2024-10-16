import strawberry

from .resolvers import get_books
from .types import BookViewType


# Queryのルーティング
@strawberry.type
class Query:
    books: list[BookViewType] = strawberry.field(resolver=get_books)
