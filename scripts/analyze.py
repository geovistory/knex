import sys
from knex import nlp

string = sys.argv[1]

print("\n\033[1m===== Original =====\033[0m")
print(string)


doc = nlp(string)
token_len = 0
lemma_len = 0
pos_len = 0
dep_len = 0
head_len = 0
for token in doc:
    if len(token.text) > token_len: token_len = len(token.text)
    if len(token.lemma_) > lemma_len: lemma_len = len(token.lemma_)
    if len(token.pos_) > pos_len: pos_len = len(token.pos_)
    if len(token.dep_) > dep_len: dep_len = len(token.dep_)
    if len(token.head.text) > head_len: head_len = len(token.head.text)


print("\n\033[1m===== Tokens =====\033[0m")
for token in doc:
    print(f"{token.text.rjust(token_len)} =>  LEMMA: {token.lemma_.ljust(lemma_len)}   POS: {token.pos_.ljust(pos_len)}   DEP: {token.dep_.ljust(dep_len)}   HEAD: {token.head.text.ljust(head_len)}")


print("\n\033[1m===== Entities =====\033[0m")
for token in doc.ents:
    print(token.text.rjust(token_len), token.label_)