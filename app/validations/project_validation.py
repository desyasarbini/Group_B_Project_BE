# from pydantic import BaseModel, field_validator
# from datetime import datetime

# class ProjectCreate(BaseModel):
#     project_image: str
#     project_name: str
#     description: str
#     target_amount: float
#     end_date: str

#     @field_validator('project_image')
#     def project_image_must_be_url(cls, v):
#         if not v:
#             raise ValueError('Project image URL must be provided')
#         return v

#     @field_validator('project_name')
#     def project_name_must_be_provided(cls, v):
#         if not v:
#             raise ValueError('Project name must be provided')
#         return v

#     @field_validator('description')
#     def description_must_be_provided(cls, v):
#         if not v:
#             raise ValueError('Description must be provided')
#         return v

#     @field_validator('target_amount')
#     def target_amount_must_be_positive(cls, v):
#         if v <= 0:
#             raise ValueError('Target amount must be a positive number')
#         return v
    
#     @field_validator('end_date')
#     def end_date_format_check(cls, v):
#         try:
#             datetime.strptime(v, '%Y-%m-%d')
#         except ValueError:
#             raise ValueError('End date must be in the format YYYY-MM-DD')
#         return v

# class ProjectUpdate(BaseModel):
#     project_name: str = None
#     description: str = None
#     end_date: str = None

#     @field_validator('end_date')
#     def end_date_format_check(cls, v):
#         if v is not None:
#             try:
#                 datetime.strptime(v, '%Y-%m-%d')
#             except ValueError:
#                 raise ValueError('End date must be in the format YYYY-MM-DD')
#         return v