from spacy.matcher import PhraseMatcher
from spacy.language import Language
from spacy.tokens import Span, Doc
from ..main import nlp

white_list = ['catholic', 'protestant', 'chrétien']
black_list = []

matcher = PhraseMatcher(nlp.vocab, attr='LOWER')
matcher.add('RELIGION', list(nlp.pipe(white_list)))


@Language.component('ner_religion')
def ner_religion(doc: Doc) -> Doc:

    # This is a new entity label. 
    # So first, we need to remove those found as something else who could match either white or black list.
    # This is it because entities in spaCy can not have multiple labels

    # Remove all already listed and found (white and black) entities
    doc.ents = list(filter(lambda ent: ent.text.lower() not in white_list and ent.text.lower() not in black_list, doc.ents))
    # doc.ents = list(filter(lambda ent: ent.lemma_ not in white_list and ent.lemma_ not in black_list, doc.ents))

    # Add as entity all whitelisted entity
    religions = [Span(doc, start, end, label='RELIGION') for _, start, end in matcher(doc)]

    # print('== RELIGION NER ==')
    # for religion in religions:
    #     print('Religion found:', religion.text, religion.label_)
    
    # Add new entities
    doc.ents = list(doc.ents) + religions

    return doc


nlp.add_pipe('ner_religion', before='merge_entities')
