from typing import Optional, List
from pydantic import BaseModel, Field


# This class is to be given to a LLM.
# Classes descriptions, attributes names, fields description should be set thoroughly.
class Activity(BaseModel):
    """An activity made by a person."""

    person_name: Optional[str] = Field(default=None, description="the person doing the activity")
    name: Optional[str] = Field(default=None, description="the activity name")
    place: Optional[str] = Field(default=None, description="the activity place")
    date_begin: Optional[str] = Field(default=None, description="the activity begin date (only)")
    date_end: Optional[str] = Field(default=None, description="the activity end date (only)")
    activity_type: Optional[str] = Field(default=None, description="one of: job, social role, formation")
    institution: Optional[str] = Field(default=None,  description="the institution of the activity (a company, a university, a city hall, ...)")
    discipline: Optional[str] = Field(default=None, description="in case the activity is a formation, the discipline studied.")


# This class is to be given to a LLM.
# Class description, fields description should be set accordingly.
class Activities(BaseModel):
    """List of activities mentioned in the context"""

    activities: List[Activity] = Field(default=[], description="list of all activities mentioned in the text")


def get_activities_assertions(activities: Activities) -> List[str]:
    """
    Produce the assertion for Activities
    
    Args: 
        activities (Activities): An object having a list of activities

    Returns:
        List[str]: the list of assertions from the given activities
    """

    assertions = []
    for act in activities.activities:
        assertions.append(f"{act.person_name} did {act.name}.")
        if act.place:
            assertions.append(f"{act.person_name}'s {act.activity_type}, {act.name}, was in {act.place}.")
        if act.date_begin:
            assertions.append(f"{act.person_name}'s {act.activity_type}, {act.name}, started in {act.date_begin}.")
        if act.date_end:
            assertions.append(f"{act.person_name}'s {act.activity_type}, {act.name}, ended in {act.date_end}.")
        if act.institution:
            assertions.append(f"{act.person_name}'s {act.activity_type}, {act.name}, was taking place in {act.institution}")
        if act.discipline:
            assertions.append(f"{act.person_name}'s {act.activity_type}, {act.name}, was about {act.discipline}")
    
    return assertions