from pydantic import BaseModel
from datetime import datetime


class Appointment(BaseModel):
    id: str
    first_name: str
    last_name: str
    timestamp: datetime
