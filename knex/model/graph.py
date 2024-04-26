from typing import List, Set
from spacy.tokens import Span, Doc
from .entity import Entity
from .triple import Triple


class Graph:

    def __init__(self):
        self.triples: List[Triple] = []
        self.keys: Set[str] = set()

        self.entities: List[Entity] = []
        self.pk_index = 0

        self.functions: List[function] = []
        self.debug = False

    def reset(self):
        self.pk_index = 0
        self.entities = []
        self.triples = []
        self.keys = set()


    def create_entity(
            self,
            pk_class: int,
            text: str = None,
            span: Span = None,
            linked: bool = False
        ) -> int:
        """Create or get an existing entity based on given information."""

        # Get the entity label
        if text: label = text.title()
        if span and not text: label = span.text.title()

        # Find similar entities (if exist): entities that have the same class and the same label. i.e. record linkage
        same = list(filter(lambda entity: entity.pk_class == pk_class and entity.label == label, self.entities))

        # Save the orphan fact in the doc directly
        if span and not span._.linked: span._.linked = linked
        
        # If one is found, returns it (and set meta information)
        if len(same) == 1:
            if span: span._.pk_entity = same[0].pk_entity
            return same[0].pk_entity
        
        # Raise an Error if multiples are found
        elif len(same) > 1: 
            raise Exception(f'Multiple entity found for [{pk_class['label']}:{text}]')
        
        # If none is found, create a new one
        else:
            self.pk_index += 1
            pk_entity = self.pk_index
            if span: span._.pk_entity = pk_entity
            self.entities.append(Entity(pk_entity, pk_class, label))
            return pk_entity
        

    def get_entity(self, pk_entity: int) -> Entity:
        """Get the full Entity object from the given pk."""

        same = list(filter(lambda entity: entity.pk_entity == pk_entity, self.entities))

        if len(same) == 1: return same[0]
        if len(same) == 0: raise Exception(f'No entity with pk [{pk_entity}] found.')
        if len(same) > 0: raise Exception(f'Multiple entity found for pk [{pk_entity}]')


    def add_triple(self, pk_subject: int, pk_property: int, pk_object: int) -> None:

        # Check if triple already exists
        key = f"{pk_subject}-{pk_property}-{pk_object}"
        if key in self.keys: return
        else: self.keys.add(key)

        # Create the triple
        self.triples.append(Triple(pk_subject, pk_property, pk_object))


    def extract(self, doc: Doc) -> None:
        for function in self.functions:
            function(doc)