from fastapi import APIRouter
from app.api import index, items, appointments, packages
from app.api.app_api_router import AppAPIRouter  # Assuming the CustomAPIRouter is defined here

# Replace APIRouter with CustomAPIRouter
router = AppAPIRouter()
router.include_router(index.router, prefix="", tags=["index"])
router.include_router(items.router, prefix="/items", tags=["items"])
router.include_router(appointments.router, prefix="/appointments", tags=["appointments"])
router.include_router(packages.router, prefix="/packages", tags=["packages"])