from spacy.matcher import DependencyMatcher
from spacy.tokens import Doc
from ..constants.ontology import *
from ..globals import nlp, graph, params
from .date import link_date


matcher = DependencyMatcher(nlp.vocab)
pattern = [
]
matcher.add("profession", [pattern])


def extract_profession(doc):

    matchings = matcher(doc)
    for match_id, indexes in matchings:
        pass

graph.functions.append(extract_profession)
