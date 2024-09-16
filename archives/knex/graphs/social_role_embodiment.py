from spacy.matcher import Matcher
from spacy.tokens import Doc
from ..constants.ontology import *
from ..globals import nlp, graph
from ..debug import debug
from .date import link_date

matcher = Matcher(nlp.vocab)


matcher.add("social_role", [
    [{'ENT_TYPE':'PERSON'}, {'LEMMA':'hold'}, {'LEMMA':'the'}, {'LEMMA':'position'}, {'LEMMA':'of'}, {'POS':'ADJ','OP':'?'}, {'ENT_TYPE':'SOCIAL_ROLE'}, {'LEMMA':{'IN':[',','and']},'OP':'?'}, {'POS':'ADJ','OP':'?'}, {'ENT_TYPE':'SOCIAL_ROLE','OP':'?'}, {'LEMMA':{'IN':[',','and']},'OP':'?'}, {'POS':'ADJ','OP':'?'}, {'ENT_TYPE':'SOCIAL_ROLE','OP':'?'}],
    [{'ENT_TYPE':'PERSON'}, {'LEMMA':{'IN':['be','become','serve']}}, {'TEXT':{'IN':['a','an','as']},'OP':'?'}, {'POS':'ADJ','OP':'?'}, {'ENT_TYPE':'SOCIAL_ROLE'}, {'LEMMA':{'IN':['at','in']},'OP':'?'}, {'ENT_TYPE':'GPE','OP':'?'}, {'ENT_TYPE':'DATE','OP':'?'}, {'LEMMA':'and','OP':'?'}, {'ENT_TYPE':'DATE','OP':'?'}, {'LEMMA': '(','OP':'?'}, {'ENT_TYPE':'DATE','OP':'?'}, {'LEMMA': ')','OP':'?'}],
])


def extract_social_role(doc: Doc) -> None:

    # For the matcher
    matchings = matcher(doc)
    for match_id, start, end in matchings:
        span = doc[start:end]

        person_spans = list(filter(lambda ent: ent.label_ == "PERSON", span.ents))
        social_role_spans = list(filter(lambda ent: ent.label_ == "SOCIAL_ROLE", span.ents))
        gpe_spans = list(filter(lambda ent: ent.label_ == "GPE", span.ents))
        date_spans = list(filter(lambda ent: ent.label_ == "DATE", span.ents))

        if debug('social_role'):
            person_str = ', '.join(map(lambda ent: ent.text + ' (PERSON)', person_spans)) + ','
            social_role_str = ', '.join(map(lambda ent: ent.text + ' (SOCIAL_ROLE)', social_role_spans)) + ','
            gpe_str = ', '.join(map(lambda ent: ent.text + ' (GPE)', gpe_spans)) + ','
            date_str = ', '.join(map(lambda ent: ent.text + ' (DATE)', date_spans)) + ','
            print(f'> Social Role Embodiment found: {person_str} {social_role_str} {gpe_str} {date_str}'[:-1])

        pks_person = list(map(lambda span: graph.create_entity(classes.E21_person, span=span, linked=True), person_spans))
        pks_social_role = list(map(lambda span: graph.create_entity(classes.C12_actorSSocialRole, span=span, linked=True), social_role_spans))
        pks_social_role_embodiment = list(map(lambda span: graph.create_entity(classes.C13_socialRoleEmbodiment, text=span.text), social_role_spans))
        pks_gpe = list(map(lambda span: graph.create_entity(classes.C13_geographicalPlace, span=span, linked=True), gpe_spans))

        for pk_person in pks_person:
            for i, social_role_span in enumerate(social_role_spans):
                pk_social_role = pks_social_role[i]
                pk_social_role_embodiment = pks_social_role_embodiment[i]

                graph.add_triple(pk_social_role_embodiment, properties.P4_isOccupationOf, pk_person)
                graph.add_triple(pk_social_role_embodiment, properties.P5_isAbout, pk_social_role)

                for pk_gpe in pks_gpe:
                    graph.add_triple(pk_social_role_embodiment, properties.P6_takesPlaceAt, pk_gpe)

                for date_span in date_spans:
                    link_date(pk_social_role_embodiment, date_span)

graph.functions.append(extract_social_role)
