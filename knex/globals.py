import spacy
from spacy.tokens import Span, Token
from .schema import Graph


# Extend spaCy objects
Span.set_extension('pk_entity', default=-1)
Span.set_extension('linked', default=False)
Token.set_extension('pk_entity', default=-1)
Token.set_extension('linked', default=False)


# Spacy NLP object which components list is extended in the knex/components folder
nlp = spacy.load('en_core_web_trf')
nlp.add_pipe('merge_entities')
# nlp.add_pipe('merge_noun_chunks') # Becareful: adds the "a" before a word: eg "a catholic" instead of "catholic"


# Knex graph object which contains all info needed from extrated information.
# It is extended in the knex/graphs folder
graph = Graph()


# To remove entities detected multiple times by a matcher, take the wider one: "in 2020-2024" should be prefered to "in 2020"
def take_wider_entities(entities):
    # If there is multiple entities on the same word, remove the shorter entity
    entities_to_keep = []

    for i in range(0, len(entities)):
        entity1 = entities[i]
        keep = True
        for j in range(0, len(entities)):
            if i == j: continue
            entity2 = entities[j]

            # Overlaping checking
            if entity1.start < entity2.start and entity2.start < entity1.end < entity2.end: # Other way around will be checked on other way
                # print("\nOVERLAPING CONFUSION:")
                # print('Entity 1:', entity1.text)
                # print('Entity 2:', entity2.text)
                # raise Exception('Overlaping confusion')
                keep = False
            
            # if the entity is INCLUDED in the next one, entity should not be kept
            if entity2.start <= entity1.start and entity1.end <= entity2.end:
                keep = False

        if keep: entities_to_keep.append(entity1)

    return entities_to_keep


def update_entities(doc, new_entities):

    # print('=================')
    # for ent in doc.ents: print(ent.label_, ent.text)
    # print('------')
    # for ent in new_entities: print(ent.label_, ent.text)

    self_filtered = take_wider_entities(new_entities)
    all_entities = take_wider_entities(list(doc.ents) + self_filtered)

    doc.ents = all_entities
    return doc
