from fastapi import APIRouter, Depends, HTTPException
from app.core.dependencies.contentful_clients import get_contentful_clients

router = APIRouter()


@router.post("/")
async def create_appointments():
    return {"item_id": "created"}

@router.get("/")
async def get_appointments(clients: dict = Depends(get_contentful_clients)):
    cda_client = clients["cda_client"]
    try:
        entries = cda_client.entries({'content_type': 'appointments'})
        return {"appointments": [entry.fields() for entry in entries]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
