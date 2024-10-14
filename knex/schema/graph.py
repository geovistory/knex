from typing import List, Tuple
from pydantic import BaseModel
from pyvis.network import Network
import pandas as pd, numpy as np
import pickle
from ..constants import OntoObject, ontology as onto, properties as p, classes as c, colors


class Entity(BaseModel):
    pk: int
    klass: OntoObject
    label: str

    def get_display(self):
        return f"{self.label} ({self.klass.label} - pk{self.pk})"


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


    def get_entity(self, pk: int) -> Entity | None:
        """
        Given the pk, return the corresponding entity

        Args:
            pk (int): The pk of the entity to fetch
        Returns:
            Entity | None: The wanted entity
        """

        # Look in memory if we have an existing entity
        filtered = list(filter(lambda entity: entity.pk == pk, self.entities))

        if len(filtered) > 0: return filtered[0] 
        else: return None


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


    def delete_triple(self, pk_subject: int, pk_property: int, pk_object: int):
        """
        Delete a triple from the graph.

        Args:
            pk_subject (int): the pk subject 
            pk_property (int): the pk property
            pk_object (int): the pk_object
        """
        self.triples = list(filter(lambda t: t.subject.pk != pk_subject or t.property.pk != pk_property or t.object.pk != pk_object, self.triples))


    def merge_graph(self, graph: 'Graph'):
        # First the entities are merged
        new_pks = {}
        for entity in graph.entities:
            new_entity = self.create_entity(entity.klass.pk, entity.label)
            new_pks[entity.pk] = new_entity.pk

        # Then, triples from the second graph are merged
        for triple in graph.triples:
            subject = self.get_entity(new_pks[triple.subject.pk])
            object = self.get_entity(new_pks[triple.object.pk])
            self.create_triple(subject, triple.property.pk, object)
            

    def to_dataframe(self) -> pd.DataFrame:
        """
        Transform the graph object into a global dataframe.
        
        Returns:
            pd.DataFrame: A global DataFrame representing the full graph.
        """

        # If there is no entity in the graph, there is no need to go further
        if len(self.entities) == 0: 
            return pd.DataFrame()

        # Transform the entity list into a proper Dataframe
        entities = list(map(lambda entity: ({'pk': entity.pk, 'pk_class': entity.klass.pk, 'class_label': entity.klass.label, 'label': entity.label, 'display': entity.get_display()}), self.entities))
        entities = pd.DataFrame(entities)

        # Transform the triple list into a proper Dataframe
        triples = list(map(lambda triple: ({'subject': triple.subject.pk, 'property': triple.property.pk, 'property_label': triple.property.label, 'object': triple.object.pk}), self.triples))
        triples = pd.DataFrame(triples)

        # Craft the final dataframe with the needed informations
        df = triples.merge(entities, left_on='subject', right_on='pk', how='left') \
                        .drop(columns=['pk']) \
                        .rename(columns={'pk_class': 'subject_class_pk', 'class_label': 'subject_class_label', 'label': 'subject_label', 'display': 'subject_display'}) \
                    .merge(entities, left_on='object', right_on='pk', how='left') \
                        .drop(columns=['pk']) \
                        .rename(columns={'pk_class': 'object_class_pk', 'class_label': 'object_class_label', 'label': 'object_label', 'display': 'object_display'}) \
        
        # Select and reorder columns so that it is easy to read
        columns = [
            'subject', 'subject_class_pk', 'subject_class_label', 'subject_label', 'subject_display',
            'property', 'property_label',
            'object', 'object_class_pk', 'object_class_label', 'object_label', 'object_display',
        ]
        df = df[columns]

        # Type formating for some columns
        df['subject_class_pk'] = df['subject_class_pk'].astype(pd.Int64Dtype())
        df['object_class_pk'] = df['object_class_pk'].astype(pd.Int64Dtype())

        return df[columns]


    @staticmethod
    def from_dataframe(df: pd.DataFrame) -> 'Graph':
        """
        Create a graph out of a right formed given Dataframe.

        Args:
            df (pd.DataFrame): the dataframe of the graph
        """

        # Extract subject entities
        subjects = df[['subject', 'subject_class_pk', 'subject_label']]
        subjects.columns = ['pk', 'pk_class', 'label']

        # Extract object entities
        objects = df[['object', 'object_class_pk', 'object_label']]
        objects.columns = ['pk', 'pk_class', 'label']

        # The return object
        graph = Graph()

        # Get all the unique entities from the given dataframe, and put them in the return graph
        entities_df = pd.concat([subjects, objects]).drop_duplicates()
        entities = []
        for _, row in entities_df.iterrows():
            entities.append(Entity(pk=row['pk'], klass=onto.klass(row['pk_class']), label=row['label']))
        graph.entities = entities

        # Get all triples from the dataframe, and put then in the return graph
        triples_df = df[['subject', 'property', 'object']]

        triples = []
        for _, row in triples_df.iterrows():
            triples.append(Triple(subject=graph.get_entity(row['subject']), property=onto.property(row['property']), object=graph.get_entity(row['object'])))
        graph.triples = triples

        return graph


    def get_visuals(self, path: str) -> None:
        """
        Generate a html file with a graph visual, and save it at the given place
        
        Args:
            path (str): the place to store the html file.
        """

        graph = self.to_dataframe()
        if len(graph) == 0: return

        # A bit of formating
        graph['subject_display'] = graph['subject_display'].str.replace(' (', '\n(') 
        graph['object_display'] = graph['object_display'].str.replace(' (', '\n(') 

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


    def get_subgraph(self, pk_entity: int, depth: int):
        """
        Given an entity, fetch the sub graph of given depth

        Args:
            entities (int): The pk of the enetity to get the graph from
            depth (int): the depth of the wanted graph
        """

        entities_to_fetch = set({pk_entity})
        for _ in range(depth):
            selection = list(filter(lambda triple: triple.subject.pk in entities_to_fetch or triple.object.pk in entities_to_fetch, self.triples))
            entities_to_fetch.update(list(map(lambda triple: triple.subject.pk, selection)))
            entities_to_fetch.update(list(map(lambda triple: triple.object.pk, selection)))

        entities = list(map(lambda pk: self.get_entity(pk), entities_to_fetch))

        return Graph(entities=entities, triples=selection)