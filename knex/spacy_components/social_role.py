from spacy.matcher import Matcher
from spacy.language import Language
from spacy.tokens import Span, Doc
from ..main import nlp


social_role_base = ['princess', 'queen', 'prince', 'king']

matcher = Matcher(nlp.vocab)
patterns = [
    # TITLE of GPE
    [{'TEXT': {'IN':social_role_base}}, {'LEMMA':'of'}, {'ENT_TYPE':'GPE'}]
]
matcher.add('SOCIAL_ROLE', patterns)

@Language.component('ner_social_role')
def ner_social_role(doc: Doc) -> Doc:

    # Add as entity all whitelisted entity
    matchings = matcher(doc)
    spans = []
    for _, start, end in matchings:
        
        # Create the span
        span = Span(doc, start, end, label='SOCIAL_ROLE')

        # If there was entities in the span, remove them from the doc
        doc.ents = list(filter(lambda ent: ent.end < span.start or span.end < ent.start, doc.ents))

        # Add the span to the add list
        spans.append(span)

    # Update the document entities
    doc.ents = list(doc.ents) + spans

    return doc

nlp.add_pipe('ner_social_role', before='merge_entities')
