import strawberry
from models.core import PyObjectId
from strawberry.fastapi import GraphQLRouter

from .context import get_context
from .resolvers import get_books
from .types import BookViewType, PyObjectIdType


# Queryのルーティング
@strawberry.type
class Query:
    books: list[BookViewType] = strawberry.field(resolver=get_books)


# Schemaの初期化
schema = strawberry.federation.Schema(
    query=Query,
    enable_federation_2=True,
    scalar_overrides={PyObjectId: PyObjectIdType},
)

graphql_app = GraphQLRouter(schema, context_getter=get_context)
