from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response
from starlette.requests import Request
from datetime import datetime, timezone

from app.security.api_key_reader import ApiKeyReader


class ApiKeyAuthenticationMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):

        if not('/api/' in request.url.path):
            # Bypass API key check for paths not containing '/api/'
            return await call_next(request)

        reader = ApiKeyReader()

        # Read "my-key" from query string parameters
        customer_name = request.query_params.get("customer")

        if customer_name is None:
            return Response(content="customer is not provided.", status_code=403)

        expiration_timestamp = reader.get_expiration(customer_name)

        # Check if expiration_timestamp exists and has not exceeded
        if expiration_timestamp:
            if datetime.now(timezone.utc) < expiration_timestamp:
                # Proceed to the next middleware or endpoint
                response = await call_next(request)
                return response
            else:
                # Reject the request
                return Response(content="API key expired.", status_code=403)
        else:
            # Proceed to the next middleware or endpoint if no expiration timestamp
            response = await call_next(request)
            return response