from fastapi import HTTPException, Request, Depends
from app.core.config import settings

valid_api_keys = [settings.GROOMING_API_KEY, settings.ADMIN_API_KEY]


async def api_key_validator(request: Request):
    api_key = request.query_params.get("customer")
    if api_key not in valid_api_keys:
        raise HTTPException(status_code=403, detail="Access forbidden: Invalid API key")
