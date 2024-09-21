from typing import Optional
from langchain_core.pydantic_v1 import BaseModel, Field


class Relationship(BaseModel):

    partner_name: Optional[str] = Field(default=None, description="the other person of the relationship")
    date_begin: Optional[str] = Field(default=None, description="the relationship start date (format: yyyy.mm.dd)")
    date_end: Optional[str] = Field(default=None, description="the relationship end date (format: yyyy.mm.dd)")
    is_marriage: Optional[bool] = Field(default=False, description="Is the relation a marriage?")
    is_friendship: Optional[bool] = Field(default=False, description="Is the relation a friendship?")
    is_mentorship: Optional[bool] = Field(default=False, description="Is the relation a mentorship?")
