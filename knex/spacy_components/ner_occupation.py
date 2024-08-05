from spacy.matcher import PhraseMatcher
from spacy.language import Language
from spacy.tokens import Span, Doc
from ..main import nlp
from ..white_lists import occupations_white_list as white_list

black_list = []

matcher = PhraseMatcher(nlp.vocab, attr='LOWER')
matcher.add('OCCUPATION', list(nlp.pipe(white_list)))


@Language.component('ner_occupation')
def ner_occupation(doc: Doc) -> Doc:

    # This is a new entity label. 
    # So first, we need to remove those found as something else who could match either white or black list.
    # This is it because entities in spaCy can not have multiple labels

    # Remove all already listed and found (white and black) entities
    doc.ents = list(filter(lambda ent: ent.text.lower() not in white_list and ent.text.lower() not in black_list, doc.ents))
    # doc.ents = list(filter(lambda ent: ent.lemma_ not in white_list and ent.lemma_ not in black_list, doc.ents))

    # Add as entity all whitelisted entity
    occupations = [Span(doc, start, end, label='OCCUPATION') for _, start, end in matcher(doc)]

    # Add new entities
    doc.ents = list(doc.ents) + occupations


    return doc


nlp.add_pipe('ner_occupation', before='merge_entities')
