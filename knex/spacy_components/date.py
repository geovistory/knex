from spacy.matcher import Matcher
from spacy.language import Language
from spacy.tokens import Span, Doc
from ..main import nlp


matcher = Matcher(nlp.vocab)
patterns = [
    [{'LEMMA': {'IN':['in']}}, {'ENT_TYPE':'DATE'}],
    [{'LEMMA': {'IN':['on']}}, {'ENT_TYPE':'DATE'}],
]
matcher.add('DATE', patterns)


@Language.component('ner_date')
def ner_date(doc: Doc) -> Doc:

    # Add as entity all whitelisted entity
    matchings = matcher(doc)
    spans = []
    for _, start, end in matchings:
        
        # Create the span
        span = Span(doc, start, end, label='DATE')

        # If there was entities in the span, remove them from the doc
        doc.ents = list(filter(lambda ent: ent.end < span.start or span.end < ent.start, doc.ents))

        # Add the span to the add list
        spans.append(span)

    # Update the document entities
    doc.ents = list(doc.ents) + spans

    return doc

nlp.add_pipe('ner_date', before='merge_entities')
