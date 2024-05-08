from pydantic import BaseModel, field_validator
from datetime import datetime

class DonationCreate(BaseModel):
    project_id: int
    email: str
    phone_number: str
    amount: float

    @field_validator('project_id')
    def project_id_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('Project ID must be a positive integer')
        return v

    @field_validator('email')
    def email_must_be_valid(cls, v):
        if '@' not in v or '.' not in v:
            raise ValueError('Invalid email format')
        return v

    @field_validator('phone_number')
    def phone_number_must_be_valid(cls, v):
        if len(v) < 8:
            raise ValueError('Invalid phone number format')
        return v

    @field_validator('amount')
    def amount_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('Amount must be a positive number')
        return v