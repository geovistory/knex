from spacy.matcher import Matcher
from spacy.tokens import Doc
from ..constants.ontology import *
from ..globals import nlp, graph
from ..debug import debug
from .date import link_date

matcher = Matcher(nlp.vocab)

# matcher.add("1_person_N_occupations", [
#     # PERSON be [a | an] OCCUPATION
#     [{'ENT_TYPE':'PERSON'}, {'LEMMA':'be'}, {'TEXT':'a','OP':'?'}, {'TEXT':'an','OP':'?'}, {'ENT_TYPE':'OCCUPATION'}],
#     # PERSON held the position of OCCUPATION [',' | 'and'] OCCUPATION [',' | 'and'] OCCUPATION
#     [{'ENT_TYPE':'PERSON'}, {'LEMMA':'hold'}, {'LEMMA':'the'}, {'LEMMA':'position'}, {'LEMMA':'of'}, {'ENT_TYPE':'OCCUPATION'}, {'LEMMA': {'IN': [',', 'and']}, 'OP':'?'}, {'ENT_TYPE':'OCCUPATION', 'OP':'?'}, {'LEMMA': {'IN': [',', 'and']}, 'OP':'?'}, {'ENT_TYPE':'OCCUPATION', 'OP':'?'}]
# ])
# matcher.add("1_person_1_occupation_0_1_gpe_N_dates", [
#     # PERSON be [a | an] OCCUPATION ['at' | 'in'] GPE
#     [{'ENT_TYPE':'PERSON'}, {'LEMMA': {'IN': ['be', 'become']} }, {'TEXT':'a','OP':'?'}, {'TEXT':'an','OP':'?'}, {'ENT_TYPE':'TYPE','OP':'?'}, {'ENT_TYPE':'OCCUPATION'}, {'LEMMA': {'IN': ['at', 'in']}, 'OP':'?'}, {'ENT_TYPE':'GPE', 'OP':'?'}],
# ])
# matcher.add("1_person_1_occupation_1_gpe_N_dates", [
#     # PERSON be [a | an] OCCUPATION ['at', 'in'] GPE DATE [and] [DATE]
#     [{'ENT_TYPE':'PERSON'}, {'LEMMA':'be'}, {'TEXT':'a','OP':'?'}, {'TEXT':'an','OP':'?'}, {'ENT_TYPE':'OCCUPATION'}, {'LEMMA': {'IN': ['at', 'in']}}, {'ENT_TYPE':'GPE'}, {'ENT_TYPE':'DATE'}, {'LEMMA':'and','OP':'?'}, {'ENT_TYPE':'DATE','OP':'?'}],
#     # PERSON be [a | an] OCCUPATION ['at', 'in'] GPE (DATE) 
#     [{'ENT_TYPE':'PERSON'}, {'LEMMA':'be'}, {'TEXT':'a','OP':'?'}, {'TEXT':'an','OP':'?'}, {'ENT_TYPE':'OCCUPATION'}, {'LEMMA': {'IN': ['at', 'in']}}, {'ENT_TYPE':'GPE'}, {'LEMMA': '('}, {'ENT_TYPE':'DATE'}, {'LEMMA': ')'} ],
# ])
# matcher.add("1_person_1_occupation_N_dates", [
#     # PERSON become [a | an] OCCUPATION DATE
#     [{'ENT_TYPE':'PERSON'}, {'LEMMA':'become'}, {'TEXT':'a','OP':'?'}, {'TEXT':'an','OP':'?'}, {'ENT_TYPE':'OCCUPATION'}, {'ENT_TYPE':'DATE'}]
# ])


matcher.add("occupation", [
    # PERSON held the position of OCCUPATION [',' | 'and'] [OCCUPATION] [',' | 'and'] [OCCUPATION]
    [{'ENT_TYPE':'PERSON'}, {'LEMMA':'hold'}, {'LEMMA':'the'}, {'LEMMA':'position'}, {'LEMMA':'of'}, {'ENT_TYPE':'OCCUPATION'}, {'LEMMA':{'IN':[',','and']},'OP':'?'}, {'ENT_TYPE':'OCCUPATION','OP':'?'}, {'LEMMA':{'IN':[',','and']},'OP':'?'}, {'ENT_TYPE':'OCCUPATION','OP':'?'}],
    # PERSON be|become|serve [a|an|as] OCCUPATION [at|in] [GPE] [DATE] [and] [DATE] [(] [DATE] [)]
    [{'ENT_TYPE':'PERSON'}, {'LEMMA':{'IN':['be','become','serve']}}, {'TEXT':{'IN':['a','an','as']},'OP':'?'}, {'ENT_TYPE':'OCCUPATION'}, {'LEMMA':{'IN':['at','in']},'OP':'?'}, {'ENT_TYPE':'GPE','OP':'?'}, {'ENT_TYPE':'DATE','OP':'?'}, {'LEMMA':'and','OP':'?'}, {'ENT_TYPE':'DATE','OP':'?'}, {'LEMMA': '(','OP':'?'}, {'ENT_TYPE':'DATE','OP':'?'}, {'LEMMA': ')','OP':'?'}],
])


def extract_occupation(doc: Doc) -> None:

    # For the matcher
    matchings = matcher(doc)
    for match_id, start, end in matchings:
        span = doc[start:end]

        person_spans = list(filter(lambda ent: ent.label_ == "PERSON", span.ents))
        occupation_spans = list(filter(lambda ent: ent.label_ == "OCCUPATION", span.ents))
        gpe_spans = list(filter(lambda ent: ent.label_ == "GPE", span.ents))
        date_spans = list(filter(lambda ent: ent.label_ == "DATE", span.ents))

        if debug('occupation'):
            person_str = ', '.join(map(lambda ent: ent.text + ' (PERSON)', person_spans)) + ','
            occupation_str = ', '.join(map(lambda ent: ent.text + ' (OCCUPATION)', occupation_spans)) + ','
            gpe_str = ', '.join(map(lambda ent: ent.text + ' (GPE)', gpe_spans)) + ','
            date_str = ', '.join(map(lambda ent: ent.text + ' (DATE)', date_spans)) + ','
            print(f'> Occupation (TeEn) found: {person_str} {occupation_str} {gpe_str} {date_str}'[:-1])

        pks_person = list(map(lambda span: graph.create_entity(classes.E21_person, span=span, linked=True), person_spans))
        pks_occupations_peit = list(map(lambda span: graph.create_entity(classes.C7_occupation, span=span, linked=True), occupation_spans))
        pks_occupations_teen = list(map(lambda span: graph.create_entity(classes.C8_occupationTemporalEntity, text=span.text), occupation_spans))
        pks_gpe = list(map(lambda span: graph.create_entity(classes.C13_geographicalPlace, span=span, linked=True), gpe_spans))

        for pk_person in pks_person:
            for i, occupation_span in enumerate(occupation_spans):
                pk_occupation_peit = pks_occupations_peit[i]
                pk_occupation_teen = pks_occupations_teen[i]

                graph.add_triple(pk_occupation_teen, properties.P4_isOccupationOf, pk_person)
                graph.add_triple(pk_occupation_teen, properties.P5_isAbout, pk_occupation_peit)

                for pk_gpe in pks_gpe:
                    graph.add_triple(pk_occupation_teen, properties.P6_takesPlaceAt, pk_gpe)

                for date_span in date_spans:
                    link_date(pk_occupation_teen, date_span)


        # # If we only have an occupation of a person
        # if nlp.vocab.strings[match_id] == '1_person_N_occupations':

        #     # Extract NER from the span
        #     person_span = list(filter(lambda ent: ent.label_ == "PERSON", span.ents))[0]
        #     occupation_spans = list(filter(lambda ent: ent.label_ == "OCCUPATION", span.ents))

        #     # Logs
        #     if debug('occupation'):
        #         occupations_string = ', '.join(map(lambda occ: occ.text + ' (OCCUPATION)', occupation_spans))
        #         print(f'> Occupation (TeEn) found: {person_span.text} (PERSON), {occupations_string}')

        #     # Create graph nodes
        #     pk_person = graph.create_entity(classes.E21_person, span=person_span, linked=True)
        #     for span in occupation_spans:
        #         pk_occupation_teen = graph.create_entity(classes.C8_occupationTemporalEntity, text=span.text)
        #         pk_occupation_peit = graph.create_entity(classes.C7_occupation, span=span, linked=True)

        #         # Create edges
        #         graph.add_triple(pk_occupation_teen, properties.P4_isOccupationOf, pk_person)
        #         graph.add_triple(pk_occupation_teen, properties.P5_isAbout, pk_occupation_peit)


        # # If we have an occupation of a person at a place
        # if nlp.vocab.strings[match_id] == '1_person_1_occupation_1_gpe':

        #     # Extract NER from the span
        #     person_span = list(filter(lambda ent: ent.label_ == "PERSON", span.ents))[0]
        #     occupation_span = list(filter(lambda ent: ent.label_ == "OCCUPATION", span.ents))[0]
        #     gpe_span = list(filter(lambda ent: ent.label_ == "GPE", span.ents))[0]

        #     # Logs
        #     if debug('occupation'):
        #         print(f'> Occupation (TeEn) found: {person_span.text} (PERSON), {occupation_span.text} (OCCUPATION), {gpe_span.text} (GPE)')

        #     # Create graph nodes
        #     pk_person = graph.create_entity(classes.E21_person, span=person_span, linked=True)
        #     pk_occupation_teen = graph.create_entity(classes.C8_occupationTemporalEntity, text=occupation_span.text)
        #     pk_occupation_peit = graph.create_entity(classes.C7_occupation, span=occupation_span, linked=True)
        #     pk_geoplace = graph.create_entity(classes.C13_geographicalPlace, span=gpe_span, linked=True)

        #     # Create edges
        #     graph.add_triple(pk_occupation_teen, properties.P4_isOccupationOf, pk_person)
        #     graph.add_triple(pk_occupation_teen, properties.P5_isAbout, pk_occupation_peit)
        #     graph.add_triple(pk_occupation_teen, properties.P6_takesPlaceAt, pk_geoplace)


        # # If we have an occupation of a person at a place with a begin and an end date
        # if nlp.vocab.strings[match_id] == '1_person_1_occupation_1_gpe_N_dates':

        #     # Extract NER from the span
        #     person_span = list(filter(lambda ent: ent.label_ == "PERSON", span.ents))[0]
        #     occupation_span = list(filter(lambda ent: ent.label_ == "OCCUPATION", span.ents))[0]
        #     gpe_span = list(filter(lambda ent: ent.label_ == "GPE", span.ents))[0]
        #     date_spans = list(filter(lambda ent: ent.label_ == "DATE", span.ents))

        #     # Logs
        #     if debug('occupation'):
        #         date_str = ', '.join(list(map(lambda span: span.text + ' (DATE)', date_spans)))
        #         print(f'> Occupation (TeEn) found: {person_span.text} (PERSON), {occupation_span.text} (OCCUPATION), {gpe_span.text} (GPE), {date_str}')

        #     # Create graph nodes
        #     pk_person = graph.create_entity(classes.E21_person, span=person_span, linked=True)
        #     pk_occupation_teen = graph.create_entity(classes.C8_occupationTemporalEntity, text=occupation_span.text)
        #     pk_occupation_peit = graph.create_entity(classes.C7_occupation, span=occupation_span, linked=True)
        #     pk_geoplace = graph.create_entity(classes.C13_geographicalPlace, span=gpe_span, linked=True)

        #     # Create edges
        #     graph.add_triple(pk_occupation_teen, properties.P4_isOccupationOf, pk_person)
        #     graph.add_triple(pk_occupation_teen, properties.P5_isAbout, pk_occupation_peit)
        #     graph.add_triple(pk_occupation_teen, properties.P6_takesPlaceAt, pk_geoplace)
        #     for date_span in date_spans:
        #         link_date(pk_occupation_teen, date_span)


        # # If we have an occupation of a person at a place with a begin and an end date
        # if nlp.vocab.strings[match_id] == '1_person_1_occupation_N_dates':

        #     # Extract NER from the span
        #     person_span = list(filter(lambda ent: ent.label_ == "PERSON", span.ents))[0]
        #     occupation_span = list(filter(lambda ent: ent.label_ == "OCCUPATION", span.ents))[0]
        #     date_spans = list(filter(lambda ent: ent.label_ == "DATE", span.ents))

        #     # Logs
        #     if debug('occupation'):
        #         date_str = ', '.join(list(map(lambda span: span.text + ' (DATE)', date_spans)))
        #         print(f'> Occupation (TeEn) found: {person_span.text} (PERSON), {occupation_span.text} (OCCUPATION), {date_str}')

        #     # Create graph nodes
        #     pk_person = graph.create_entity(classes.E21_person, span=person_span, linked=True)
        #     pk_occupation_teen = graph.create_entity(classes.C8_occupationTemporalEntity, text=occupation_span.text)
        #     pk_occupation_peit = graph.create_entity(classes.C7_occupation, span=occupation_span, linked=True)

        #     # Create edges
        #     graph.add_triple(pk_occupation_teen, properties.P4_isOccupationOf, pk_person)
        #     graph.add_triple(pk_occupation_teen, properties.P5_isAbout, pk_occupation_peit)
        #     for date_span in date_spans:
        #         link_date(pk_occupation_teen, date_span)


graph.functions.append(extract_occupation)
