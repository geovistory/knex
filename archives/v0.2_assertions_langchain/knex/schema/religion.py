from typing import Optional, ClassVar
from pydantic import Field
from ..globals import schemas
from ..model import ExtractedSchema


class Religion(ExtractedSchema):
    """Information about a person's religion."""
    
    topic: ClassVar = 'religion'

    person_name: Optional[str] = Field(default=None, description="The name of a person which has a religion.")
    religion_name: Optional[str] = Field(default=None, description="The religion name.")

    def explicit(self) -> str:
        text = ''
        name = self.person_name or 'Someone'
        if self.religion_name: text += f"{name} was (a) {self.religion_name}. "
        return text.strip()[:-1] + "."



schemas.append(Religion)