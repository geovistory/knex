from spacy.matcher import PhraseMatcher
from spacy.language import Language
from spacy.tokens import Span, Doc
from ..main import nlp
from ..globals import update_entities

white_list = ['catholic', 'protestant', 'chrétien']

matcher = PhraseMatcher(nlp.vocab, attr='LOWER')
matcher.add('RELIGION', list(nlp.pipe(white_list)))

@Language.component('ner_religion')
def ner_religion(doc: Doc) -> Doc:
    
    # Add as entity all whitelisted entity
    religions = []
    for _, start, end in matcher(doc):
        # Create the span
        span = Span(doc, start, end, label='RELIGION')

        # Add the span to the add list
        religions.append(span)

    # Add new entities
    doc = update_entities(doc, religions)

    return doc


nlp.add_pipe('ner_religion', before='merge_entities')
