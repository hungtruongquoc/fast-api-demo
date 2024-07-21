from fastapi import APIRouter, Depends, HTTPException

from app.core.config import settings
from app.core.dependencies.contentful_clients import get_contentful_clients
from app.core.models.appointment import Appointment

router = APIRouter()


@router.post("/")
async def create_appointments(appointment: Appointment, clients: dict = Depends(get_contentful_clients)):
    try:
        cma_client = clients["cma_client"]
        space = cma_client.spaces().find(settings.CONTENTFUL_SPACE_ID)
        environment = space.environments().find('master')
        entry = environment.entries().create(None, {
            'content_type_id': 'appointments',
            'fields': {
                'firstName': {'en-US': appointment.first_name},
                'lastName': {'en-US': appointment.last_name},
            }
        })
        entry.publish()
        return {"entry": entry.to_json()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/")
async def get_appointments(clients: dict = Depends(get_contentful_clients)):
    cda_client = clients["cda_client"]
    try:
        entries = cda_client.entries({'content_type': 'appointments'})
        return {"appointments": [entry.fields() for entry in entries]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
