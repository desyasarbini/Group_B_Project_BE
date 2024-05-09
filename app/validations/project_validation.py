from pydantic import BaseModel, field_validator
from datetime import datetime

class ProjectCreate(BaseModel):
    project_image: str
    project_name: str
    description: str
    target_amount: float

    @field_validator('project_image')
    def project_image_must_be_url(cls, v):
        if not v:
            raise ValueError('Project image URL must be provided')
        return v

    @field_validator('project_name')
    def project_name_must_be_provided(cls, v):
        if not v:
            raise ValueError('Project name must be provided')
        return v

    @field_validator('description')
    def description_must_be_provided(cls, v):
        if not v:
            raise ValueError('Description must be provided')
        return v

    @field_validator('target_amount')
    def target_amount_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('Target amount must be a positive number')
        return v

class ProjectUpdate(BaseModel):
    project_name: str = None
    description: str = None