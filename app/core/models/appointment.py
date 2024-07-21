from pydantic import BaseModel


class Appointment(BaseModel):
    first_name: str
    last_name: str
