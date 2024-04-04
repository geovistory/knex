from ..globals import nlp
from ..tools import add_triple, get_entity
from spacy.matcher import PhraseMatcher
from spacy.language import Language
from spacy.tokens import Span

white_list = []
black_list = []

matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
matcher.add('GPE', list(nlp.pipe(white_list)))

@Language.component('knex_geoplace_component')
def knex_geoplace_component(doc):

    # Add whitelisted to doc.ents
    matchings = matcher(doc)
    for id, start, end in matchings:
        doc.ents = list(doc.ents) + [Span(doc, start, end, label='GPE')]
    
    # Remove blacklisted from doc.ents
    doc.ents = list(filter(lambda span: (span.label_ != 'GPE') or (span.label_ == 'GPE' and span.text not in black_list), doc.ents))

    # Focus on wanted entities
    geoplaces = list(filter(lambda ent: ent.label_ == 'GPE', doc.ents))

    # Create wanted entities (doc._.entities)
    geoplaces = [get_entity(doc, 'Geographical Place', ent.text) for ent in geoplaces]

    # Expand graph (doc._.graph)
    for geoplace in geoplaces:
        aial = get_entity(doc, 'Appellation in a Language', geoplace['name'])
        appellation = get_entity(doc, 'Value', geoplace['name'])
        add_triple(doc, (aial, 'is appellation for language of', geoplace))
        add_triple(doc, (aial, 'refers to name', appellation))

    return doc


nlp.add_pipe('knex_geoplace_component')
