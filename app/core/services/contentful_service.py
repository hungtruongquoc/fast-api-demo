from app.core.dao.contentful_dao import ContentfulDAO


class ContentfulService:
    def __init__(self, dao: ContentfulDAO):
        self.dao = dao

    def create_appointment(self, appointment):
        return self.dao.create_appointment(appointment)

    def get_appointments(self):
        return self.dao.get_appointments()
