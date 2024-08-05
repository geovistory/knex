from spacy.matcher import Matcher
from spacy.tokens import Doc
from ..constants.ontology import classes, properties
from ..globals import nlp, graph
from ..debug import debug


matcher = Matcher(nlp.vocab)
matcher.add("parent_single", [
    # PERSON be PERSON's [mother | father]
    [{'ENT_TYPE':'PERSON'}, {'LEMMA':'be'}, {'ENT_TYPE':'PERSON'}, {'LEMMA':'\'s'}, {'LEMMA': {'IN': ['mother', 'father']}}]
])
matcher.add("parent_both", [
    # PERSON be PERSON's [mother | father]
    [{'ENT_TYPE':'PERSON'}, {'LEMMA':'\s', 'OP': '?'}, {'LEMMA':'parent'}, {'LEMMA':'be'}, {'ENT_TYPE':'PERSON'}, {'LEMMA':'and'}, {'ENT_TYPE':'PERSON'}]
])


def extract_parents(doc: Doc) -> None:

    # For the matcher
    matchings = matcher(doc)
    for match_id, start, end in matchings:

        # If we have the parent_single matching
        if nlp.vocab.strings[match_id] == 'parent_single':

            # Extract NER from the span
            # Because of how the pattern is build, there can only be single entities in the spans
            span = doc[start:end]
            child_span = list(filter(lambda ent: ent.label_ == "PERSON", span.ents))[0]
            parent1_span = list(filter(lambda ent: ent.label_ == "PERSON", span.ents))[1]

            # Logs
            if debug('parent'):
                print(f'> Parenting found: {child_span} (PERSON, parent), {parent1_span} (PERSON, child)')

            # Build graph: nodes
            pk_child = graph.create_entity(classes.E21_person, span=child_span, linked=True)
            pk_parent1 = graph.create_entity(classes.E21_person, span=parent1_span, linked=True)
            pk_birth = graph.create_entity(classes.E67_birth, text=parent1_span.text)
            pk_union = graph.create_entity(classes.C9_relationship, text=child_span.text)

            # Build graph: edges
            graph.add_triple(pk_birth, properties.P98_broughtIntoLife, pk_parent1)
            graph.add_triple(pk_birth, properties.P22_stemmedFrom, pk_union)
            graph.add_triple(pk_union, properties.P20_hadPartner, pk_child)


        # If we have the parent_both matching
        if nlp.vocab.strings[match_id] == 'parent_both':

            # Extract NER from the span
            # Because of how the pattern is build, there can only be single entities in the spans
            span = doc[start:end]
            child_span = list(filter(lambda ent: ent.label_ == "PERSON", span.ents))[0]
            parent1_span = list(filter(lambda ent: ent.label_ == "PERSON", span.ents))[1]
            parent2_span = list(filter(lambda ent: ent.label_ == "PERSON", span.ents))[2]

            # Logs
            if debug('parent'):
                print(f'> Parenting found: {child_span} (PERSON, child), {parent1_span} (PERSON, parent), {parent2_span} (PERSON, parent)')

            # Build graph: nodes
            pk_child = graph.create_entity(classes.E21_person, span=child_span, linked=True)
            pk_parent1 = graph.create_entity(classes.E21_person, span=parent1_span, linked=True)
            pk_parent2 = graph.create_entity(classes.E21_person, span=parent2_span, linked=True)
            pk_birth = graph.create_entity(classes.E67_birth, text=child_span.text)
            pk_union = graph.create_entity(classes.C9_relationship, text=f'{parent1_span} and {parent2_span}')

            # Build graph: edges
            graph.add_triple(pk_birth, properties.P98_broughtIntoLife, pk_child)
            graph.add_triple(pk_birth, properties.P22_stemmedFrom, pk_union)
            graph.add_triple(pk_union, properties.P20_hadPartner, pk_parent1)
            graph.add_triple(pk_union, properties.P20_hadPartner, pk_parent2)


graph.functions.append(extract_parents)
