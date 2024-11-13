from spacy.matcher import Matcher
from spacy.tokens import Doc
from ..constants.ontology import classes, properties
from ..globals import nlp, graph
from ..debug import debug


matcher = Matcher(nlp.vocab)
matcher.add("sibling", [
    # PERSON be PERSON's [mother | father]
    [{'ENT_TYPE':'PERSON'}, {'LEMMA':'be'}, {'ENT_TYPE':'PERSON'}, {'LEMMA':'\'s', 'OP': '?'}, {'LEMMA': {'IN':['mother','father']}}]
])


def extract_siblings(doc: Doc) -> None:

    # For the matcher
    matchings = matcher(doc)
    for match_id, start, end in matchings:

        # If we have the parent_single matching
        if nlp.vocab.strings[match_id] == 'sibling':

            # Extract NER from the span
            # Because of how the pattern is build, there can only be single entities in the spans
            span = doc[start:end]
            person1_span = list(filter(lambda ent: ent.label_ == "PERSON", span.ents))[0]
            person2_span = list(filter(lambda ent: ent.label_ == "PERSON", span.ents))[1]

            # Logs
            if debug('sibling'):
                print(f'> Siblings found: {person1_span} (PERSON), {person2_span} (PERSON)')

            # Build graph: nodes
            pk_person1 = graph.create_entity(classes.E21_person, span=person1_span, linked=True)
            pk_person2 = graph.create_entity(classes.E21_person, span=person2_span, linked=True)
            pk_birth1 = graph.create_entity(classes.E67_birth, text=person1_span.text)
            pk_birth2 = graph.create_entity(classes.E67_birth, text=person2_span.text)
            pk_union = graph.create_entity(classes.C9_relationship, text=person1_span.text)

            # Build graph: edges
            graph.add_triple(pk_birth1, properties.P98_broughtIntoLife, pk_person1)
            graph.add_triple(pk_birth2, properties.P98_broughtIntoLife, pk_person2)
            graph.add_triple(pk_birth1, properties.P22_stemmedFrom, pk_union)
            graph.add_triple(pk_birth2, properties.P22_stemmedFrom, pk_union)


graph.functions.append(extract_siblings)
