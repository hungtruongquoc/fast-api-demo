from fastapi import APIRouter, Depends, HTTPException
import logging
from app.api.dependencies.api_key_validator import api_key_validator
from app.core.dependencies.contentful_service_injector import get_contentful_service
from app.core.services.contentful_service import ContentfulService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/", dependencies=[Depends(api_key_validator)])
async def get_packages(service: ContentfulService = Depends(get_contentful_service)):
    try:
        entries = service.get_packages()
        return {"packages": entries}
    except Exception as e:
        logger.error(f"An error in get packages endpoint: ", e)
        raise HTTPException(status_code=500, detail=str(e))
