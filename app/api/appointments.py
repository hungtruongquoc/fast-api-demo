from typing import Union

from fastapi import APIRouter

router = APIRouter()


@router.post("/")
async def create_appointments():
    return {"item_id": "created"}
