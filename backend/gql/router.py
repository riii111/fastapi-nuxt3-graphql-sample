import strawberry

from .resolvers.books import (
    create_book,
    delete_book,
    get_book_by_id,
    get_books,
    update_book,
)
from gql.types.books import BookViewType, ListBookResponseType


# Queryのルーティング
@strawberry.type
class Query:
    books: ListBookResponseType = strawberry.field(resolver=get_books)
    book_by_id: BookViewType = strawberry.field(resolver=get_book_by_id)


# Mutationのルーティング
@strawberry.type
class Mutation:
    create_book: BookViewType = strawberry.mutation(resolver=create_book)
    update_book: BookViewType = strawberry.mutation(resolver=update_book)
    delete_book: bool = strawberry.mutation(resolver=delete_book)
