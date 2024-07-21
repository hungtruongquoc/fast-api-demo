from fastapi import Depends

from app.core.dao.contentful_dao import ContentfulDAO
from app.core.dependencies.contentful_dao_injector import get_contentful_dao
from app.core.services.contentful_service import ContentfulService


def get_contentful_service(dao: ContentfulDAO = Depends(get_contentful_dao)) -> ContentfulService:
    return ContentfulService(dao)
