from typing import List

from fastapi import APIRouter, Depends, HTTPException

from app.core.dependencies.contentful_service_injector import get_contentful_service
from app.core.models.service_package import ServicePackage
from app.core.services.contentful_service import ContentfulService
from app.api.packages.stats.stats import stats_router

router = APIRouter()


@router.get("/")
async def get_packages(service: ContentfulService = Depends(get_contentful_service)):
    try:
        entries = service.get_packages()
        return {"packages": entries}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Include the stats sub-router under the /stats prefix
router.include_router(stats_router, prefix="/stats")
