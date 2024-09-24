from ...extraction import Person
from ..graph import Graph
from ..ontology import properties, classes

def parse_person(person: Person, graph: Graph):
    """
    Transform an object instance into a list of entities and statements.
    """

    # If the person does not have a name, set a default value
    if not person.name:
        person.name = "Unknown Person " + str(graph.get_current_index())

    # Create the person
    person_ent = graph.create_entity(classes.E21_person, person.name)

    # Name
    if person.name:
        paiail = graph.create_entity(pk_class=classes.C38_personAppellationInALanguage, label=person.name)
        appe = graph.create_entity(pk_class=classes.E41_appellation, label=person.name)
        graph.create_triple(paiail, properties.P11_isAppellationForLanguageOf, person_ent)
        graph.create_triple(paiail, properties.P13_refersToName, appe)

    # Gender
    if person.gender:
        gender = graph.create_entity_aial(classes.C11_gender, person.gender)
        graph.create_triple(person_ent, properties.P23_hasGender, gender)

    # Origins
    if person.origins:
        geoplace = graph.create_entity_aial(classes.C13_geographicalPlace, person.origins)
        graph.create_triple(person_ent, properties.P24_hasItsOriginsIn, geoplace)

    # Religion
    if person.religion:
        religious_identity = graph.create_entity_aial(classes.C23_religiousIdentity, person.religion)
        graph.create_triple(religious_identity, properties.P36_pertainsTo, person_ent)

    # Birth date
    if person.birth_date:
        birth = graph.create_entity(classes.E67_birth, person.name)
        date = graph.create_entity(classes.E61_timePrimitive, person.birth_date)
        graph.create_triple(birth, properties.P98_broughtIntoLife, person_ent)
        graph.create_triple(birth, properties.P82_atSomeTimeWithin, date)

    # Birth place
    if person.birth_place:
        geoplace = graph.create_entity_aial(classes.C13_geographicalPlace, person.birth_place)
        birth = graph.create_entity(classes.E67_birth, person.name)
        graph.create_triple(birth, properties.P98_broughtIntoLife, person_ent)
        graph.create_triple(birth, properties.P8_tookPlaceOnOrWithin, geoplace)

    # Death date
    if person.death_date:
        death = graph.create_entity(classes.E69_death, person.name)
        date = graph.create_entity(classes.E61_timePrimitive, person.death_date)
        graph.create_triple(death, properties.P100_wasDeathOf, person_ent)
        graph.create_triple(death, properties.P82_atSomeTimeWithin, date)

    # Death place
    if person.death_place:
        geoplace = graph.create_entity_aial(classes.C13_geographicalPlace, person.death_place)
        death = graph.create_entity(classes.E69_death, person.name)
        graph.create_triple(death, properties.P100_wasDeathOf, person_ent)
        graph.create_triple(death, properties.P8_tookPlaceOnOrWithin, geoplace)


    # Parents
    if person.father_name or person.mother_name:
        # Unions names are ordered alphabetically so that there label match
        union_name = [person.father_name or "Unknown", person.mother_name or "Unknown"]
        union_name.sort()
        union_name = ' and '.join(union_name)
        union = graph.create_entity(classes.C9_relationship, union_name)
        # Create parents
        if person.father_name:
            father_ent = graph.create_entity_aial(classes.E21_person, person.father_name)
            graph.create_triple(union, properties.P20_hadPartner, father_ent)
        if person.mother_name:
            mother_ent = graph.create_entity_aial(classes.E21_person, person.mother_name)
            graph.create_triple(union, properties.P20_hadPartner, mother_ent)
        # Create the birth, and link it to the union
        birth = graph.create_entity(classes.E67_birth, person.name)
        graph.create_triple(birth, properties.P98_broughtIntoLife, person_ent)
        graph.create_triple(birth, properties.P22_stemmedFrom, union)