from fastapi import APIRouter, Depends, HTTPException

from app.core.dependencies.contentful_service_injector import get_contentful_service
from app.core.models.appointment import Appointment
from app.core.services.contentful_service import ContentfulService

router = APIRouter()


@router.post("/")
async def create_appointments(appointment: Appointment,
                              service: ContentfulService = Depends(get_contentful_service)):
    try:
        entry = service.create_appointment(appointment)
        return {"entry": entry}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/")
async def get_appointments(service: ContentfulService = Depends(get_contentful_service)):
    try:
        entries = service.get_appointments()
        return {"appointments": entries}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
