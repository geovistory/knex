from spacy.matcher import DependencyMatcher
from spacy.tokens import Doc
from ..constants.ontology import *
from ..globals import nlp, graph, params
from .date import link_date


matcher = DependencyMatcher(nlp.vocab)
pattern = [
]
matcher.add("THE_NAME", [pattern])


def extract_THE_NAME(doc: Doc) -> None:

    matchings = matcher(doc)
    for match_id, indexes in matchings:

        # Logs
        if params.debug or 'THE_NAME' in params.debug_list:
            print(f'> ')

        pass

graph.functions.append(extract_THE_NAME)
