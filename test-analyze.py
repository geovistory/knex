import sys
import spacy

nlp = spacy.load('en_core_web_trf')
nlp.add_pipe('merge_entities')
nlp.add_pipe('merge_noun_chunks')

string = sys.argv[1]

print("===== Original =====")
print(string)
doc = nlp(string)

for ent in doc.ents:
    if ent.label_ == 'GPE': ent.label_ = "Geoplace"

print("\n===== Tokens =====")
for token in doc:
    print(f"{token.text} => LEMMA: {token.lemma_} |  POS: {token.pos_} | DEP: {token.dep_} | HEAD: {token.head}")
print("\n===== Entities =====")
for ent in doc.ents:
    print(ent.text, ent.label_)