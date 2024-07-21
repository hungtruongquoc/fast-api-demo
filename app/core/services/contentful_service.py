from typing import List, Dict

from app.core.dao.contentful_dao import ContentfulDAO
from app.core.dao.contentful_graphql_dao import ContentfulGraphQLDAO
import pandas as pd

from app.core.models.appointment import Appointment
from app.core.models.service_package import ServicePackage


class ContentfulService:
    def __init__(self, dao: ContentfulDAO, graphql_dao: ContentfulGraphQLDAO):
        self.dao = dao
        self.graphql_dao = graphql_dao

    def create_appointment(self, appointment) -> Appointment:
        return self.dao.create_appointment(appointment)

    def get_appointments(self) -> List[Appointment]:
        return self.dao.get_appointments()

    def get_packages(self) -> List[ServicePackage]:
        return self.dao.get_packages()

    def get_appointments_with_package(self) -> List[Dict]:
        return self.graphql_dao.get_package_appointments()

    def get_appointment_stats_by_month(self) -> Dict[str, List[Appointment]]:
        appointments = self.graphql_dao.get_appointments()

        # Convert appointments to DataFrame
        df = pd.DataFrame(appointments)
        df['timestampUtc'] = pd.to_datetime(df['timestampUtc'])

        # Extract month and year for aggregation
        df['month_year'] = df['timestampUtc'].dt.to_period('M')

        # Group appointments by month
        grouped = df.groupby('month_year').apply(lambda x: x.to_dict(orient='records')).to_dict()

        # Format the output
        grouped_appointments = {}
        for month, items in grouped.items():
            grouped_appointments[str(month)] = [
                Appointment(
                    id=item['id'],
                    timestamp=item['timestampUtc'].isoformat(),
                    first_name=item['firstName'],
                    last_name=item['lastName']
                ) for item in items
            ]

        return grouped_appointments
