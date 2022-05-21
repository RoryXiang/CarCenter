import uuid
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response
from conf import request_id_context


class LogTraceMiddleware(BaseHTTPMiddleware, RequestResponseEndpoint):
    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        request_id = str(uuid.uuid4())
        request_id_context.set(request_id)
        response = await call_next(request)
        response.headers['X-Request-Id'] = request_id
        request_id_context.set(None)
        return response