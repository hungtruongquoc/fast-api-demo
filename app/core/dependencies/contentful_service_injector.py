from fastapi import Depends
from app.core.dependencies.contentful_clients import get_contentful_clients
from app.core.services.contentful_service import ContentfulService


def get_contentful_service(clients: dict = Depends(get_contentful_clients)) -> ContentfulService:
    return ContentfulService(clients["cda_client"], clients["cma_client"])
