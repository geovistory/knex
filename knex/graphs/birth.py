from spacy.matcher import Matcher
from spacy.tokens import Doc
from ..constants.ontology import *
from ..globals import nlp, graph, params
from .date import link_date

matcher = Matcher(nlp.vocab)
patterns = [
    # PERSON be born in GPE
    [{'ENT_TYPE': 'PERSON'}, {'LEMMA': 'be'}, {'TEXT': 'born'}, {'LEMMA': {'IN': ['in', 'on']}}, {'ENT_TYPE': 'GPE'}],
    # PERSON be born on DATE
    [{'ENT_TYPE': 'PERSON'}, {'LEMMA': 'be'}, {'TEXT': 'born'}, {'LEMMA': {'IN': ['in', 'on']}}, {'ENT_TYPE': 'DATE'}],
    # PERSON be born on DATE in GPE
    [{'ENT_TYPE': 'PERSON'}, {'LEMMA': 'be'}, {'TEXT': 'born'}, {'LEMMA': {'IN': ['in', 'on']}}, {'ENT_TYPE': 'DATE'}, {'LEMMA': {'IN': ['in', 'on']}}, {'ENT_TYPE': 'GPE'}],
    # PERSON be born in GPE on DATE
    [{'ENT_TYPE': 'PERSON'}, {'LEMMA': 'be'}, {'TEXT': 'born'}, {'LEMMA': {'IN': ['in', 'on']}}, {'ENT_TYPE': 'GPE'}, {'LEMMA': {'IN': ['in', 'on']}}, {'ENT_TYPE': 'DATE'}],
]
matcher.add('HAS_BIRTH', patterns)


def extract_birth(doc: Doc) -> None:

    matchings = matcher(doc)
    for _, start, end in matchings:

        # Extract NER from the span
        span = doc[start:end]
        persons_spans = list(filter(lambda ent: ent.label_ == "PERSON", span.ents))
        geoplaces_spans = list(filter(lambda ent: ent.label_ == "GPE", span.ents))
        dates_spans = list(filter(lambda ent: ent.label_ == "DATE", span.ents))

        if params.debug:
            print('== Birth Extraction ==')
            print(f' --> Matching: {span.text}')
            print(f' --> Persons: {persons_spans}')
            print(f' --> Geoplaces: {geoplaces_spans}')
            print(f' --> Dates: {dates_spans}')

        # Error detection
        if len(persons_spans) != 1 or len(geoplaces_spans) > 1 or len(dates_spans) > 1:
            print(f'Impossible to parse BIRTH:')
            print(f' --> Matching: {span.text}')
            print(f' --> Persons: {persons_spans}')
            print(f' --> Geoplaces: {geoplaces_spans}')
            print(f' --> Dates: {dates_spans}')
            return doc

        # Get the Person, and link it to a Birth
        pk_person = graph.create_entity(class_E21_person, span=persons_spans[0], is_orphan=False)
        pk_birth = graph.create_entity(class_E67_birth, text=persons_spans[0].text)
        graph.add_triple(pk_birth, property_P98_broughtIntoLife, pk_person)

        # Birth took place at
        if len(geoplaces_spans) == 1:
            pk_geoplace = graph.create_entity(class_C13_geographicalPlace, span=geoplaces_spans[0], is_orphan=False)
            graph.add_triple(pk_birth, property_P6_tookPlaceAt, pk_geoplace)

        # Birth was at some time within
        if len(dates_spans) == 1:
            link_date(pk_birth, dates_spans[0])


graph.functions.append(extract_birth)