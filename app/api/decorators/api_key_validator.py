from functools import wraps
from typing import Callable, Any
from fastapi import HTTPException, Request, Depends

from app.core.config import settings

valid_api_keys = [settings.GROOMING_API_KEY, settings.ADMIN_API_KEY]


def api_key_required(func: Callable[..., Any]):
    @wraps(func)
    async def wrapper(request: Request = Depends(), *args, **kwargs):
        api_key = request.query_params.get("customer")
        if api_key not in valid_api_keys:
            raise HTTPException(status_code=403, detail="Access forbidden: Invalid API key")
        return await func(request, *args, **kwargs)

    return wrapper
