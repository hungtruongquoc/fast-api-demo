from pydantic import BaseModel, Field, validator, field_validator
from datetime import datetime


class AppointmentBase(BaseModel):
    first_name: str = Field(..., description="First name is required")
    last_name: str = Field(..., description="Last name is required")
    timestamp: datetime

    @field_validator('timestamp')
    def timestamp_not_in_past(cls, value):
        if value < datetime.now():
            raise ValueError('Timestamp must not be in the past')
        return value

    @field_validator('first_name', 'last_name')
    def not_empty(cls, value, field):
        if not value.strip():
            raise ValueError(f'{field.name} cannot be empty')
        return value
