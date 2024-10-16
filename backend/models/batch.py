from urllib.parse import ParseResult, urlparse

from config import app_config
from functions.exceptions import InvalidArgumentException
from functions.super_enum import SuperEnumMixIn
from pydantic import BaseModel, Field, field_validator


class HTTPVerbs(str, SuperEnumMixIn):
    GET = "GET"
    POST = "POST"
    DELETE = "DELETE"
    PATCH = "PATCH"
    PUT = "PUT"


class HTTPBase(BaseModel):
    id: int = Field(1, description="バッチ内の個々のレスポンスをリクエストに関連付けるためのID")
    headers: None | dict[str, str] = Field({}, description="ヘッダーのJSONオブジェクト")
    body: None | dict = Field({}, description="リクエストボディのJSONオブジェクト")


class HTTPRequest(HTTPBase):
    url: str = Field("/users/", description="リクエスト先のURL")
    method: HTTPVerbs = Field(HTTPVerbs.GET, description="HTTPメソッド")

    @field_validator("url")
    @classmethod  # type: ignore
    def validate_url(cls, val: str) -> str:
        val = val.strip()
        parse_result: ParseResult = urlparse(val)
        if parse_result.scheme:
            raise InvalidArgumentException(f"url: {val} にhttp://等のスキームは不要です。")
        if parse_result.hostname:
            raise InvalidArgumentException(f"url: {val} にホスト名は不要です。")
        if not val.startswith("/"):
            raise InvalidArgumentException("url は/から始めてください。")
        return val


class HTTPResponse(HTTPBase):
    status: int


class CreateBatchRequest(BaseModel):
    """Createメソッドのリクエスト"""

    requests: list[HTTPRequest] = Field(
        [HTTPRequest().model_dump()], description="リクエストのリスト"
    )

    @field_validator("requests")
    def validate_requests(cls, val: list[HTTPRequest]) -> list[HTTPRequest]:
        if len(val) > 20:
            raise InvalidArgumentException(
                f"一度にリクエスト可能な処理は{app_config.MAX_BATCH_REQUEST}個までです。"
            )
        if len(val) != len(set((request.id for request in val))):
            raise InvalidArgumentException("IDに重複がないようにしてください。")
        return val


class BatchView(BaseModel):
    responses: list[HTTPResponse]
