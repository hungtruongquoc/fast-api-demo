from fastapi import Depends

from app.core.dao.contentful_dao import ContentfulDAO
from app.core.dependencies.contentful_dao_injector import get_contentful_dao
from app.core.dependencies.contentful_graphql_dao_injector import get_contentful_graphql_dao
from app.core.services.contentful_service import ContentfulService


def get_contentful_service(dao: ContentfulDAO = Depends(get_contentful_dao),
                           graphql_dao=Depends(get_contentful_graphql_dao)) -> ContentfulService:
    return ContentfulService(dao, graphql_dao)
