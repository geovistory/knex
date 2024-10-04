from spacy.matcher import DependencyMatcher
from spacy.tokens import Doc
from ..constants.ontology import classes, properties
from ..globals import nlp, graph
from ..debug import debug
from .date import link_date


matcher = DependencyMatcher(nlp.vocab)
pattern_person = [
    {'RIGHT_ID': 'die', 'RIGHT_ATTRS': {'LEMMA': 'die'}},
    {'RIGHT_ID': 'person', 'RIGHT_ATTRS': {'ENT_TYPE': 'PERSON'}, 'REL_OP':'>', 'LEFT_ID': 'die'},
]
pattern_person_date = [
    {'RIGHT_ID': 'die', 'RIGHT_ATTRS': {'LEMMA': 'die'}},
    {'RIGHT_ID': 'person', 'RIGHT_ATTRS': {'ENT_TYPE': 'PERSON'}, 'REL_OP':'>', 'LEFT_ID': 'die'},
    {'RIGHT_ID': 'date', 'RIGHT_ATTRS': {'ENT_TYPE': 'DATE'}, 'REL_OP':'>', 'LEFT_ID': 'die'},
]
pattern_person_place = [
    {'RIGHT_ID': 'die', 'RIGHT_ATTRS': {'LEMMA': 'die'}},
    {'RIGHT_ID': 'person', 'RIGHT_ATTRS': {'ENT_TYPE': 'PERSON'}, 'REL_OP':'>', 'LEFT_ID': 'die'},
    {'RIGHT_ID': 'geoplace', 'RIGHT_ATTRS': {'ENT_TYPE': 'GPE'}, 'REL_OP':'>>', 'LEFT_ID': 'die'},
]
pattern_person_date_place = [
    {'RIGHT_ID': 'die', 'RIGHT_ATTRS': {'LEMMA': 'die'}},
    {'RIGHT_ID': 'person', 'RIGHT_ATTRS': {'ENT_TYPE': 'PERSON'}, 'REL_OP':'>', 'LEFT_ID': 'die'},
    {'RIGHT_ID': 'date', 'RIGHT_ATTRS': {'ENT_TYPE': 'DATE'}, 'REL_OP':'>', 'LEFT_ID': 'die'},
    {'RIGHT_ID': 'geoplace', 'RIGHT_ATTRS': {'ENT_TYPE': 'GPE'}, 'REL_OP':'>>', 'LEFT_ID': 'die'},
]
matcher.add('death_person', [pattern_person])
matcher.add('death_person_date', [pattern_person_date])
matcher.add('death_person_place', [pattern_person_place])
matcher.add('death_person_date_place', [pattern_person_date_place])


def extract_death(doc: Doc) -> None:

    matchings = matcher(doc)
    for match_id, indexes in matchings:

        # If we only have the death of a person
        if nlp.vocab.strings[match_id] == 'death_person':

            # Logs
            if debug('death'):
                print(f'> Death found: {doc[indexes[1]:indexes[1]+1]} (PERSON)')

            # Extract info 
            person_span = doc[indexes[1]:indexes[1]+1]

            # Create nodes
            pk_person = graph.create_entity(classes.E21_person, span=person_span, linked=True)
            pk_death = graph.create_entity(classes.E69_death, text=person_span.text)

            # Create edges
            graph.add_triple(pk_death, properties.P100_wasDeathOf, pk_person)


        # If we have the death of a person at a date
        if nlp.vocab.strings[match_id] == 'death_person_date':

            # Logs
            if debug('death'):
                print(f'> Death found: {doc[indexes[1]:indexes[1]+1]} (PERSON), {doc[indexes[2]:indexes[2]+1]} (DATE)')

            # Extract info from 
            person_span = doc[indexes[1]:indexes[1]+1]
            date_span = doc[indexes[2]:indexes[2]+1]

            # Create nodes
            pk_person = graph.create_entity(classes.E21_person, span=person_span, linked=True)
            pk_death = graph.create_entity(classes.E69_death, text=person_span.text)

            # Link nodes
            graph.add_triple(pk_death, properties.P100_wasDeathOf, pk_person)
            link_date(pk_death, date_span)


        # If we have the death of a person in a place
        if nlp.vocab.strings[match_id] == 'death_person_place':

            # Logs
            if debug('death'):
                print(f'> Death found: {doc[indexes[1]:indexes[1]+1]} (PERSON), {doc[indexes[2]:indexes[2]+1]} (GPE)')

            # Extract info from matching 
            person_span = doc[indexes[1]:indexes[1]+1]
            geoplace_span = doc[indexes[2]:indexes[2]+1]

            # Create nodes
            pk_person = graph.create_entity(classes.E21_person, span=person_span, linked=True)
            pk_death = graph.create_entity(classes.E69_death, text=person_span.text)
            pk_geoplace = graph.create_entity(classes.C13_geographicalPlace, span=geoplace_span, linked=True)

            # Link nodes
            graph.add_triple(pk_death, properties.P100_wasDeathOf, pk_person)
            graph.add_triple(pk_death, properties.P8_tookPlaceOnOrWithin, pk_geoplace)


        # If we have the death of a person at a date in a place
        if nlp.vocab.strings[match_id] == 'death_person_date_place':

            # Logs
            if debug('death'):
                print(f'> Death found: {doc[indexes[1]:indexes[1]+1]} (PERSON), {doc[indexes[2]:indexes[2]+1]} (DATE), {doc[indexes[3]:indexes[3]+1]} (GPE)')

            # Extract info from 
            person_span = doc[indexes[1]:indexes[1]+1]
            date_span = doc[indexes[2]:indexes[2]+1]
            geoplace_span = doc[indexes[3]:indexes[3]+1]

            # Create nodes
            pk_person = graph.create_entity(classes.E21_person, span=person_span, linked=True)
            pk_death = graph.create_entity(classes.E69_death, text=person_span.text)
            pk_geoplace = graph.create_entity(classes.C13_geographicalPlace, span=geoplace_span, linked=True)

            # Link nodes
            graph.add_triple(pk_death, properties.P100_wasDeathOf, pk_person)
            graph.add_triple(pk_death, properties.P8_tookPlaceOnOrWithin, pk_geoplace)
            link_date(pk_death, date_span)

graph.functions.append(extract_death)
