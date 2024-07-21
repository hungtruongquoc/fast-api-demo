from fastapi import APIRouter, Depends
from typing import Dict, List
import pandas as pd

from app.core.dependencies.contentful_service_injector import get_contentful_service
from app.core.services.contentful_service import ContentfulService

# Define the stats sub-router
stats_router = APIRouter()


@stats_router.get("/count-by-month", response_model=Dict[str, int])
async def get_package_count_by_months(service: ContentfulService = Depends(get_contentful_service)):
    return service.get_count_stats_by_package_and_month()