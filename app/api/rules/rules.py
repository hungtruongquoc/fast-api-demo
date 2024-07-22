from fastapi import APIRouter, Depends, HTTPException

from app.api.dependencies.api_key_validator import api_key_validator
from app.core.dependencies.firestore_service_injector import get_firestore_service
from app.core.services.firestore_service import FirestoreService

router = APIRouter()


@router.get("/", dependencies=[Depends(api_key_validator)])
async def get_packages(service: FirestoreService = Depends(get_firestore_service)):
    try:
        documents = service.get_scheduling_rules()
        return {"data": [doc.to_dict() for doc in documents if doc.exists]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
