from enum import Enum
from typing import Callable

from fastapi import HTTPException, Request, Response
from fastapi.logger import logger
from fastapi.routing import APIRoute


class RouteErrorHandler(APIRoute):
    """Custom APIRoute that handles application errors and exceptions"""

    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            try:
                return await original_route_handler(request)
            except HTTPException as ex:
                logger.exception(ex)
                raise ex
            except Exception as ex:
                logger.exception(ex)
                raise HTTPException(status_code=500, detail=str(ex))

        return custom_route_handler


class ErrorStatus(int, Enum):
    INVALID_ARGUMENT = 1
    FAILED_PRECONDITION = 2
    OUT_OF_RANGE = 3
    UNAUTHENTICATED = 4
    PERMISSION_DENIED = 5
    NOT_FOUND = 6
    ABORTED = 7
    ALREADY_EXISTS = 8
    RESOURCE_EXHAUSTED = 9
    CANCELLED = 10
    DATA_LOSS = 100
    INTERNAL = 101


class BaseException(Exception):
    def __init__(
        self,
        message: str,
        status_code: int,
        error_status: ErrorStatus = ErrorStatus.INTERNAL,
        raw_error: None | Exception = None,
    ):
        detail: dict = {
            "message": message,
            "error_status": error_status.name,
            "status_code": status_code,
            "raw_error": raw_error,
        }
        logger.error(detail)
        raise HTTPException(status_code=status_code, detail=detail)


class InvalidArgumentException(BaseException):
    """クライアントが無効な引数を指定。詳しくはエラーメッセージとエラーの詳細を確認させる。"""

    def __init__(self, message: str, raw_error: None | Exception = None):
        super().__init__(
            message=message,
            status_code=400,
            error_status=ErrorStatus.INVALID_ARGUMENT,
            raw_error=raw_error,
        )


class FailedPreconditionException(BaseException):
    """空でないディレクトリの削除など、現在のシステム状態ではリクエストを実行できない。"""

    def __init__(self, message: str, raw_error: None | Exception = None):
        super().__init__(
            message=message,
            status_code=400,
            error_status=ErrorStatus.FAILED_PRECONDITION,
            raw_error=raw_error,
        )


class OutOfRangeException(BaseException):
    """クライアントが無効な範囲を指定。"""

    def __init__(self, message: str, raw_error: None | Exception = None):
        super().__init__(
            message=message,
            status_code=400,
            error_status=ErrorStatus.OUT_OF_RANGE,
            raw_error=raw_error,
        )


class UnauthenticatedException(BaseException):
    """OAuthトークンがない、もしくは無効、期限切れのためにリクエストが認証されない。"""

    def __init__(self, message: str, raw_error: None | Exception = None):
        super().__init__(
            message=message,
            status_code=401,
            error_status=ErrorStatus.UNAUTHENTICATED,
            raw_error=raw_error,
        )


class PermissionDeniedException(BaseException):
    """クライアントに十分な権限がない。これは、OAuthトークンに正しいスコープが割り当てられていないか、クライアントに権限が付与されていない、またはAPIが有効になっていないことが原因で発生。"""

    def __init__(self, message: str, raw_error: None | Exception = None):
        super().__init__(
            message=message,
            status_code=403,
            error_status=ErrorStatus.PERMISSION_DENIED,
            raw_error=raw_error,
        )


class NotFoundException(BaseException):
    """指定されたリソースが見つからない。"""

    def __init__(self, message: str, raw_error: None | Exception = None):
        super().__init__(
            message=message,
            status_code=404,
            error_status=ErrorStatus.NOT_FOUND,
            raw_error=raw_error,
        )


class AbortedException(BaseException):
    """同時実行の競合（読み取り - 変更 - 書き込みの競合など）。"""

    def __init__(self, message: str, raw_error: None | Exception = None):
        super().__init__(
            message=message,
            status_code=409,
            error_status=ErrorStatus.ABORTED,
            raw_error=raw_error,
        )


class AlreadyExistsException(BaseException):
    """クライアントが作成しようとしたリソースがすでに存在。"""

    def __init__(self, message: str, raw_error: None | Exception = None):
        super().__init__(
            message=message,
            status_code=409,
            error_status=ErrorStatus.ALREADY_EXISTS,
            raw_error=raw_error,
        )


class ResourceExhaustedException(BaseException):
    """リソース割り当てが不足しているか、レート制限に達している。"""

    def __init__(self, message: str, raw_error: None | Exception = None):
        super().__init__(
            message=message,
            status_code=429,
            error_status=ErrorStatus.RESOURCE_EXHAUSTED,
            raw_error=raw_error,
        )


class CancelledException(BaseException):
    """リクエストはクライアントによってキャンセルされた。"""

    def __init__(self, message: str, raw_error: None | Exception = None):
        super().__init__(
            message=message,
            status_code=499,
            error_status=ErrorStatus.CANCELLED,
            raw_error=raw_error,
        )


class DataLossException(BaseException):
    """復元できないデータ損失またはデータ破損。"""

    def __init__(self, message: str, raw_error: None | Exception = None):
        super().__init__(
            message=message,
            status_code=500,
            error_status=ErrorStatus.DATA_LOSS,
            raw_error=raw_error,
        )


class InternalException(BaseException):
    """内部サーバーエラー。通常サーバーのバグ。"""

    def __init__(self, message: str, raw_error: None | Exception = None):
        super().__init__(
            message=message,
            status_code=500,
            error_status=ErrorStatus.INTERNAL,
            raw_error=raw_error,
        )
