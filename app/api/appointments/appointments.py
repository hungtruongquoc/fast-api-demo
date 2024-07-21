from typing import Dict, List

from fastapi import APIRouter, Depends, HTTPException
from app.api.appointments.stats.stats import stats_router
from app.core.dependencies.contentful_service_injector import get_contentful_service
from app.core.models.appointment import Appointment
from app.core.models.appointment_create import AppointmentCreate
from app.core.services.contentful_service import ContentfulService

router = APIRouter()


@router.post("/")
async def create_appointments(appointment: AppointmentCreate,
                              service: ContentfulService = Depends(get_contentful_service)):
    try:
        entry = service.create_appointment(appointment)
        return {"entry": entry}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/")
async def get_appointments(service: ContentfulService = Depends(get_contentful_service)):
    try:
        entries = service.get_appointments_with_package()
        return {"appointments": entries}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Include the stats sub-router under the /stats prefix
router.include_router(stats_router, prefix="/stats")
