from contentful import Client as ContentfulClient
from contentful_management import Client as ContentfulManagementClient
from app.core.config import settings
from app.core.models.appointment import Appointment


class ContentfulDAO:
    def __init__(self, cda_client: ContentfulClient, cma_client: ContentfulManagementClient):
        self.cda_client = cda_client
        self.cma_client = cma_client

    def create_appointment(self, appointment: Appointment):
        space = self.cma_client.spaces().find(settings.SPACE_ID)
        environment = space.environments().find('master')
        entry = environment.entries().create(None, {
            'content_type_id': 'appointments',
            'fields': {
                'firstName': {'en-US': appointment.first_name},
                'lastName': {'en-US': appointment.last_name},
                'timestampUtc': {'en-US': appointment.timestamp},
            }
        })
        entry.publish()
        return entry.to_json()

    def get_appointments(self):
        entries = self.cda_client.entries({'content_type': 'appointments'})
        return [entry.fields() for entry in entries]
