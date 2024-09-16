from spacy.matcher import Matcher, DependencyMatcher
from spacy.tokens import Doc
from ..constants.ontology import *
from ..globals import nlp, graph
from ..debug import debug
from .date import link_date


# If there is a pattern matcher to be added, else you can remove next part
matcher = Matcher(nlp.vocab)
matcher.add("THE_NAME", [
])


# If there is a dependency matcher to be added, else you can remove next part
matcher = DependencyMatcher(nlp.vocab)
pattern = [
]
# matcher.add("THE_NAME", [pattern])


def extract_THE_NAME(doc: Doc) -> None:

    # For the matcher
    matchings = matcher(doc)
    for match_id, start, end in matchings:

        # If we have the XXX matching
        # if nlp.vocab.strings[match_id] == '':

        # Extract NER from the span
        span = doc[start:end]
        XXX_span = list(filter(lambda ent: ent.label_ == "", span.ents))

        # Logs
        if debug('THE_NAME'):
            print(f'> THE_NAME found: {span.text} ()')

        # Build graph: nodes
        pk_XXX = graph.create_entity(classes., span=XXX_span, linked=True)

        # Build graph: edges
        graph.add_triple(pk_XXX, properties., pk_XXX)


    # For the dependency matcher
    matchings = matcher(doc)
    for match_id, indexes in matchings:

        if nlp.vocab.strings[match_id] == '':

            # Logs
            if debug('THE_NAME'):
                print(f'> THE_NAME found: ')

            # Extract info from matching 
            _span = doc[indexes[1]:indexes[1]+1]

            # Build graph: nodes
            pk_ = graph.create_entity(-1, span=_span, linked=True)

            # Build graph: entities
            graph.add_triple(-1, -1, -1)


graph.functions.append(extract_THE_NAME)
