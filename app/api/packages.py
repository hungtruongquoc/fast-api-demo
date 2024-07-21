from fastapi import APIRouter, Depends, HTTPException

from app.core.dependencies.contentful_service_injector import get_contentful_service
from app.core.services.contentful_service import ContentfulService

router = APIRouter()


@router.get("/")
async def get_appointments(service: ContentfulService = Depends(get_contentful_service)):
    try:
        entries = service.get_packages()
        return {"packages": entries}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
