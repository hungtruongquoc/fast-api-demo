from app.core.dao.contentful_dao import ContentfulDAO
from app.core.dao.contentful_graphql_dao import ContentfulGraphQLDAO


class ContentfulService:
    def __init__(self, dao: ContentfulDAO, graphql_dao: ContentfulGraphQLDAO):
        self.dao = dao
        self.graphql_dao = graphql_dao

    def create_appointment(self, appointment):
        return self.dao.create_appointment(appointment)

    def get_appointments(self):
        return self.dao.get_appointments()

    def get_packages(self):
        return self.dao.get_packages()

    def get_appoints_with_package(self):
        return self.graphql_dao.get_package_appointments()