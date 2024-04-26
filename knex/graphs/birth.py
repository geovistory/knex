from spacy.matcher import DependencyMatcher
from spacy.tokens import Doc
from ..constants.ontology import *
from ..globals import nlp, graph, params
from .date import link_date


matcher = DependencyMatcher(nlp.vocab)
pattern_person = [
    {'RIGHT_ID': 'born', 'RIGHT_ATTRS': {'TEXT': 'born'}},
    {'RIGHT_ID': 'person', 'RIGHT_ATTRS': {'ENT_TYPE': 'PERSON'}, 'REL_OP':'>', 'LEFT_ID': 'born'},
]
pattern_person_date = [
    {'RIGHT_ID': 'born', 'RIGHT_ATTRS': {'TEXT': 'born'}},
    {'RIGHT_ID': 'person', 'RIGHT_ATTRS': {'ENT_TYPE': 'PERSON'}, 'REL_OP':'>', 'LEFT_ID': 'born'},
    {'RIGHT_ID': 'date', 'RIGHT_ATTRS': {'ENT_TYPE': 'DATE'}, 'REL_OP':'>', 'LEFT_ID': 'born'},
]
pattern_person_place = [
    {'RIGHT_ID': 'born', 'RIGHT_ATTRS': {'TEXT': 'born'}},
    {'RIGHT_ID': 'person', 'RIGHT_ATTRS': {'ENT_TYPE': 'PERSON'}, 'REL_OP':'>', 'LEFT_ID': 'born'},
    {'RIGHT_ID': 'geoplace', 'RIGHT_ATTRS': {'ENT_TYPE': 'GPE'}, 'REL_OP':'>>', 'LEFT_ID': 'born'},
]
pattern_person_date_place = [
    {'RIGHT_ID': 'born', 'RIGHT_ATTRS': {'TEXT': 'born'}},
    {'RIGHT_ID': 'person', 'RIGHT_ATTRS': {'ENT_TYPE': 'PERSON'}, 'REL_OP':'>', 'LEFT_ID': 'born'},
    {'RIGHT_ID': 'date', 'RIGHT_ATTRS': {'ENT_TYPE': 'DATE'}, 'REL_OP':'>', 'LEFT_ID': 'born'},
    {'RIGHT_ID': 'geoplace', 'RIGHT_ATTRS': {'ENT_TYPE': 'GPE'}, 'REL_OP':'>>', 'LEFT_ID': 'born'},
]
matcher.add('birth_person', [pattern_person])
matcher.add('birth_person_date', [pattern_person_date])
matcher.add('birth_person_place', [pattern_person_place])
matcher.add('birth_person_date_place', [pattern_person_date_place])


def extract_birth(doc):

    matchings = matcher(doc)
    for match_id, indexes in matchings:

        # If we only have the birth of a person
        if nlp.vocab.strings[match_id] == 'birth_person':

            # Logs
            if params.debug or 'birth' in params.debug_list:
                print(f'> Birth found: {doc[indexes[1]:indexes[1]+1]} (PERSON)')

            # Extract info 
            person_span = doc[indexes[1]:indexes[1]+1]

            # Create nodes
            pk_person = graph.create_entity(class_E21_person, span=person_span, linked=True)
            pk_birth = graph.create_entity(class_E67_birth, text=person_span.text)

            # Create edges
            graph.add_triple(pk_birth, property_P98_broughtIntoLife, pk_person)


        # If we have the birth of a person at a date
        if nlp.vocab.strings[match_id] == 'birth_person_date':

            # Logs
            if params.debug or 'birth' in params.debug_list:
                print(f'> Birth found: {doc[indexes[1]:indexes[1]+1]} (PERSON), {doc[indexes[2]:indexes[2]+1]} (DATE)')

            # Extract info from 
            person_span = doc[indexes[1]:indexes[1]+1]
            date_span = doc[indexes[2]:indexes[2]+1]

            # Create nodes
            pk_person = graph.create_entity(class_E21_person, span=person_span, linked=True)
            pk_birth = graph.create_entity(class_E67_birth, text=person_span.text)

            # Link nodes
            graph.add_triple(pk_birth, property_P98_broughtIntoLife, pk_person)
            link_date(pk_birth, date_span)


        # If we have the birth of a person in a place
        if nlp.vocab.strings[match_id] == 'birth_person_place':

            # Logs
            if params.debug or 'birth' in params.debug_list:
                print(f'> Birth found: {doc[indexes[1]:indexes[1]+1]} (PERSON), {doc[indexes[2]:indexes[2]+1]} (GPE)')

            # Extract info from 
            person_span = doc[indexes[1]:indexes[1]+1]
            geoplace_span = doc[indexes[2]:indexes[2]+1]

            # Create nodes
            pk_person = graph.create_entity(class_E21_person, span=person_span, linked=True)
            pk_birth = graph.create_entity(class_E67_birth, text=person_span.text)
            pk_geoplace = graph.create_entity(class_C13_geographicalPlace, span=geoplace_span, linked=True)

            # Link nodes
            graph.add_triple(pk_birth, property_P98_broughtIntoLife, pk_person)
            graph.add_triple(pk_birth, property_P6_tookPlaceAt, pk_geoplace)


        # If we have the birth of a person at a date in a place
        if nlp.vocab.strings[match_id] == 'birth_person_date_place':

            # Logs
            if params.debug or 'birth' in params.debug_list:
                print(f'> Birth found: {doc[indexes[1]:indexes[1]+1]} (PERSON), {doc[indexes[2]:indexes[2]+1]} (DATE), {doc[indexes[3]:indexes[3]+1]} (GPE)')

            # Extract info from 
            person_span = doc[indexes[1]:indexes[1]+1]
            date_span = doc[indexes[2]:indexes[2]+1]
            geoplace_span = doc[indexes[3]:indexes[3]+1]

            # Create nodes
            pk_person = graph.create_entity(class_E21_person, span=person_span, linked=True)
            pk_birth = graph.create_entity(class_E67_birth, text=person_span.text)
            pk_geoplace = graph.create_entity(class_C13_geographicalPlace, span=geoplace_span, linked=True)

            # Link nodes
            graph.add_triple(pk_birth, property_P98_broughtIntoLife, pk_person)
            graph.add_triple(pk_birth, property_P6_tookPlaceAt, pk_geoplace)
            link_date(pk_birth, date_span)

graph.functions.append(extract_birth)
