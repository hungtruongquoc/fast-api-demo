from fastapi import FastAPI, Request
from starlette.responses import JSONResponse
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.middleware import SlowAPIMiddleware
from slowapi.errors import RateLimitExceeded

from app.api.routes import router as api_router
from app.core.config import settings
from app.middlewares.api_key_authentication import ApiKeyAuthenticationMiddleware

# Initialize the rate limiter
limiter = Limiter(key_func=get_remote_address, default_limits=["5/minute"])

app = FastAPI(title=settings.PROJECT_NAME)

app.state.limiter = limiter

# Register the rate limit exceeded handler
@app.exception_handler(RateLimitExceeded)
async def rate_limit_exceeded_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={"detail": "Rate limit exceeded. Please try again later."},
    )


# Add SlowAPI middleware to apply rate limiting globally
app.add_middleware(SlowAPIMiddleware)
app.add_middleware(ApiKeyAuthenticationMiddleware)

app.include_router(api_router, prefix=settings.API_V1_STR)
