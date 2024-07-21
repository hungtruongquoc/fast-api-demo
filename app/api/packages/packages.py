from fastapi import APIRouter, Depends, HTTPException

from app.api.dependencies.api_key_validator import api_key_validator
from app.api.packages.stats.stats import stats_router
from app.core.dependencies.contentful_service_injector import get_contentful_service
from app.core.services.contentful_service import ContentfulService

router = APIRouter()


@router.get("/", dependencies=[Depends(api_key_validator)])
async def get_packages(service: ContentfulService = Depends(get_contentful_service)):
    try:
        entries = service.get_packages()
        return {"packages": entries}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Include the stats sub-router under the /stats prefix
router.include_router(stats_router, prefix="/stats")
