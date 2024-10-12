import asyncio

import aiohttp
from models.batch import HTTPRequest, HTTPResponse


class BatchProcessor:
    def __init__(self, host: str):
        self._host = host

    async def __aenter__(self):
        self._session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self._session.close()

    def _construct_url(self, relative_url: str) -> str:
        return f"{self._host}{relative_url}"

    async def _handle_request(self, request: HTTPRequest) -> HTTPResponse:
        request_url = self._construct_url(request.url)
        response = await self._session.request(
            method=request.method,
            url=request_url,
            headers=request.headers,
            json=request.body,
        )
        return HTTPResponse(
            id=request.id,
            status=response.status,
            headers=response.headers,
            body=await response.json(),
        )

    async def process(self, batch_requests: list[HTTPRequest]) -> list[HTTPResponse]:
        async with asyncio.TaskGroup() as tg:
            tasks = [
                tg.create_task(self._handle_request(req)) for req in batch_requests
            ]
        return [task.result() for task in tasks]
