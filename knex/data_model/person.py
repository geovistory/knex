from typing import Optional, List
from langchain_core.pydantic_v1 import BaseModel, Field

from .occupation import Occupation
from .relationship import Relationship


class Person(BaseModel):
    """Information from the text about the wanted person, "the person" in following descriptions"""

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
    
    # Lists
    # occupations: Optional[List[Occupation]] = Field(default=[], description="the person professional occupations")
    # relationships: Optional[List[Relationship]] = Field(default=[], description="the person relations (avoid parenthood relations)")


    def validate(self):
        forbidden = ['', 'unspecified', 'unknown']
        if self.name.lower() in forbidden: self.name = None
        if self.gender.lower() in forbidden: self.gender = None
        if self.origins.lower() in forbidden: self.origins = None
        if self.religion.lower() in forbidden: self.religion = None
        if self.birth_date.lower() in forbidden: self.birth_date = None
        if self.birth_place.lower() in forbidden: self.birth_place = None
        if self.death_date.lower() in forbidden: self.death_date = None
        if self.death_place.lower() in forbidden: self.death_place = None
        if self.father_name.lower() in forbidden: self.father_name = None
        if self.mother_name.lower() in forbidden: self.mother_name = None


    def get_assertions(self):
        assertions = []
        if self.gender: assertions.append(f"{self.name} is a {self.gender}.")
        if self.origins: assertions.append(f"{self.name} has its origin in {self.origins}.")
        if self.religion: assertions.append(f"{self.name} religion is {self.religion}.")
        if self.birth_date: assertions.append(f"{self.name} was born on {self.birth_date}.")
        if self.birth_place: assertions.append(f"{self.name} was born in {self.birth_place}.")
        if self.death_date: assertions.append(f"{self.name} died on {self.death_date}.")
        if self.death_place: assertions.append(f"{self.name} died in {self.death_place}.")
        if self.father_name: assertions.append(f"{self.name} is the child of {self.father_name}.")
        if self.mother_name: assertions.append(f"{self.name} is the child of {self.mother_name}.")

        return assertions
