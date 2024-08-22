from spacy.matcher import PhraseMatcher
from spacy.language import Language
from spacy.tokens import Span, Doc
from ..main import nlp
from ..white_lists import social_role_white_list as white_list
from ..globals import update_entities


matcher = PhraseMatcher(nlp.vocab, attr='LOWER')
matcher.add('SOCIAL_ROLE', list(nlp.pipe(white_list)))


@Language.component('ner_social_role')
def ner_social_role(doc: Doc) -> Doc:

    # Add as entity all whitelisted entity
    social_roles = []
    for _, start, end in matcher(doc):
        # Create the span
        span = Span(doc, start, end, label='SOCIAL_ROLE')

        # Add the span to the add list
        social_roles.append(span)

    # Add new entities
    doc = update_entities(doc, social_roles)

    return doc

nlp.add_pipe('ner_social_role', before='merge_entities')
