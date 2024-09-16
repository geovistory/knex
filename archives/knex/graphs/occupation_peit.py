from spacy.tokens import Doc
from ..constants.ontology import classes, properties
from ..globals import graph
from ..debug import debug


def extract_occupation_peit(doc: Doc) -> None:

    # Focus on wanted entities
    occupations_spans = list(filter(lambda ent: ent.label_ == 'OCCUPATION', doc.ents))

    # Logs
    if debug('occupation'):
        print(f'> Occupation(s) (PeIt) found: {occupations_spans}')

    # Create occupation and there name
    for occupation_span in occupations_spans:   
        pk_occupation = graph.create_entity(classes.C7_occupation, span=occupation_span)
        pk_aial = graph.create_entity(classes.C11_appellationInALanguage, text=occupation_span.text)
        pk_appellation = graph.create_entity(classes.E41_appellation, text=occupation_span.text)
        graph.add_triple(pk_aial, properties.P11_isAppellationForLanguageOf, pk_occupation)
        graph.add_triple(pk_aial, properties.P13_refersToName, pk_appellation)

graph.functions.append(extract_occupation_peit)
