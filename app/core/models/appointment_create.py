from pydantic import Field, field_validator
from app.core.models.appointment_base import AppointmentBase


class AppointmentCreate(AppointmentBase):
    package_id: str = Field(..., description="package_id is required")

    @field_validator('package_id')
    def not_empty(cls, value, field):
        if not value.strip():
            raise ValueError(f'{field.name} cannot be empty')
        return value
