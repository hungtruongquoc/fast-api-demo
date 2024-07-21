from functools import wraps
from typing import Callable

from fastapi import HTTPException, Request

from app.core.config import settings

valid_api_keys = [settings.GROOMING_API_KEY, settings.ADMIN_API_KEY]


def api_key_required(func: Callable):
    @wraps(func)
    async def wrapper(*args, request: Request, **kwargs):
        api_key = request.query_params.get("customer")
        if valid_api_keys.index(api_key) == -1:
            raise HTTPException(status_code=403, detail="Access forbidden: Invalid API key")
        return await func(*args, **kwargs)

    return wrapper
