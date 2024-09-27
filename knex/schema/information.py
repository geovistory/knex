from typing import List
import pandas as pd

from .person import Person
from .activities import Activity
from .relationships import Relationship


class Information:
    """
    This is the result object of the full extraction.
    By default all attributes are set to None.
    """
    persons_names: List[str] = None
    persons: List[Person] = None
    activities: List[Activity] = None
    relationships: List[Relationship] = None


    def dataframes(self) -> List[pd.DataFrame]:
        """
        Transform all list of information to the corresponding DataFrame.

        Returns:
            List[pd.DataFrame]: The list of all Information DataFrames. 
        """

        return {
            'persons': pd.DataFrame(data=list(map(lambda obj: obj.dict(), self.persons))) if self.persons else None,
            'relationships': pd.DataFrame(data=list(map(lambda obj: obj.dict(), self.relationships))) if self.relationships else None,
            'activities': pd.DataFrame(data=list(map(lambda obj: obj.dict(), self.activities))) if self.activities else None,
        }