from typing import List, Tuple
from pydantic import BaseModel
from pyvis.network import Network
import pandas as pd
from ..constants import OntoObject, ontology as onto, properties as p, classes as c, colors


class Entity(BaseModel):
    pk: int
    klass: OntoObject
    label: str


class Triple(BaseModel):
    subject: Entity
    property: OntoObject
    object: Entity


class Graph(BaseModel):
    
    entities: List[Entity] = []
    triples: List[Triple] = []
    pk_index: int = 1


    def get_current_index(self) -> int:
        """
        Return the index of the next created entity.
        Usefull for example to set a unique label to an entity.

        Returns: 
            int: The pk given to the next entity.
        """
        return self.pk_index


    def create_entity(self, pk_class: int, label: str) -> Entity:
        """
        Create or get the entity with given informations.

        Args:
            pk_class (int): The class of the entity to create/get.
            label (str): The label of the entity to create/get.

        Returns:
            Entity: The entity that has been created (or fetched).
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
        

    def create_triple(self, subject: Entity, property: int, object: Entity) -> None:
        """
        Create the triple from given informations, if it does not already exist.

        Args:
            subject (Entity): the subject entity.
            property (int): the property to link.
            object (Entity): the object entity.
        """
    
        # Look in memory if we have an existing entity
        filtered = list(filter(lambda t: t.subject.pk == subject.pk and t.property.pk == property and t.object.pk == object.pk, self.triples))

        # If there is none, create it
        if len(filtered) == 0:
            triple = Triple(subject=subject, property=onto.property(property), object=object)
            self.triples.append(triple)


    def create_entity_aial(self, pk_class: int, name: str) -> Entity:
        """
        Shortcut to create an entity and add an appellation in a language with the given name.

        Args:
            pk_class (int): the entity to create an AiaL for.
            name (str): the name to give to the entity (label and refersToName triple).

        Returns:
            Entity: The entity that has been created (or fetched).
        """

        # Create the entity
        entity = self.create_entity(pk_class, name)

        # Create the Appellation in a Language
        if pk_class == c.E21_person: klass = c.C38_personAppellationInALanguage
        else: klass = c.C11_appellationInALanguage
        aial = self.create_entity(klass, name)

        # Create the Appellation
        appe = self.create_entity(c.E41_appellation, name)

        # Link the Appellation in a Language with the Entity
        self.create_triple(aial, p.P11_isAppellationForLanguageOf, entity)

        # Create the name of the entity (value)
        self.create_triple(aial, p.P13_refersToName, appe)

        return entity
    

    def dataframes(self) -> Tuple[pd.DataFrame]:
        """
        Return the entities and triples as DataFrames.
        
        Returns:
            Tuple[pd.DataFrame]: A tuple of length 2 with at first the entities df, and second triples df.
        """

        entities = list(map(lambda entity: ({'pk': entity.pk, 'pk_class': entity.klass.pk, 'label': entity.label}), self.entities))
        triples = list(map(lambda triple: ({'subject': triple.subject.pk, 'property': triple.property.pk, 'object': triple.object.pk if isinstance(triple.object, Entity) else triple.object}), self.triples))

        return pd.DataFrame(entities), pd.DataFrame(triples)
    

    def to_dataframe(self) -> pd.DataFrame:
        """
        Transform the graph object into a global dataframe.
        
        Returns:
            pd.DataFrame: A global DataFrame representing the full graph.
        """

        entities, triples = self.dataframes()
        if len(entities) == 0: return pd.DataFrame()


        entities['class_label'] = [onto.klass(pk_class).label for pk_class in entities['pk_class']]
        entities['display'] =  [row['class_label'] + ' - ' + row['label'] for _, row in entities.iterrows()]
        triples['property_label'] = [onto.property(prop).label for prop in triples['property']]

        df = triples.merge(entities, left_on='subject', right_on='pk', how='left') \
                        .drop(columns=['pk']) \
                        .rename(columns={'pk_class': 'subject_class_pk', 'class_label': 'subject_class_label', 'label': 'subject_label', 'display': 'subject_display'}) \
                    .merge(entities, left_on='object', right_on='pk', how='left') \
                        .drop(columns=['pk']) \
                        .rename(columns={'pk_class': 'object_class_pk', 'class_label': 'object_class_label', 'label': 'object_label', 'display': 'object_display'}) \
        

        columns = [
            'subject', 'subject_class_pk', 'subject_class_label', 'subject_label', 'subject_display',
            'property', 'property_label',
            'object', 'object_class_pk', 'object_class_label', 'object_label', 'object_display',
        ]
        df = df[columns]

        df['subject_class_pk'] = df['subject_class_pk'].astype(pd.Int64Dtype())
        df['object_class_pk'] = df['object_class_pk'].astype(pd.Int64Dtype())

        return df[columns]


    def get_visuals(self, path: str) -> None:
        """
        Generate a html file with a graph visual, and save it at the given place
        
        Args:
            path (str): the place to store the html file.
        """

        graph = self.to_dataframe()
        if len(graph) == 0: return

        # A bit of formating
        graph['subject_display'] = graph['subject_display'].str.replace(' - ', '\n') 
        graph['object_display'] = graph['object_display'].str.replace(' - ', '\n') 

        # Add node colors:
        graph['subject_color'] = [colors[klass] if pd.notna(klass) else '#000' for klass in graph['subject_class_pk']]
        graph['object_color'] = [colors[klass] if pd.notna(klass) else '#000' for klass in graph['object_class_pk']]

        # Extract nodes
        nodes_subject = graph[['subject', 'subject_display', 'subject_color']].drop_duplicates(subset=['subject'])
        nodes_object = graph[['object', 'object_display', 'object_color']].drop_duplicates(subset=['object'])
    
        # Add the node to the network
        network = Network(height=750, width=1500, notebook=False, cdn_resources='remote')
        network.add_nodes(nodes_subject['subject_display'].tolist(), color=nodes_subject['subject_color'].tolist())
        network.add_nodes(nodes_object['object_display'].tolist(), color=nodes_object['object_color'].tolist())

        # Add the edges
        for _, row in graph.iterrows():
            network.add_edge(str(row['subject_display']), str(row['object_display']), label=row['property_label'])

        # Set the options
        network.set_options("""
            const options = {
                "nodes": {"font": {"face": "tahoma"}},
                "edges": {
                    "arrows": {"to": {"enabled": true}},
                    "font": {"size": 10,"face": "tahoma","align": "top"}
                }
            }
        """)


        # Generating the file
        # network.show_buttons(filter_=['physics'])
        network.show(path, local=True, notebook=False)
