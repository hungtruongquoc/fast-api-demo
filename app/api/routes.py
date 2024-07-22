from app.api import index, items
from app.api.app_api_router import AppAPIRouter  # Assuming the CustomAPIRouter is defined here
from app.api.appointments.appointments import router as appointments_router
from app.api.packages.packages import router as package_router
from app.api.rules.rules import router as rules_router

# Replace APIRouter with CustomAPIRouter
router = AppAPIRouter()
router.include_router(index.router, prefix="", tags=["index"])
router.include_router(items.router, prefix="/items", tags=["items"])
router.include_router(appointments_router, prefix="/appointments", tags=["appointments"])
router.include_router(package_router, prefix="/packages", tags=["packages"])
router.include_router(rules_router, prefix="/rules", tags=["rules"])
