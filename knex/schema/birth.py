from typing import Optional, ClassVar
from langchain_core.pydantic_v1 import Field
from ..globals import schemas
from ..model import ExtractedSchema


class Birth(ExtractedSchema):
    """Information about a person's birth."""
    
    topic: ClassVar = 'birth'

    person_name: Optional[str] = Field(default=None, description="The name of a person which has a birth.")
    birth_date: Optional[str] = Field(default=None, description="The birth date")
    birth_place: Optional[str] = Field(default=None, description="The birth place")

    def explicit(self) -> str:
        text = ''
        name = self.person_name or 'Someone'
        if self.birth_date: text += f"{name} was born on {self.birth_date}. "
        if self.birth_place: text += f"{name} was born in {self.birth_place}. "
        return text.strip()[:-1] + "."
    

    def to_ontome_model



schemas.append(Birth)