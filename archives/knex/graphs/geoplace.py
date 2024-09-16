from spacy.tokens import Doc
from ..constants.ontology import classes, properties
from ..globals import graph
from ..debug import debug


def extract_geoplace(doc: Doc) -> None:

    # Focus on wanted entities
    geoplaces_spans = list(filter(lambda ent: ent.label_ == 'GPE', doc.ents))

    # Logs
    if debug('geoplace'):
        print(f'> Geographical place(s) found: {geoplaces_spans}')

    # Create geoplace and there name
    for geoplace_span in geoplaces_spans:
        pk_geoplace = graph.create_entity(classes.C13_geographicalPlace, span=geoplace_span)
        pk_appellation = graph.create_entity(classes.E41_appellation, text=geoplace_span.text)
        pk_paial = graph.create_entity(classes.C11_appellationInALanguage, text=geoplace_span.text)
        graph.add_triple(pk_paial, properties.P11_isAppellationForLanguageOf, pk_geoplace)
        graph.add_triple(pk_paial, properties.P13_refersToName, pk_appellation)


graph.functions.append(extract_geoplace)
