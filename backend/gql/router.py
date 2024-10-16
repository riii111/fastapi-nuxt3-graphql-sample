import strawberry
from strawberry.fastapi import GraphQLRouter
from .resolvers import get_books
from .types import BookType
from .context import get_context


@strawberry.type
class Query:
    books: list[BookType] = strawberry.field(resolver=get_books)


schema = strawberry.Schema(query=Query)  # , mutation=Mutation)
graphql_app = GraphQLRouter(schema, context_getter=get_context)
