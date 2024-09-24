from typing import Optional, List
from langchain_core.pydantic_v1 import BaseModel, Field


class Person(BaseModel):
    """
    Information from the text about a person.
    """

    # General informations
    name: Optional[str] = Field(default=None, description="the name of the person")
    gender: Optional[str] = Field(default=None, description='"male" or "female"')
    origins: Optional[str] = Field(default=None, description="the person origin: geographical place")
    religion: Optional[str] = Field(default=None, description="the person religion name")

    # Birth
    birth_date: Optional[str] = Field(default=None, description="the person birth date")
    birth_place: Optional[str] = Field(default=None, description="the birth place of the person (geographical place)")
    
    # Death
    death_date: Optional[str] = Field(default=None, description="the person death date")
    death_place: Optional[str] = Field(default=None, description="the birth place of the person (geographical place)")
    
    # Genealogy
    father_name: Optional[str] = Field(default=None, description="the father of the person")
    mother_name: Optional[str] = Field(default=None, description="the mother of the person")


def get_assertions(person: Person) -> List[str]:
    """List all assertions from the extracted Person"""

    assertions = []
    if person.gender: assertions.append(f"{person.name} is a {person.gender}.")
    if person.origins: assertions.append(f"{person.name} has its origin in {person.origins}.")
    if person.religion: assertions.append(f"{person.name} religion is {person.religion}.")
    if person.birth_date: assertions.append(f"{person.name} was born on {person.birth_date}.")
    if person.birth_place: assertions.append(f"{person.name} was born in {person.birth_place}.")
    if person.death_date: assertions.append(f"{person.name} died on {person.death_date}.")
    if person.death_place: assertions.append(f"{person.name} died in {person.death_place}.")
    if person.father_name: assertions.append(f"{person.name} is the child of {person.father_name}.")
    if person.mother_name: assertions.append(f"{person.name} is the child of {person.mother_name}.")
    # for occupation in person.occupations:
    #     assertions += get_occupation_assertions(occupation, person.name)

    return assertions
