from pydantic import BaseModel
from datetime import datetime


class Appointment(BaseModel):
    first_name: str
    last_name: str
    timestamp: datetime
