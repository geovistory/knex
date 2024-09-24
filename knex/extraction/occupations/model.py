from typing import Optional, List
from langchain_core.pydantic_v1 import BaseModel, Field


class Occupation(BaseModel):
    """
    Information from the text about an occupation.
    """

    # General information
    occupation_name: Optional[str] = Field(default=None, description="the occupation name (eg military, carpenter, counselor, deputy)")
    place: Optional[str] = Field(default=None, description="the occupation place")
    company: Optional[str] = Field(default=None, description="the occupation company or organisation name (eg Nestle, French army, Swiss state, ...)")

    # Time span
    date_begin: Optional[str] = Field(default=None, description="the occupation begin date")
    date_end: Optional[str] = Field(default=None, description="the occupation end date")

    # Occupation types (social role, formation, ...)
    has_social_role: bool = Field(default=False, description="has the occupation a social role (eg state deputy, municipal counselor, ...)")
    is_formation: bool = Field(default=False, description="is the occupation a formation (apprentice, school, ...)")



class Occupations(BaseModel):
    """
    List of all occupations mentions in the text
    """

    person_name: Optional[str] = Field(default=None, description="the person name")
    occupations: List[Occupation] = Field(default=None, description="the list of occupations this person had")



def get_assertions(occupations: Occupations) -> List[str]:
    """List all assertions from the extracted Occupation"""

    assertions = []

    for occupation in occupations.occupations:
        if occupation.occupation_name: 
            assertions.append(f"{occupation.occupation_name} is a job/position, a formation or a profession.")
        if occupations.person_name and occupation.occupation_name:
            assertions.append(f"{occupations.person_name} was doing {occupation.occupation_name}.")
        if occupations.person_name and occupation.place: 
            assertions.append(f"{occupations.person_name} was doing {occupation.occupation_name} in {occupation.place}.")
        if occupations.person_name and occupation.occupation_name and occupation.date_begin: 
            assertions.append(f"{occupations.person_name} started {occupation.occupation_name} in {occupation.date_begin}.")
        if occupations.person_name and occupation.occupation_name and occupation.date_end: 
            assertions.append(f"{occupations.person_name} stopped {occupation.occupation_name} in {occupation.date_end}.")
        if occupations.person_name and occupation.occupation_name and occupation.company: 
            assertions.append(f"{occupations.person_name} did {occupation.occupation_name} in {occupation.company}.")
        if occupations.person_name and occupation.occupation_name and occupation.has_social_role: 
            assertions.append(f"The occupation '{occupation.occupation_name}' of {occupations.person_name} had a social role.")
        if occupations.person_name and occupation.occupation_name and occupation.is_formation: 
            assertions.append(f"The occupation \"{occupation.occupation_name}\" of {occupations.person_name} is a formation.")

    return assertions