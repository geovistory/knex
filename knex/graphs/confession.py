from spacy.matcher import Matcher
from spacy.tokens import Doc
from ..constants.ontology import *
from ..globals import nlp, graph
from ..debug import debug


matcher = Matcher(nlp.vocab)
patterns = [
    # PERSON be a RELIGION
    [{'ENT_TYPE':'PERSON'}, {'LEMMA':'be'}, {'TEXT':'a','OP':'?'}, {'ENT_TYPE':'RELIGION'}]
]
matcher.add("confession", patterns)


def extract_confession(doc: Doc) -> None:

    # For the matcher
    matchings = matcher(doc)
    for _, start, end in matchings:

        # Extract NER from the span
        # Because of how the pattern is build, there can only be single entities in the spans
        span = doc[start:end]
        person_span = list(filter(lambda ent: ent.label_ == "PERSON", span.ents))[0]
        religion_span = list(filter(lambda ent: ent.label_ == "RELIGION", span.ents))[0]

        # Logs
        if debug('confession'):
            print(f'> Confession found: {person_span} (PERSON), {religion_span} (RELIGION)')

        # Build graph
        pk_person = graph.create_entity(class_E21_person, span=person_span, linked=True)
        pk_religion = graph.create_entity(class_C23_religiousIdentity, span=religion_span, linked=True)
        graph.add_triple(pk_religion, property_P36_pertainsTo, pk_person)


graph.functions.append(extract_confession)
