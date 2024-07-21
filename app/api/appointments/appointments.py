from typing import Dict, List

from fastapi import APIRouter, Depends, HTTPException
from pydantic import ValidationError
from fastapi.encoders import jsonable_encoder
from app.api.appointments.stats.stats import stats_router
from app.core.dependencies.contentful_service_injector import get_contentful_service
from app.core.models.appointment import Appointment
from app.core.services.contentful_service import ContentfulService

router = APIRouter()


@router.post("/", response_model=Appointment)
async def create_appointments(appointment: Appointment,
                              service: ContentfulService = Depends(get_contentful_service)):
    try:
        entry = service.create_appointment(appointment)
        return {"entry": entry}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/", response_model=List[Dict])
async def get_appointments(service: ContentfulService = Depends(get_contentful_service)):
    try:
        entries = service.get_appointments_with_package()
        return {"appointments": entries}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Include the stats sub-router under the /stats prefix
router.include_router(stats_router, prefix="/stats")
