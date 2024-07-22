from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.middleware import SlowAPIMiddleware
from slowapi.errors import RateLimitExceeded
from fastapi.middleware.cors import CORSMiddleware

import logging

from app.api.routes import router as api_router
from app.core.config import settings
from app.middlewares.api_key_authentication import ApiKeyAuthenticationMiddleware

# Initialize the rate limiter
limiter = Limiter(key_func=get_remote_address, default_limits=["5/minute"])
# Configure the logger
logging.basicConfig(level=logging.INFO)

app = FastAPI(title=settings.PROJECT_NAME)

app.state.limiter = limiter


# Register the rate limit exceeded handler
@app.exception_handler(RateLimitExceeded)
async def rate_limit_exceeded_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={"detail": "Rate limit exceeded. Please try again later."},
    )


# Register the custom exception handler
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content=jsonable_encoder({"detail": exc.errors()})
    )


# Add SlowAPI middleware to apply rate limiting globally
app.add_middleware(SlowAPIMiddleware)
app.add_middleware(ApiKeyAuthenticationMiddleware)
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"],
                   allow_headers=["*"])

app.include_router(api_router, prefix=settings.API_V1_STR)
