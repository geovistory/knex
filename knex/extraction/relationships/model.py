from typing import Optional, List
from langchain_core.pydantic_v1 import BaseModel, Field


class Relationship(BaseModel):
    """
    Information about relationship between two persons.
    Does not concern parent-child relations, but rather marriage, frienship, mentorship, ...
    """

    person1_name: Optional[str] = Field(default=None, description="the first person of the relationship (in case of mentorship, the mentor)")
    person2_name: Optional[str] = Field(default=None, description="the second person of the relationship")
    date_begin: Optional[str] = Field(default=None, description="the relationship start date (format: yyyy.mm.dd)")
    date_end: Optional[str] = Field(default=None, description="the relationship end date (format: yyyy.mm.dd)")
    is_marriage: Optional[bool] = Field(default=False, description="Is the relation a marriage?")
    is_friendship: Optional[bool] = Field(default=False, description="Is the relation a friendship?")
    is_mentorship: Optional[bool] = Field(default=False, description="Is the relation a mentorship?")


class Relationships(BaseModel):
    """
    List of all relationships mentioned in the text.
    """

    relationships: List[Relationship] = Field(default=None, description="the list of relationships")



def get_assertions(relationships: Relationships) -> List[str]:
    """List all assertions from the extracted Occupation"""

    assertions = []

    for rlt in relationships.relationships:
        if rlt.person1_name and rlt.person2_name:
            assertions.append(f"{rlt.person1_name} and {rlt.person2_name} had a relationship.")
        if rlt.person1_name and rlt.person2_name and rlt.date_begin:
            assertions.append(f"{rlt.person1_name} and {rlt.person2_name} relationship started in {rlt.date_begin}.")
        if rlt.person1_name and rlt.person2_name and rlt.date_end:
            assertions.append(f"{rlt.person1_name} and {rlt.person2_name} relationship ended in {rlt.date_end}.")
        if rlt.is_marriage:
            assertions.append(f"{rlt.person1_name or 'Someone'} and {rlt.person2_name or 'someone'} were married.")
        if rlt.is_friendship:
            assertions.append(f"{rlt.person1_name} and {rlt.person2_name} were friends.")
        if rlt.is_mentorship:
            assertions.append(f"{rlt.person1_name} was the mentor of {rlt.person2_name}.")

    return assertions