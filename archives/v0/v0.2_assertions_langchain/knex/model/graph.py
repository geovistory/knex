from typing import List
from pydantic import BaseModel
from .triple import Triple
from .entity import Entity
from ..constants import ontology



class Graph(BaseModel):
    """Keep information following the ontology."""

    # The list of all triples of the graph
    triples: List[Triple]

    # The list of the instances of the graph
    entities: List[Entity]

    # An index which increases with entities creation
    pk_index: int = 0


    def __init__(self):
        pass


    def create_entity(self, pk_class: int, label: str):
        """Create or get (pk) an existing entity based on given information."""

        klass = ontology.klass(pk_class)

        # Record linkage: entities have same class and same label
        same = list(filter(lambda entity: entity.pk_class == pk_class and entity.label == label, self.entities))

        # If one is found, returns it
        if len(same) == 1: 
            return same[0].pk_entity
            
        # Raise an Error if multiples are found
        elif len(same) > 1: 
            raise Exception(f"Multiple entities found for [{klass.labe}:{label}]")
        
        # If none is found, create a new one
        else:
            self.pk_index += 1
            pk_entity = self.pk_index
            self.entities.append(Entity(pk_entity, pk_class, label))
            return pk_entity
        
