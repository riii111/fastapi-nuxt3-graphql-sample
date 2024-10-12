from config import app_config
from fastapi import APIRouter
from functions.batch import BatchProcessor
from functions.exceptions import RouteErrorHandler
from models.batch import BatchView, CreateBatchRequest
from starlette.status import HTTP_200_OK

router = APIRouter(route_class=RouteErrorHandler)


@router.post(
    "/",
    response_model=BatchView,
    description="バッチ処理",
    response_description="バッチ処理の結果",
    status_code=HTTP_200_OK,
)
async def post_batch(batch: CreateBatchRequest) -> BatchView:
    async with BatchProcessor(host=app_config.MY_HOST) as batch_processor:
        responses = await batch_processor.process(batch_requests=batch.requests)
    return BatchView(responses=responses)
