from spacy.matcher import Matcher
from spacy.tokens import Doc
from ..constants.ontology import *
from ..globals import nlp, graph, params


matcher = Matcher(nlp.vocab)
patterns = [
    # PERSON be a RELIGION
    [{'ENT_TYPE':'PERSON'}, {'LEMMA':'be'}, {'TEXT':'a','OP':'?'}, {'ENT_TYPE':'RELIGION'}]
]
matcher.add('CONFESSION', patterns)


def extract_confession(doc: Doc) ->  None:

    matchings = matcher(doc)
    for _, start, end in matchings:

        # Extract NER from the span
        span = doc[start:end]
        persons_spans = list(filter(lambda ent: ent.label_ == "PERSON", span.ents))
        religions_spans = list(filter(lambda ent: ent.label_ == "RELIGION", span.ents))

        # Logs
        if params.debug or 'confession' in params.debug_list:
            print(f'> Confession found: {persons_spans[0].text} (PERSON), {religions_spans[0].text} (RELIGION)')
            
        # Religions pertains to Persons
        for person_span in persons_spans:
            pk_person = graph.create_entity(class_E21_person, span=person_span, is_orphan=False)
            for religion_span in religions_spans:
                pk_religion = graph.create_entity(class_C23_religiousIdentity, span=religion_span, is_orphan=False)
                graph.add_triple(pk_religion, property_P36_pertainsTo, pk_person)


graph.functions.append(extract_confession)