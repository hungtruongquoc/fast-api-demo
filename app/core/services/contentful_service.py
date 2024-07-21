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

    def get_appointment_count_stats_by_month(self) -> Dict[str, int]:
        appointments = self.graphql_dao.get_appointments()

        # Convert appointments to DataFrame
        df = pd.DataFrame(appointments)
        df['timestampUtc'] = pd.to_datetime(df['timestampUtc'])

        # Extract month and year for aggregation
        df['month_year'] = df['timestampUtc'].dt.to_period('M')

        # Group appointments by month and count them
        grouped = df.groupby('month_year').size().to_dict()

        # Convert PeriodIndex to string keys for the dictionary
        grouped_appointments = {str(month): count for month, count in grouped.items()}

        return grouped_appointments

    def get_count_stats_by_package_and_month(self) -> List[Dict[str, int]]:
        data = self.get_appointments_with_package()

        # Convert data to DataFrame and normalize nested fields
        df = pd.json_normalize(data)

        # Ensure correct field names based on the structure
        df['appointment.timestampUtc'] = pd.to_datetime(df['appointment.timestampUtc'])

        # Extract month and year for aggregation
        df['month_year'] = df['appointment.timestampUtc'].dt.to_period('M').astype(str)

        # Group by month and package name and count occurrences
        grouped = df.groupby(['month_year', 'packageName.name']).size().unstack(fill_value=0).reset_index()

        # Debug: print the intermediate grouped DataFrame
        print("Grouped DataFrame:\n", grouped)

        # Convert grouped DataFrame to list of dictionaries
        package_stats_by_month = []
        for index, row in grouped.iterrows():
            stats = {'month': str(row['month_year'])}
            for package_name in grouped.columns[1:]:
                stats[package_name] = int(row[package_name])  # Ensure values are integers
            package_stats_by_month.append(stats)

        # Debug: print the final stats list
        print("Package Stats by Month:\n", package_stats_by_month)

        return package_stats_by_month

