from spacy.matcher import Matcher, DependencyMatcher
from spacy.tokens import Doc
from ..constants.ontology import *
from ..globals import nlp, graph
from ..debug import debug

from .date import link_date


matcher = Matcher(nlp.vocab)
pattern_occupation = [
    # PERSON be a OCCUPATION
    [{'ENT_TYPE':'PERSON'}, {'LEMMA':'be'}, {'TEXT':'a','OP':'?'}, {'ENT_TYPE':'OCCUPATION'}]
]
pattern_occupation_gpe = [
    # PERSON be a OCCUPATION ['at', 'in'] GPE
    [{'ENT_TYPE':'PERSON'}, {'LEMMA':'be'}, {'TEXT':'a','OP':'?'}, {'ENT_TYPE':'OCCUPATION'}, {'LEMMA': {'IN': ['at', 'in']}}, {'ENT_TYPE':'GPE'}],
]
pattern_occupation_gpe_dates = [
    # PERSON be a OCCUPATION ['at', 'in'] GPE, DATE, DATE
    [{'ENT_TYPE':'PERSON'}, {'LEMMA':'be'}, {'TEXT':'a','OP':'?'}, {'ENT_TYPE':'OCCUPATION'}, {'LEMMA': {'IN': ['at', 'in']}}, {'ENT_TYPE':'GPE'}, {'ENT_TYPE':'DATE'}, {'ENT_TYPE':'DATE'}],
]

matcher.add("occupation", pattern_occupation)
matcher.add("occupation_gpe", pattern_occupation_gpe)
matcher.add("occupation_gpe_dates", pattern_occupation_gpe_dates)


def extract_occupation(doc: Doc) -> None:


    # For the matcher
    matchings = matcher(doc)
    for match_id, start, end in matchings:
        span = doc[start:end]

        # If we only have an occupation of a person
        if nlp.vocab.strings[match_id] == 'occupation':

            # Extract NER from the span
            person_span = list(filter(lambda ent: ent.label_ == "PERSON", span.ents))[0]
            occupation_span = list(filter(lambda ent: ent.label_ == "OCCUPATION", span.ents))[0]

            # Logs
            if debug('occupation'):
                print(f'> Occupation found: {person_span.text} (PERSON), {occupation_span.text} (OCCUPATION)')

            # Create graph nodes
            pk_person = graph.create_entity(classes.E21_person, span=person_span, linked=True)
            pk_occupation_teen = graph.create_entity(classes.C8_occupationTemporalEntity, text=occupation_span.text)
            pk_occupation_peit = graph.create_entity(classes.C7_occupation, span=occupation_span, linked=True)

            # Create edges
            graph.add_triple(pk_occupation_teen, properties.P4_isOccupationOf, pk_person)
            graph.add_triple(pk_occupation_teen, properties.P5_isAbout, pk_occupation_peit)


        # If we have an occupation of a person at a place
        if nlp.vocab.strings[match_id] == 'occupation_gpe':

            # Extract NER from the span
            person_span = list(filter(lambda ent: ent.label_ == "PERSON", span.ents))[0]
            occupation_span = list(filter(lambda ent: ent.label_ == "OCCUPATION", span.ents))[0]
            gpe_span = list(filter(lambda ent: ent.label_ == "GPE", span.ents))[0]

            # Logs
            if debug('occupation'):
                print(f'> Occupation found: {person_span.text} (PERSON), {occupation_span.text} (OCCUPATION), {gpe_span.text} (GPE)')

            # Create graph nodes
            pk_person = graph.create_entity(classes.E21_person, span=person_span, linked=True)
            pk_occupation_teen = graph.create_entity(classes.C8_occupationTemporalEntity, text=occupation_span.text)
            pk_occupation_peit = graph.create_entity(classes.C7_occupation, span=occupation_span, linked=True)
            pk_geoplace = graph.create_entity(classes.C13_geographicalPlace, span=gpe_span, linked=True)

            # Create edges
            graph.add_triple(pk_occupation_teen, properties.P4_isOccupationOf, pk_person)
            graph.add_triple(pk_occupation_teen, properties.P5_isAbout, pk_occupation_peit)
            graph.add_triple(pk_occupation_teen, properties.P6_takesPlaceAt, pk_geoplace)


        # If we have an occupation of a person at a place with a begin and an end date
        if nlp.vocab.strings[match_id] == 'occupation_gpe_dates':

            # Extract NER from the span
            person_span = list(filter(lambda ent: ent.label_ == "PERSON", span.ents))[0]
            occupation_span = list(filter(lambda ent: ent.label_ == "OCCUPATION", span.ents))[0]
            gpe_span = list(filter(lambda ent: ent.label_ == "GPE", span.ents))[0]
            date1_span = list(filter(lambda ent: ent.label_ == "DATE", span.ents))[0]
            date2_span = list(filter(lambda ent: ent.label_ == "DATE", span.ents))[1]

            # Logs
            if debug('occupation'):
                print(f'> Occupation found: {person_span.text} (PERSON), {occupation_span.text} (OCCUPATION), {gpe_span.text} (GPE), {date1_span} (DATE), {date2_span} (DATE)')

            # Create graph nodes
            pk_person = graph.create_entity(classes.E21_person, span=person_span, linked=True)
            pk_occupation_teen = graph.create_entity(classes.C8_occupationTemporalEntity, text=occupation_span.text)
            pk_occupation_peit = graph.create_entity(classes.C7_occupation, span=occupation_span, linked=True)
            pk_geoplace = graph.create_entity(classes.C13_geographicalPlace, span=gpe_span, linked=True)

            # Create edges
            graph.add_triple(pk_occupation_teen, properties.P4_isOccupationOf, pk_person)
            graph.add_triple(pk_occupation_teen, properties.P5_isAbout, pk_occupation_peit)
            graph.add_triple(pk_occupation_teen, properties.P6_takesPlaceAt, pk_geoplace)
            link_date(pk_occupation_teen, date1_span)
            link_date(pk_occupation_teen, date2_span)




graph.functions.append(extract_occupation)
