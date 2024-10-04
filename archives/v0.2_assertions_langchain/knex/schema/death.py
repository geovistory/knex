from typing import Optional, ClassVar
from pydantic import Field
from ..globals import schemas
from ..model import ExtractedSchema


class Death(ExtractedSchema):
    """Information about a person's death."""
    
    topic: ClassVar = 'death'

    person_name: Optional[str] = Field(default=None, description="The name of a person which has a death.")
    death_date: Optional[str] = Field(default=None, description="The death date")
    death_place: Optional[str] = Field(default=None, description="The death place")

    def explicit(self) -> str:
        text = ''
        name = self.person_name or 'Someone'
        if self.death_date: text += f"{name} died on {self.death_date}. "
        if self.death_place: text += f"{name} died in {self.death_place}. "
        return text.strip()[:-1] + "."



schemas.append(Death)