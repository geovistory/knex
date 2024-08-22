from spacy.matcher import Matcher
from spacy.tokens import Doc
from ..constants.ontology import *
from ..globals import nlp, graph
from ..debug import debug
from .date import link_date


matcher = Matcher(nlp.vocab)
pattern_social_role_embodiment1 = [
    # PERSON be a SOCIAL_ROLE
    [{'ENT_TYPE':'PERSON'}, {'LEMMA':'be'}, {'TEXT':'a','OP':'?'}, {'ENT_TYPE':'TYPE','OP':'?'}, {'ENT_TYPE':'SOCIAL_ROLE'}]
]
pattern_social_role_embodiment2 = [
    # PERSON held the position of SOCIAL_ROLE [',' | 'and'] SOCIAL_ROLE [',' | 'and'] SOCIAL_ROLE
    [{'ENT_TYPE':'PERSON'}, {'LEMMA':'hold'}, {'LEMMA':'the'}, {'LEMMA':'position'}, {'LEMMA':'of'}, {'ENT_TYPE':'SOCIAL_ROLE'}, {'LEMMA': {'IN': [',', 'and']}, 'OP':'?'}, {'ENT_TYPE':'SOCIAL_ROLE', 'OP':'?'}, {'LEMMA': {'IN': [',', 'and']}, 'OP':'?'}, {'ENT_TYPE':'SOCIAL_ROLE', 'OP':'?'}]
]
pattern_social_role_embodiment_gpe = [
    # PERSON be a SOCIAL_ROLE ['at', 'in'] GPE
    [{'ENT_TYPE':'PERSON'}, {'LEMMA':'be'}, {'TEXT':'a','OP':'?'}, {'ENT_TYPE':'TYPE','OP':'?'}, {'ENT_TYPE':'SOCIAL_ROLE'}, {'LEMMA': {'IN': ['at', 'in']}}, {'ENT_TYPE':'GPE'}],
]
pattern_social_role_embodiment_gpe_dates1 = [
    # PERSON be a ?TYPE SOCIAL_ROLE ['at', 'in'] GPE DATE DATE
    [{'ENT_TYPE':'PERSON'}, {'LEMMA':'be'}, {'TEXT':'a','OP':'?'}, {'ENT_TYPE':'TYPE','OP':'?'}, {'ENT_TYPE':'SOCIAL_ROLE'}, {'LEMMA': {'IN': ['at', 'in']}}, {'ENT_TYPE':'GPE'}, {'ENT_TYPE':'DATE'}, {'ENT_TYPE':'DATE'}],
]
pattern_social_role_embodiment_gpe_dates2 = [
    # PERSON be a ?TYPE SOCIAL_ROLE ['at', 'in'] GPE (DATE) 
    [{'ENT_TYPE':'PERSON'}, {'LEMMA':'be'}, {'TEXT':'a','OP':'?'}, {'ENT_TYPE':'TYPE','OP':'?'}, {'ENT_TYPE':'SOCIAL_ROLE'}, {'LEMMA': {'IN': ['at', 'in']}}, {'ENT_TYPE':'GPE'}, {'LEMMA': '('}, {'ENT_TYPE':'DATE'}, {'LEMMA': ')'} ],
]


matcher.add("social_role_embodiment1", pattern_social_role_embodiment1)
matcher.add("social_role_embodiment2", pattern_social_role_embodiment2)
matcher.add("social_role_embodiment_gpe", pattern_social_role_embodiment_gpe)
matcher.add("social_role_embodiment_gpe_dates1", pattern_social_role_embodiment_gpe_dates1)
matcher.add("social_role_embodiment_gpe_dates2", pattern_social_role_embodiment_gpe_dates2)


def extract_social_role_embodiment(doc: Doc) -> None:

    # For the matcher
    matchings = matcher(doc)
    for match_id, start, end in matchings:
        span = doc[start:end]

        # If we only have an social_role_embodiment of a person
        if nlp.vocab.strings[match_id] == 'social_role_embodiment1' or nlp.vocab.strings[match_id] == 'social_role_embodiment2':

            # Extract NER from the span
            person_span = list(filter(lambda ent: ent.label_ == "PERSON", span.ents))[0]
            social_role_spans = list(filter(lambda ent: ent.label_ == "SOCIAL_ROLE", span.ents))

            # Logs
            if debug('social_role'):
                social_role_string = ', '.join(map(lambda socrol: socrol.text + ' (SOCIAL_ROLE)', social_role_spans))
                print(f'> Social Role Embodiment found: {person_span.text} (PERSON), {social_role_string}')

            # Create graph nodes
            pk_person = graph.create_entity(classes.E21_person, span=person_span, linked=True)
            for social_role_span in social_role_spans:
                pk_social_role_embodiment = graph.create_entity(classes.C13_socialRoleEmbodiment, text=social_role_span.text)
                pk_social_role = graph.create_entity(classes.C12_actorSSocialRole, span=social_role_span, linked=True)

                # Create edges
                graph.add_triple(pk_social_role_embodiment, properties.P4_isOccupationOf, pk_person)
                graph.add_triple(pk_social_role_embodiment, properties.P5_isAbout, pk_social_role)


        # If we have an social_role_embodiment of a person at a place
        if nlp.vocab.strings[match_id] == 'social_role_embodiment_gpe':

            # Extract NER from the span
            person_span = list(filter(lambda ent: ent.label_ == "PERSON", span.ents))[0]
            social_role_span = list(filter(lambda ent: ent.label_ == "SOCIAL_ROLE", span.ents))[0]
            gpe_span = list(filter(lambda ent: ent.label_ == "GPE", span.ents))[0]

            # Logs
            if debug('social_role'):
                print(f'> Social Role Embodiment found: {person_span.text} (PERSON), {social_role_span.text} (SOCIAL_ROLE), {gpe_span.text} (GPE)')

            # Create graph nodes
            pk_person = graph.create_entity(classes.E21_person, span=person_span, linked=True)
            pk_social_role_embodiment = graph.create_entity(classes.C13_socialRoleEmbodiment, text=social_role_span.text)
            pk_social_role = graph.create_entity(classes.C12_actorSSocialRole, span=social_role_span, linked=True)
            pk_geoplace = graph.create_entity(classes.C13_geographicalPlace, span=gpe_span, linked=True)

            # Create edges
            graph.add_triple(pk_social_role_embodiment, properties.P4_isOccupationOf, pk_person)
            graph.add_triple(pk_social_role_embodiment, properties.P5_isAbout, pk_social_role)
            graph.add_triple(pk_social_role_embodiment, properties.P6_takesPlaceAt, pk_geoplace)


        # If we have an social_role_embodiment of a person at a place with a begin and an end date
        if nlp.vocab.strings[match_id] == 'social_role_embodiment_gpe_dates1':

            # Extract NER from the span
            person_span = list(filter(lambda ent: ent.label_ == "PERSON", span.ents))[0]
            social_role_span = list(filter(lambda ent: ent.label_ == "SOCIAL_ROLE", span.ents))[0]
            gpe_span = list(filter(lambda ent: ent.label_ == "GPE", span.ents))[0]
            date1_span = list(filter(lambda ent: ent.label_ == "DATE", span.ents))[0]
            date2_span = list(filter(lambda ent: ent.label_ == "DATE", span.ents))[1]

            # Logs
            if debug('social_role'):
                print(f'> Social Role embodiment found: {person_span.text} (PERSON), {social_role_span.text} (SOCIAL_ROLE), {gpe_span.text} (GPE), {date1_span} (DATE), {date2_span} (DATE)')

            # Create graph nodes
            pk_person = graph.create_entity(classes.E21_person, span=person_span, linked=True)
            pk_social_role_embodiment = graph.create_entity(classes.C13_socialRoleEmbodiment, text=social_role_span.text)
            pk_social_role = graph.create_entity(classes.C12_actorSSocialRole, span=social_role_span, linked=True)
            pk_geoplace = graph.create_entity(classes.C13_geographicalPlace, span=gpe_span, linked=True)

            # Create edges
            graph.add_triple(pk_social_role_embodiment, properties.P4_isOccupationOf, pk_person)
            graph.add_triple(pk_social_role_embodiment, properties.P5_isAbout, pk_social_role)
            graph.add_triple(pk_social_role_embodiment, properties.P6_takesPlaceAt, pk_geoplace)
            link_date(pk_social_role_embodiment, date1_span)
            link_date(pk_social_role_embodiment, date2_span)


        # If we have an social_role_embodiment of a person at a place with a begin and an end date in another format
        if nlp.vocab.strings[match_id] == 'social_role_embodiment_gpe_dates2':

            # Extract NER from the span
            person_span = list(filter(lambda ent: ent.label_ == "PERSON", span.ents))[0]
            social_role_span = list(filter(lambda ent: ent.label_ == "SOCIAL_ROLE", span.ents))[0]
            gpe_span = list(filter(lambda ent: ent.label_ == "GPE", span.ents))[0]
            date_span = list(filter(lambda ent: ent.label_ == "DATE", span.ents))[0]

            # Logs
            if debug('social_role'):
                print(f'> Social Role Embodiment found: {person_span.text} (PERSON), {social_role_span.text} (SOCIAL_ROLE), {gpe_span.text} (GPE), {date_span} (DATE)')

            # Create graph nodes
            pk_person = graph.create_entity(classes.E21_person, span=person_span, linked=True)
            pk_social_role_embodiment = graph.create_entity(classes.socialrole, text=social_role_span.text)
            pk_social_role = graph.create_entity(classes.C13_socialRoleEmbodiment, span=social_role_span, linked=True)
            pk_geoplace = graph.create_entity(classes.C13_geographicalPlace, span=gpe_span, linked=True)

            # Create edges
            graph.add_triple(pk_social_role_embodiment, properties.P4_isOccupationOf, pk_person)
            graph.add_triple(pk_social_role_embodiment, properties.P5_isAbout, pk_social_role)
            graph.add_triple(pk_social_role_embodiment, properties.P6_takesPlaceAt, pk_geoplace)
            link_date(pk_social_role_embodiment, date_span)


graph.functions.append(extract_social_role_embodiment)
