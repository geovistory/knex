from spacy.matcher import Matcher
from spacy.language import Language
from spacy.tokens import Span, Doc
from ..main import nlp
from ..globals import update_entities


matcher = Matcher(nlp.vocab)
matcher.add('DATE', [
    [{'LEMMA': {'IN':['from', 'to', 'in', 'on', 'until']}}, {'ENT_TYPE':'DATE'}],
    [{'LEMMA': 'from'}, {'ENT_TYPE':'DATE'}, {'LEMMA': 'to'}, {'ENT_TYPE':'DATE'}],
])


@Language.component('ner_date')
def ner_date(doc: Doc) -> Doc:

    # Add as entity all whitelisted entity
    dates = []
    for match_id, start, end in matcher(doc):
        # Create the span
        span = Span(doc, start, end, label='DATE')

        # Add the span to the add list
        dates.append(span)

    # Add new entities
    doc = update_entities(doc, dates)

    return doc


nlp.add_pipe('ner_date', before='merge_entities')
