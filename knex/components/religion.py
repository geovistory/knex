from ..globals import nlp
from ..tools import add_triple, get_entity
from spacy.matcher import PhraseMatcher, Matcher
from spacy.language import Language
from spacy.tokens import Span

white_list = ['catholic', 'protestant']
black_list = []

entity_matcher = PhraseMatcher(nlp.vocab, attr='LOWER')
entity_matcher.add('RELIGION', list(nlp.pipe(white_list)))

pattern_matcher = Matcher(nlp.vocab)
patterns = [

]
pattern_matcher.add('HAS_RELIGION', patterns)

@Language.component('knex_religion_component')
def knex_religion_component(doc):

    # Remove all already listed and found (white and black) entities
    doc.ents = list(filter(lambda ent: ent.text.lower() not in white_list and ent.text.lower() not in black_list, doc.ents))

    # Add as entity all whitelisted entity
    religions = [Span(doc, start, end, label='RELIGION') for _, start, end in entity_matcher(doc)]
    doc.ents = list(doc.ents) + religions

    return doc


nlp.add_pipe('knex_religion_component')
