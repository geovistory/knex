from spacy.matcher import Matcher
from spacy.tokens import Doc
from ..constants.ontology import classes, properties
from ..globals import nlp, graph
from ..debug import debug


matcher = Matcher(nlp.vocab)
matcher.add("parent_child", [
    [{'ENT_TYPE':'PERSON'}, {'LEMMA':'be'}, {'ENT_TYPE':'PERSON'}, {'LEMMA':'\'s', 'OP': '?'}, {'LEMMA': {'IN':['mother','father']}}],
    [{'ENT_TYPE':'PERSON'}, {'LEMMA':'be'}, {'LEMMA':'the'}, {'LEMMA': {'IN':['mother','father']}}, {'LEMMA':'of'}, {'ENT_TYPE':'PERSON'}]
])
matcher.add("child_parents", [
    [{'ENT_TYPE':'PERSON'}, {'LEMMA':'\'s', 'OP':'?'}, {'LEMMA': {'IN': ['mother', 'father', 'parent']}}, {'LEMMA':'be'}, {'ENT_TYPE':'PERSON'}, {'LEMMA':{'IN':[',','and']},'OP':'?'}, {'ENT_TYPE':'PERSON','OP':'?'}],
    [{'ENT_TYPE':'PERSON'}, {'LEMMA':'be'}, {'LEMMA':'the'}, {'LEMMA':{'IN':['daughter','son']}}, {'LEMMA':'of'}, {'ENT_TYPE':'PERSON'},{'LEMMA':{'IN':[',','and']},'OP':'?'}, {'ENT_TYPE':'PERSON','OP':'?'} ],
    [{'ENT_TYPE':'PERSON'}, {'LEMMA':','}, {'LEMMA':{'IN':['daughter','son']}}, {'LEMMA':'of'}, {'ENT_TYPE':'PERSON'}]
])

def extract_parents(doc: Doc) -> None:

    # For the matcher
    matchings = matcher(doc)
    for match_id, start, end in matchings:
        span = doc[start:end]

        person_spans = list(filter(lambda ent: ent.label_ == "PERSON", span.ents))

        if nlp.vocab.strings[match_id] in ['parent_child']:
            parent_spans = person_spans[0:1]
            child_spans = person_spans[1:]

        if nlp.vocab.strings[match_id] in ['child_parents']:
            child_spans = person_spans[0:1]
            parent_spans = person_spans[1:]

        if debug('parent'):
            child_str = ', '.join(map(lambda ent: ent.text + ' (CHILD)', child_spans)) + ','
            parent_str = ', '.join(map(lambda ent: ent.text + ' (PARENT)', parent_spans)) + ','
            print(f'Parenting found: {child_str} {parent_str}')

        parent_str = ' and '.join(map(lambda ent: ent.text, parent_spans))
        pk_union = graph.create_entity(classes.C9_relationship, text=parent_str)
        for parent_span in parent_spans:
            pk_parent = graph.create_entity(classes.E21_person, span=parent_span, linked=True)
            graph.add_triple(pk_union, properties.P20_hadPartner, pk_parent)

        for child_span in child_spans:
            pk_child = graph.create_entity(classes.E21_person, span=child_span, linked=True)
            pk_birth = graph.create_entity(classes.E67_birth, text=child_span.text)
            graph.add_triple(pk_birth, properties.P22_stemmedFrom, pk_union)
            graph.add_triple(pk_birth, properties.P98_broughtIntoLife, pk_child)

graph.functions.append(extract_parents)
