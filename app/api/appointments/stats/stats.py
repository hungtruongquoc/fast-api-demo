from fastapi import APIRouter, Depends
from typing import Dict, List

from app.core.dependencies.contentful_service_injector import get_contentful_service
from app.core.models.appointment import Appointment
from app.core.services.contentful_service import ContentfulService

# Define the stats sub-router
stats_router = APIRouter()


@stats_router.get("/by-month", response_model=Dict[str, List[Appointment]])
async def get_appointment_stats_by_month(service: ContentfulService = Depends(get_contentful_service)):
    return service.get_appointment_stats_by_month()
