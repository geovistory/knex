from spacy.tokens import Doc
from ..constants.ontology import classes, properties
from ..globals import graph
from ..debug import debug


def extract_person(doc: Doc) -> None:

    # Focus on wanted entities
    persons_spans = list(filter(lambda ent: ent.label_ == 'PERSON', doc.ents))

    # Logs
    if debug('person'):
        print(f'> Person(s) found: {persons_spans}')

    # Create person and there name
    for person_span in persons_spans:
        pk_person = graph.create_entity(classes.E21_person, span=person_span)
        pk_appellation = graph.create_entity(classes.E41_appellation, text=person_span.text)
        pk_paial = graph.create_entity(classes.C38_personAppellationInALanguage, text=person_span.text)
        graph.add_triple(pk_paial, properties.P11_isAppellationForLanguageOf, pk_person)
        graph.add_triple(pk_paial, properties.P13_refersToName, pk_appellation)


graph.functions.append(extract_person)
