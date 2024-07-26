from spacy.matcher import PhraseMatcher
from spacy.language import Language
from spacy.tokens import Span, Doc
from ..main import nlp

white_list = []
black_list = []

matcher = PhraseMatcher(nlp.vocab, attr='LOWER')
matcher.add('PERSON', list(nlp.pipe(white_list)))

@Language.component('ner_person')
def ner_person(doc: Doc) -> Doc:

    # Add whitelisted to doc.ents
    matchings = matcher(doc)
    for id, start, end in matchings:
        doc.ents = list(doc.ents) + [Span(doc, start, end, label='PERSON')]

    # Remove blacklisted from doc.ents
    new_ents = []
    for ent in list(doc.ents):
        if ent.label_ == 'PERSON' and ent.text in black_list: continue
        else: new_ents.append(ent)
    
    # Add new entities
    doc.ents = new_ents

    return doc


nlp.add_pipe('ner_person', before='merge_entities')
