import logging
from contentful import Client as ContentfulClient
from contentful_management import Client as ContentfulManagementClient
from app.core.config import settings
from app.core.models.appointment import Appointment
from uuid6 import uuid7

logger = logging.getLogger(__name__)


class ContentfulDAO:
    def __init__(self, cda_client: ContentfulClient, cma_client: ContentfulManagementClient):
        self.cda_client = cda_client
        self.cma_client = cma_client

    def create_appointment(self, appointment: Appointment, package_id: str):
        try:
            space = self.cma_client.spaces().find(settings.CONTENTFUL_SPACE_ID)
            environment = space.environments().find('master')
            appointment_id = str(uuid7())

            entry = environment.entries().create(None, {
                'content_type_id': 'appointments',
                'fields': {
                    'id': {'en-US': appointment_id},
                    'firstName': {'en-US': appointment.first_name},
                    'lastName': {'en-US': appointment.last_name},
                    'timestampUtc': {'en-US': appointment.timestamp.isoformat()},
                }
            })

            # Create the package appointment entry
            package_appointment_entry = environment.entries().create(None, {
                'content_type_id': 'appointmentPackage',
                'fields': {
                    'packageName': {'en-US': {'sys': {'type': 'Link', 'linkType': 'Entry', 'id': package_id}}},
                    'appointment': {
                        'en-US': {'sys': {'type': 'Link', 'linkType': 'Entry', 'id': entry.sys['id']}}},
                }
            })

            entry.publish()
            package_appointment_entry.publish()
            return entry.to_json()
        except Exception as e:
            logger.error(f"An error occurred: {e}")
            raise

    def get_appointments(self):
        entries = self.cda_client.entries({'content_type': 'appointments'})
        return list(map(lambda entry: {**entry.sys, **entry.fields}, entries))

    def get_packages(self):
        entries = self.cda_client.entries({'content_type': 'package'})
        return list(map(lambda entry: {**entry.sys, **entry.fields}, entries))
