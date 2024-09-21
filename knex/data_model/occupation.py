from typing import Optional
from langchain_core.pydantic_v1 import BaseModel, Field


class Occupation(BaseModel):

    name: Optional[str] = Field(default=None, description="the occupation name (eg military, carpenter, counselor, deputy)")
    place: Optional[str] = Field(default=None, description="the occupation place")
    date_begin: Optional[str] = Field(default=None, description="the occupation begin date (format: yyyy.mm.dd)")
    date_end: Optional[str] = Field(default=None, description="the occupation end date (format: yyyy.mm.dd)")
    company: Optional[str] = Field(default=None, description="the occupation company or organisation name (eg Nestle, French army, Swiss state, ...)")
    has_social_role: bool = Field(default=False, description="has the occupation a social role (eg state deputy, municipal counselor, ...)")
    is_formation: bool = Field(default=False, description="is the occupation a formation (apprentice, school, ...)")