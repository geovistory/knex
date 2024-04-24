from ..globals import graph, params
from ..constants.ontology import *
from spacy.tokens import Doc



def extract_person(doc: Doc) -> None:

    # Focus on wanted entities
    persons_spans = list(filter(lambda ent: ent.label_ == 'PERSON', doc.ents))

    # Create wanted entities (doc._.entities)
    for span in persons_spans:

        if params.debug:
            print(f'> Person found: {span.text}')

        pk_person = graph.create_entity(class_E21_person, span=span)
        person = graph.get_entity(pk_person)
        pk_paial = graph.create_entity(class_C38_personAppellationInALanguage, text=person.label)
        pk_appellation = graph.create_entity(class_E41_appellation, text=person.label)
        graph.add_triple(pk_paial, property_P11_isAppellationForLanguageOf, pk_person)
        graph.add_triple(pk_paial, property_P13_refersToName, pk_appellation)


graph.functions.append(extract_person)
