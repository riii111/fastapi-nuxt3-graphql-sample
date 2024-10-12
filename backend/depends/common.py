from config import app_config
from fastapi import Query
from functions.exceptions import InvalidArgumentException
from pydantic import BaseModel


class ListQuery(BaseModel):
    limit: int
    offset: int


async def list_query(
    limit: int = Query(100, description="取得上限"),
    offset: int = Query(0, description="取得開始位置"),
):
    if limit > app_config.MAX_LIST_LIMIT:
        raise InvalidArgumentException(
            f"limit は {app_config.MAX_LIST_LIMIT}以下に設定してください。"
        )
    return ListQuery(limit=limit, offset=offset)
