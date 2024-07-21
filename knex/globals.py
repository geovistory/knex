import spacy
from spacy.tokens import Span, Token
from .schema import Graph


# Extend spaCy objects
Span.set_extension('pk_entity', default=-1)
Span.set_extension('linked', default=False)
Token.set_extension('pk_entity', default=-1)
Token.set_extension('linked', default=False)


# Spacy NLP object which components list is extended in the knex/components folder
nlp = spacy.load('en_core_web_trf')
nlp.add_pipe('merge_entities')
nlp.add_pipe('merge_noun_chunks')


# Knex graph object which contains all info needed from extrated information.
# It is extended in the knex/graphs folder
graph = Graph()