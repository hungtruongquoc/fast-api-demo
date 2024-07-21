import requests

from app.core.config import settings


class ContentfulGraphQLDAO:
    def __init__(self):
        self.space_id = settings.CONTENTFUL_SPACE_ID
        self.access_token = settings.CONTENTFUL_CDA_TOKEN
        self.endpoint = f'https://graphql.contentful.com/content/v1/spaces/{self.space_id}'
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.access_token}'
        }

    def query(self, query):
        response = requests.post(self.endpoint, headers=self.headers, json={'query': query})
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f'Query failed to run by returning code of {response.status_code}. {response.text}')

    def get_appointment_count(self):
        query = '''
                {
                  appointmentCollection {
                    total
                  }
                }
                '''
        data = self.query(query)
        return data['data']['appointmentCollection']['total']

    def get_package_appointments(self):
        query = '''
        {
          appointmentPackage {
            items {
              sys {
                id
              }
              package {
                sys {
                  id
                }
                name
                id
              }
              appointment {
                sys {
                  id
                }
                timestampUtc
                firstName
                lastName
                id
              }
            }
          }
        }
        '''
        data = self.query(query)
        return data['data']['appointmentPackage']['items']