from fastapi import APIRouter
from app.api import index, items

router = APIRouter()
router.include_router(index.router, prefix="/", tags=["index"])
router.include_router(items.router, prefix="/items", tags=["items"])