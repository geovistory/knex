from spacy.matcher import Matcher
from spacy.tokens import Doc
from ..constants.ontology import *
from ..globals import nlp, graph, params
from .date import link_date

matcher = Matcher(nlp.vocab)
patterns = [
    # PERSON die in GPE
    [{'ENT_TYPE': 'PERSON'}, {'LEMMA': 'die'}, {'LEMMA': {'IN': ['in', 'on']}}, {'ENT_TYPE': 'GPE'}],
    # PERSON die on DATE
    [{'ENT_TYPE': 'PERSON'}, {'LEMMA': 'die'}, {'ENT_TYPE': 'DATE'}],
    # PERSON die on DATE in GPE
    [{'ENT_TYPE': 'PERSON'}, {'LEMMA': 'die'}, {'ENT_TYPE': 'DATE'}, {'LEMMA': {'IN': ['in', 'on']}}, {'ENT_TYPE': 'GPE'}],
    # PERSON die in GPE on DATE
    [{'ENT_TYPE': 'PERSON'}, {'LEMMA': 'die'}, {'LEMMA': {'IN': ['in', 'on']}}, {'ENT_TYPE': 'GPE'}, {'ENT_TYPE': 'DATE'}],
]
matcher.add('HAS_DEATH', patterns)


def extract_death(doc: Doc) -> None:

    matchings = matcher(doc)
    for _, start, end in matchings:

        # Extract NER from the span
        span = doc[start:end]
        persons_spans = list(filter(lambda ent: ent.label_ == "PERSON", span.ents))
        geoplaces_spans = list(filter(lambda ent: ent.label_ == "GPE", span.ents))
        dates_spans = list(filter(lambda ent: ent.label_ == "DATE", span.ents))

        # Error detection
        if len(persons_spans) != 1 or len(geoplaces_spans) > 1 or len(dates_spans) > 1:
            print(f'Impossible to parse DEATH:')
            print(f' --> Matching: {span.text}')
            print(f' --> Persons: {persons_spans}')
            print(f' --> Geoplaces: {geoplaces_spans}')
            print(f' --> Dates: {dates_spans}')
            return doc
        
        # Logs
        if params.debug or 'death' in params.debug_list:
            print(f'> Death found: {persons_spans[0].text} (PERSON), {geoplaces_spans[0].text if len(geoplaces_spans) > 0 else None} (GPE), {dates_spans[0].text if len(dates_spans) > 0 else None} (DATE)')

        # Get the Person, and link it to a Death
        pk_person = graph.create_entity(class_E21_person, span=persons_spans[0], is_orphan=False)
        pk_death = graph.create_entity(class_E69_death, text=persons_spans[0].text)
        graph.add_triple(pk_death, property_P100_wasDeathOf, pk_person)

        # Death took place at
        if len(geoplaces_spans) == 1:
            pk_geoplace = graph.create_entity(class_C13_geographicalPlace, span=geoplaces_spans[0], is_orphan=False)
            graph.add_triple(pk_death, property_P6_tookPlaceAt, pk_geoplace)

        # Death was at some time within
        if len(dates_spans) == 1:
            link_date(pk_death, dates_spans[0])


graph.functions.append(extract_death)