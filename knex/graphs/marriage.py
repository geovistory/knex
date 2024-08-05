from spacy.matcher import Matcher
from spacy.tokens import Doc
from ..constants.ontology import classes, properties
from ..globals import nlp, graph
from ..debug import debug
from .date import link_date



matcher = Matcher(nlp.vocab)
matcher.add("marriage", [
    # PERSON marry PERSON
    [{'ENT_TYPE':'PERSON'}, {'LEMMA':'marry'}, {'ENT_TYPE':'PERSON'}]
])
matcher.add("marriage_date", [
    # PERSON marry PERSON in DATE
    [{'ENT_TYPE':'PERSON'}, {'LEMMA':'marry'}, {'ENT_TYPE':'PERSON'}, {'ENT_TYPE':'DATE'}]
])

def extract_parents(doc: Doc) -> None:

    # For the matcher
    matchings = matcher(doc)
    for match_id, start, end in matchings:

        # If we have the parent_single matching
        if nlp.vocab.strings[match_id] == 'marriage':

            # Extract NER from the span
            # Because of how the pattern is build, there can only be single entities in the spans
            span = doc[start:end]
            person1_span = list(filter(lambda ent: ent.label_ == "PERSON", span.ents))[0]
            person2_span = list(filter(lambda ent: ent.label_ == "PERSON", span.ents))[1]

            # Logs
            if debug('marriage'):
                print(f'> Marriage found: {person1_span} (PERSON), {person2_span} (PERSON)')

            # Build graph: nodes
            pk_person1 = graph.create_entity(classes.E21_person, span=person1_span, linked=True)
            pk_person2 = graph.create_entity(classes.E21_person, span=person2_span, linked=True)
            pk_union = graph.create_entity(classes.C9_relationship, text=f"{person1_span.text} and {person2_span.text}")
            pk_union_type_marriage = graph.create_entity(classes.C4_socialRelationshipType, text="Marriage")

            # Build graph: edges
            graph.add_triple(pk_union, properties.P2_hasType, pk_union_type_marriage)
            graph.add_triple(pk_union, properties.P20_hadPartner, pk_person1)
            graph.add_triple(pk_union, properties.P20_hadPartner, pk_person2)


        # If we have the parent_both matching
        if nlp.vocab.strings[match_id] == 'marriage_date':

            # Extract NER from the span
            # Because of how the pattern is build, there can only be single entities in the spans
            span = doc[start:end]
            person1_span = list(filter(lambda ent: ent.label_ == "PERSON", span.ents))[0]
            person2_span = list(filter(lambda ent: ent.label_ == "PERSON", span.ents))[1]
            date_span = list(filter(lambda ent: ent.label_ == "DATE", span.ents))[0]

            # Logs
            if debug('marriage'):
                print(f'> Marriage found: {person1_span} (PERSON), {person2_span} (PERSON), {date_span} (DATE)')

            # Build graph: nodes
            pk_person1 = graph.create_entity(classes.E21_person, span=person1_span, linked=True)
            pk_person2 = graph.create_entity(classes.E21_person, span=person2_span, linked=True)
            pk_union = graph.create_entity(classes.C9_relationship, text=f"{person1_span.text} and {person2_span.text}")

            # Build graph: edges
            graph.add_triple(pk_union, properties.P2_hasType, pk_union_type_marriage)
            graph.add_triple(pk_union, properties.P20_hadPartner, pk_person1)
            graph.add_triple(pk_union, properties.P20_hadPartner, pk_person2)
            link_date(pk_union, date_span)


graph.functions.append(extract_parents)
