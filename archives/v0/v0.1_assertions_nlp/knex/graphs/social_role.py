from spacy.tokens import Doc
from ..constants.ontology import classes, properties
from ..globals import graph
from ..debug import debug


def extract_social_role(doc: Doc) -> None:

    # Focus on wanted entities
    social_roles_spans = list(filter(lambda ent: ent.label_ == 'SOCIAL_ROLE', doc.ents))

    # Logs
    if debug('social_role'):
        print(f'> Social Role found: {social_roles_spans}')

    # Create social_role and there name
    for social_role_span in social_roles_spans:   
        pk_social_role = graph.create_entity(classes.C12_actorSSocialRole, span=social_role_span)
        pk_aial = graph.create_entity(classes.C11_appellationInALanguage, text=social_role_span.text)
        pk_appellation = graph.create_entity(classes.E41_appellation, text=social_role_span.text)
        graph.add_triple(pk_aial, properties.P11_isAppellationForLanguageOf, pk_social_role)
        graph.add_triple(pk_aial, properties.P13_refersToName, pk_appellation)

graph.functions.append(extract_social_role)
