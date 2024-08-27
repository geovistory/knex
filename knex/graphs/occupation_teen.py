from spacy.matcher import Matcher
from spacy.tokens import Doc
from ..constants.ontology import *
from ..globals import nlp, graph
from ..debug import debug
from .date import link_date

matcher = Matcher(nlp.vocab)

matcher.add("occupation", [
    [{'ENT_TYPE':'PERSON'}, {'LEMMA':'hold'}, {'LEMMA':'the'}, {'LEMMA':'position'}, {'LEMMA':'of'}, {'POS':'ADJ','OP':'?'}, {'ENT_TYPE':'OCCUPATION'}, {'LEMMA':{'IN':[',','and']},'OP':'?'}, {'POS':'ADJ','OP':'?'}, {'ENT_TYPE':'OCCUPATION','OP':'?'}, {'LEMMA':{'IN':[',','and']},'OP':'?'}, {'POS':'ADJ','OP':'?'}, {'ENT_TYPE':'OCCUPATION','OP':'?'}],
    [{'ENT_TYPE':'PERSON'}, {'LEMMA':{'IN':['be','become','serve',',']}}, {'TEXT':{'IN':['a','an','as']},'OP':'?'}, {'POS':'ADJ','OP':'?'}, {'ENT_TYPE':'OCCUPATION'}, {'LEMMA':{'IN':['at','in']},'OP':'?'}, {'ENT_TYPE':'GPE','OP':'?'}, {'ENT_TYPE':'DATE','OP':'?'}, {'LEMMA':'and','OP':'?'}, {'ENT_TYPE':'DATE','OP':'?'}, {'LEMMA': '(','OP':'?'}, {'ENT_TYPE':'DATE','OP':'?'}, {'LEMMA': ')','OP':'?'},{'LEMMA':{'IN':[',','and']},'OP':'?'},{'ENT_TYPE':'GPE','OP':'?'},{'LEMMA':{'IN':[',','and']},'OP':'?'},{'ENT_TYPE':'GPE','OP':'?'},{'LEMMA':{'IN':[',','and']},'OP':'?'},{'ENT_TYPE':'GPE','OP':'?'},{'LEMMA':{'IN':[',','and']},'OP':'?'},{'ENT_TYPE':'GPE','OP':'?'}, {'LEMMA':{'IN':[',','and']},'OP':'?'}, {'ENT_TYPE':'GPE','OP':'?'}, {'LEMMA':{'IN':[',','and']},'OP':'?'}, {'ENT_TYPE':'GPE','OP':'?'}, {'LEMMA':'and','OP':'?'}, {'ENT_TYPE':'OCCUPATION','OP':'?'}],
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

graph.functions.append(extract_occupation)
