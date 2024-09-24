from typing import List, Any
from pydantic import BaseModel
import pandas as pd
from .ontology import OntoObject, ontology as onto, properties, classes


class Entity(BaseModel):
    pk: int
    klass: OntoObject
    label: str


class Triple(BaseModel):
    subject: Entity
    property: OntoObject
    object: Entity | str


class Graph(BaseModel):
    
    entities: List[Entity] = []
    triples: List[Triple] = []
    pk_index: int = 1


    def get_current_index(self):
        return self.pk_index

    def create_entity(self, pk_class: int, label: str) -> Entity:
        """
        Create or get the entity with given informations.

        Parameter:
        pk_class [int]: The class of the entity to create/get
        label [str]: The label of the entity to create/get
        """

        # Look in memory if we have an existing entity
        filtered = list(filter(lambda entity: entity.klass.pk == pk_class and entity.label == label, self.entities))

        # If there is none, create it
        if len(filtered) == 0:
            entity = Entity(pk=self.pk_index, klass=onto.klass(pk_class), label=label)
            self.pk_index += 1
            self.entities.append(entity)
            return entity
        
        # If it already exists, returns it
        if len(filtered) > 0:
            return filtered[0]
        

    def create_triple(self, subject: Entity, property: int, object: Entity | str) -> None:
        """
        Create or get the triple from given informations.

        Parameter:
        subject [Entity]: the subject entity
        property [int]: the property to link
        object [Entity]: the object entity
        """
    
        # Look in memory if we have an existing entity
        def is_same_triple(triple: Triple):
            if triple.subject.pk != subject.pk: return False
            if triple.property.pk != property: return False
            if type(object) != type(triple.object): return False
            if isinstance(object, Entity) and isinstance(triple.object, Entity) and object.pk != triple.object.pk: return False
            if isinstance(object, str) and isinstance(triple.object, str) and object != triple.object: return False
            return True
        filtered = list(filter(is_same_triple, self.triples))

        # If there is none, create it
        if len(filtered) == 0:
            triple = Triple(subject=subject, property=onto.property(property), object=object)
            self.triples.append(triple)


    def create_entity_aial(self, pk_class: int, name: str):
        """
        Shortcut to create an entity and add an appellation in a language with the given name.

        Parameter:
        pk_class [int]: the entity to create an AiaL for
        name [str]: the name to give the entity (label and refersToName triple)
        """

        # Create the entity
        entity = self.create_entity(pk_class, name)

        # Create the Appellation in a Language
        aial = self.create_entity(classes.C11_appellationInALanguage, name)

        # Link the Appellation in a Language with the Entity
        self.create_triple(aial, properties.P11_isAppellationForLanguageOf, entity)

        # Create the name of the entity (value)
        self.create_triple(aial, properties.P13_refersToName, name)

        return entity
    

    def dataframes(self):
        """Return the entities and triples as DataFrames"""

        entities = list(map(lambda entity: ({'pk': entity.pk, 'pk_class': entity.klass.pk, 'label': entity.label}), self.entities))
        triples = list(map(lambda triple: ({'subject': triple.subject.pk, 'property': triple.property.pk, 'object': triple.object.pk if isinstance(triple.object, Entity) else triple.object}), self.triples))

        return pd.DataFrame(entities), pd.DataFrame(triples)
    

    def to_dataframe(self):
        """Transform the graph object into a global dataframe"""

        entities, triples = self.dataframes()

        entities['class_label'] = [onto.klass(pk_class).label for pk_class in entities['pk_class']]
        entities['display'] =  [row['class_label'] + ' - ' + row['label'] for _, row in entities.iterrows()]
        triples['property_label'] = [onto.property(prop).label for prop in triples['property']]

        df = triples.merge(entities, left_on='subject', right_on='pk', how='left') \
                        .drop(columns=['pk']) \
                        .rename(columns={'pk_class': 'subject_pk_class', 'class_label': 'subject_class_label', 'label': 'subject_label', 'display': 'subject_display'}) \
                    .merge(entities, left_on='object', right_on='pk', how='left') \
                        .drop(columns=['pk']) \
                        .rename(columns={'pk_class': 'object_pk_class', 'class_label': 'object_class_label', 'label': 'object_label', 'display': 'object_display'}) \
        

        columns = [
            'subject', 'subject_pk_class', 'subject_class_label', 'subject_label', 'subject_display',
            'property', 'property_label',
            'object', 'object_pk_class', 'object_class_label', 'object_label', 'object_display',
        ]

        return df[columns]
