from fastapi import APIRouter
from app.api import index, items, appointments, packages
from app.api.appointments.appointments import router as appointments_router
from app.api.packages.packages import router as package_router
from app.api.app_api_router import AppAPIRouter  # Assuming the CustomAPIRouter is defined here
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

# Replace APIRouter with CustomAPIRouter
router = AppAPIRouter()
router.include_router(index.router, prefix="", tags=["index"])
router.include_router(items.router, prefix="/items", tags=["items"])
router.include_router(appointments_router, prefix="/appointments", tags=["appointments"])
router.include_router(package_router, prefix="/packages", tags=["packages"])
