from ..globals import nlp
from ..tools import add_triple, get_entity
from spacy.matcher import Matcher
from spacy.language import Language
from spacy.tokens import Span


matcher = Matcher(nlp.vocab)
patterns = [
    # PERSON be from GPE
    [{'ENT_TYPE': 'PERSON'}, {'LEMMA': 'be'}, {'LEMMA': 'from'}, {'ENT_TYPE': 'GPE'}],
    # PERSON be from GPE and GPE
    [{'ENT_TYPE': 'PERSON'}, {'LEMMA': 'be'}, {'LEMMA': 'from'}, {'ENT_TYPE': 'GPE'}, {'LEMMA': 'and'}, {'ENT_TYPE': 'GPE'}],
]
matcher.add('HAS_ORIGINS', patterns)


@Language.component('knex_origins_component')
def knex_origins_component(doc):

    matchings = matcher(doc)
    for _, start, end in matchings:
        span = doc[start:end]
        persons_names = list(filter(lambda ent: ent.label_ == "PERSON", span.ents))
        persons_names = list(map(lambda span: span.text, persons_names))
        geoplaces_names = list(filter(lambda ent: ent.label_ == "GPE", span.ents))
        geoplaces_names = list(map(lambda span: span.text, geoplaces_names))

        for person_name in persons_names:
            person = get_entity(doc, 'Person', person_name)
            for geoplace_name in geoplaces_names:
                geoplace = get_entity(doc, 'Geographical Place', geoplace_name)
                add_triple(doc, (person, 'has its origins in', geoplace))

    return doc

nlp.add_pipe('knex_origins_component')
