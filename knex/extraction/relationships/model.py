from typing import Optional, List
from enum import Enum
from langchain_core.pydantic_v1 import BaseModel, Field

class Relationship(BaseModel):
    """
    Information about relationship between two persons.
    Does not concern parent-child relations.
    """

    person1_name: Optional[str] = Field(default=None, description="the first person of the relationship (in case of mentorship, the mentor)")
    person2_name: Optional[str] = Field(default=None, description="the second person of the relationship")
    date_begin: Optional[str] = Field(default=None, description="the relationship start date")
    date_end: Optional[str] = Field(default=None, description="the relationship end date")
    relationship_type: Optional[str] = Field(default=None, description="exclusively one of: romantic, marriage, friendship, mentorship, colleagues")


class Relationships(BaseModel):
    """List of relationships mentioned in the context"""

    relationships: List[Relationship] = Field(default=[], description="list of all relationships mentioned in the text")



def get_assertions(relationships: Relationships) -> List[str]:
    """List all assertions from the extracted Occupation"""

    assertions = []
    for rlt in relationships.relationships:
        p1_name = rlt.person1_name or 'Someone'
        p2_name = rlt.person2_name or 'Someone'

        if rlt.person1_name or rlt.person2_name:
            assertions.append(f"{p1_name} and {p2_name} had a relationship.")
        if rlt.date_begin:
            assertions.append(f"{p1_name} and {p2_name} relationship started in {rlt.date_begin}.")
        if rlt.date_end:
            assertions.append(f"{p1_name} and {p2_name} relationship ended in {rlt.date_end}.")
        if rlt.relationship_type:
            assertions.append(f"{p1_name} and {p2_name} relationship was {rlt.relationship_type}.")

    return assertions