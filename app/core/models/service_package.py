from pydantic import BaseModel


class ServicePackage(BaseModel):
    name: str
