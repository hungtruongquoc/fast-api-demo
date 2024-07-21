from fastapi import Depends

from app.core.dao.contentful_dao import ContentfulDAO
from app.core.dependencies.contentful_clients import get_contentful_clients


def get_contentful_dao(clients: dict = Depends(get_contentful_clients)):
    return ContentfulDAO(clients["cda_client"], clients["cma_client"])