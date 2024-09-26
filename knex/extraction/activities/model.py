from typing import Optional, List
from langchain_core.pydantic_v1 import BaseModel, Field

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

class Activities(BaseModel):
    """List of activities mentioned in the context"""

    activities: List[Activity] = Field(default=[], description="list of all activities mentioned in the text")



def get_assertions(activities: Activities):

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