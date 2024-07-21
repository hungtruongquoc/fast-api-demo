from typing import Dict, List

from fastapi import APIRouter, Depends

from app.core.dependencies.contentful_service_injector import get_contentful_service
from app.core.services.contentful_service import ContentfulService

# Define the stats sub-router
stats_router = APIRouter()


@stats_router.get("/by-month", response_model=Dict[str, List[Dict]])
async def get_appointment_stats_by_month(service: ContentfulService = Depends(get_contentful_service)):
    return service.get_appointment_stats_by_month()


@stats_router.get("/count-by-month", response_model=Dict[str, int])
async def get_appointment_stats_by_month(service: ContentfulService = Depends(get_contentful_service)):
    return service.get_appointment_count_stats_by_month()
