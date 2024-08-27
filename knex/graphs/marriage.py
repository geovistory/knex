from spacy.matcher import Matcher
from spacy.tokens import Doc
from ..constants.ontology import classes, properties
from ..globals import nlp, graph
from ..debug import debug
from .date import link_date



matcher = Matcher(nlp.vocab)

matcher.add('marriage', [
    [{'ENT_TYPE':'PERSON'}, {'LEMMA':'marry'}, {'ENT_TYPE':'PERSON'}, {'ENT_TYPE':'DATE','OP':'?'}],
    [{'ENT_TYPE':'PERSON'}, {'LEMMA':'be'}, {'ENT_TYPE':'PERSON'}, {'LEMMA':"'",'OP':'?'}, {'LEMMA':"s",'OP':'?'}, {'LEMMA':{'IN':["wife",'husband']},'OP':'?'}],
])

def extract_parents(doc: Doc) -> None:

    # For the matcher
    matchings = matcher(doc)
    for match_id, start, end in matchings:
        span = doc[start:end]

        person_spans = list(filter(lambda ent: ent.label_ == "PERSON", span.ents))
        date_spans = list(filter(lambda ent: ent.label_ == "DATE", span.ents))

        # Logs
        if debug('marriage'):
            person_str = ', '.join(map(lambda ent: ent.text + ' (PERSON)', person_spans)) + ','
            date_str = ', '.join(map(lambda ent: ent.text + ' (DATE)', date_spans)) + ','
            print(f'> Marriage found: {person_str} {date_str}'[:-1])

        pks_person = list(map(lambda span: graph.create_entity(classes.E21_person, span=span, linked=True), person_spans))
        pk_union = graph.create_entity(classes.C9_relationship, text=' and '.join(list(map(lambda span: span.text, person_spans))))
        pk_union_type_marriage = graph.create_entity(classes.C4_socialRelationshipType, text="Marriage")

        graph.add_triple(pk_union, properties.P2_hasType, pk_union_type_marriage)
        for pk_person in pks_person:
            graph.add_triple(pk_union, properties.P20_hadPartner, pk_person)
        for date_span in date_spans:
            link_date(pk_union, date_span)

graph.functions.append(extract_parents)
