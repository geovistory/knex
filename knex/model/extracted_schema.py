from typing import ClassVar
from pydantic import BaseModel

class ExtractedSchema(BaseModel):
    """The root class for all extracted object from Assertions"""

    # The concerned Topic
    topic: ClassVar = 'unknown'

    def explicit(self) -> str:
        """Transform the extracted schema in a long string made of one sentence for each properties."""
        raise Exception('Not Implemented')
