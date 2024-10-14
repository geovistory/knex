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
    
    @staticmethod
    def from_dataframes(persons: pd.DataFrame, activities: pd.DataFrame, relationships: pd.DataFrame) -> 'Information':

        info = Information()

        # Get all the person names
        info.persons_names = persons['names'].unique().tolist()

        # Create all persons
        info.persons = []
        for _, person in persons.iterrows():
            info.persons.append(Person(
                name=person['name'],
                gender=person['gender'],
                origins=person['origins'],
                religion=person['religion'],
                birth_date=person['birth_date'],
                birth_place=person['birth_place'],
                death_date=person['death_date'],
                death_place=person['death_place'],
                father_name=person['father_name'],
                mother_name=person['mother_name'],
            ))

        # Create all activities
        info.activities = []
        for _, activity in activities.iterrows():
            info.activities.append(Activity(
                person_name=activity['person_name'],
                name=activity['name'],
                place=activity['place'],
                date_begin=activity['date_begin'],
                date_end=activity['date_end'],
                activity_type=activity['activity_type'],
                institution=activity['institution'],
                discipline=activity['discipline'],
            ))

        # Create all activities
        info.relationships = []
        for _, relationship in relationships.iterrows():
            info.relationships.append(Relationship(
                person1_name=relationship['person1_name'],
                person2_name=relationship['person2_name'],
                date_begin=relationship['date_begin'],
                date_end=relationship['date_end'],
                relationship_type=relationship['relationship_type'],
            ))