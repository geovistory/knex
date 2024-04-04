from ..globals import nlp
from ..tools import add_triple, get_entity
from spacy.matcher import PhraseMatcher
from spacy.language import Language
from spacy.tokens import Span

white_list = []
black_list = []

matcher = PhraseMatcher(nlp.vocab, attr='LOWER')
matcher.add('PERSON', list(nlp.pipe(white_list)))

@Language.component('knex_person_component')
def knex_person_component(doc):

    # Add whitelisted to doc.ents
    matchings = matcher(doc)
    for id, start, end in matchings:
        doc.ents = list(doc.ents) + [Span(doc, start, end, label='PERSON')]
    
    # Remove blacklisted from doc.ents
    doc.ents = list(filter(lambda span: (span.label_ != 'PERSON') or (span.label_ == 'PERSON' and span.text not in black_list), doc.ents))

    # Focus on wanted entities
    persons = list(filter(lambda ent: ent.label_ == 'PERSON', doc.ents))

    # Create wanted entities (doc._.entities)
    persons = [get_entity(doc, 'Person', ent.text) for ent in persons]

    # Expand graph (doc._.graph)
    for person in persons:
        aial = get_entity(doc, 'Person Appellation in a Language', person['name'])
        appellation = get_entity(doc, 'Value', person['name'])
        add_triple(doc, (aial, 'is appellation for language of', person))
        add_triple(doc, (aial, 'refers to name', appellation))

    return doc


nlp.add_pipe('knex_person_component')
