from contentful import Client as ContentfulClient
from contentful_management import Client as ContentfulManagementClient
from app.core.config import settings


def get_contentful_clients():
    cda_client = ContentfulClient(settings.CONTENTFUL_SPACE_ID, settings.CONTENTFUL_CDA_TOKEN)
    cma_client = ContentfulManagementClient(settings.CONTENTFUL_CMA_TOKEN)
    return {"cda_client": cda_client, "cma_client": cma_client}
