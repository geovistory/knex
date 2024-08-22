from spacy.matcher import PhraseMatcher
from spacy.language import Language
from spacy.tokens import Span, Doc
from ..main import nlp
from ..white_lists import occupations_white_list as white_list
from ..globals import update_entities


matcher = PhraseMatcher(nlp.vocab, attr='LOWER')
matcher.add('OCCUPATION', list(nlp.pipe(white_list)))


@Language.component('ner_occupation')
def ner_occupation(doc: Doc) -> Doc:

    # Add as entity all whitelisted entity
    occupations = []
    for _, start, end in matcher(doc):
        # Create the span
        span = Span(doc, start, end, label='OCCUPATION')

        # Add the span to the add list
        occupations.append(span)

    # Add new entities
    doc = update_entities(doc, occupations)

    return doc


nlp.add_pipe('ner_occupation', before='merge_entities')
