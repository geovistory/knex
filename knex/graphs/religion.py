from spacy.tokens import Doc
from ..constants.ontology import *
from ..globals import graph
from ..debug import debug


def extract_religion(doc: Doc) -> None:

    # Focus on wanted entities
    religions_spans = list(filter(lambda ent: ent.label_ == 'RELIGION', doc.ents))

    # Logs
    if debug('religion'):
        print(f'> Religion(s) found: {religions_spans}')

    # Create person and there name
    for religion_span in religions_spans:
        pk_religion = graph.create_entity(class_C23_religiousIdentity, span=religion_span)
        pk_appellation = graph.create_entity(class_E41_appellation, text=religion_span.text)
        pk_aial = graph.create_entity(class_C11_appellationInALanguage, text=religion_span.text)
        graph.add_triple(pk_aial, property_P11_isAppellationForLanguageOf, pk_religion)
        graph.add_triple(pk_aial, property_P13_refersToName, pk_appellation)


graph.functions.append(extract_religion)
