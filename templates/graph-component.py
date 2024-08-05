from spacy.matcher import Matcher, DependencyMatcher
from spacy.tokens import Doc
from ..constants.ontology import *
from ..globals import nlp, graph
from ..debug import debug
from .date import link_date


# If there is a pattern matcher to be added, else you can remove next part
matcher = Matcher(nlp.vocab)
patterns = [
]
matcher.add("THE_NAME", patterns)


# If there is a dependency matcher to be added, else you can remove next part
matcher = DependencyMatcher(nlp.vocab)
pattern = [
]
# matcher.add("THE_NAME", [pattern])


def extract_THE_NAME(doc: Doc) -> None:

    # For the matcher
    matchings = matcher(doc)
    for match_id, start, end in matchings:

        # Extract NER from the span
        span = doc[start:end]
        span = list(filter(lambda ent: ent.label_ == "", span.ents))

        # Logs
        if debug('THE_NAME'):
            print(f'> THE_NAME found: {span.text} ()')

        # Build graph
        for _span in span:
            pass


    # For the dependency matcher
    matchings = matcher(doc)
    for match_id, indexes in matchings:

        if nlp.vocab.strings[match_id] == '':

            # Logs
            if debug('THE_NAME'):
                print(f'> THE_NAME found: ')

            # Extract info from matching 
            _span = doc[indexes[1]:indexes[1]+1]

            # Create nodes
            pk_ = graph.create_entity(-1, span=_span, linked=True)

            # Link nodes
            graph.add_triple(-1, -1, -1)


graph.functions.append(extract_THE_NAME)
