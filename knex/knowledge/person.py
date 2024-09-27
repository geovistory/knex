from ..schema import Graph, Person
from ..constants import properties as p, classes as c


def person_to_graph(person: Person, graph: Graph):
    """
    Transform an object instance into a list of entities and statements.

    Args:
        person (Person): the person to be added to the graph.
        graph (Graph): the graph to add the person to.
    """

    # If the person does not have a name, set a default value
    if not person.name:
        person.name = "Unknown Person " + str(graph.get_current_index())

    # Create the person
    person_ent = graph.create_entity_aial(c.E21_person, person.name)

    # Gender
    if person.gender:
        gender = graph.create_entity_aial(c.C11_gender, person.gender)
        graph.create_triple(person_ent, p.P23_hasGender, gender)

    # Origins
    if person.origins:
        geoplace = graph.create_entity_aial(c.C13_geographicalPlace, person.origins)
        graph.create_triple(person_ent, p.P24_hasItsOriginsIn, geoplace)

    # Religion
    if person.religion:
        religious_identity = graph.create_entity_aial(c.C23_religiousIdentity, person.religion)
        graph.create_triple(religious_identity, p.P36_pertainsTo, person_ent)

    # Birth date
    if person.birth_date:
        birth = graph.create_entity(c.E67_birth, person.name)
        date = graph.create_entity(c.E61_timePrimitive, person.birth_date)
        graph.create_triple(birth, p.P98_broughtIntoLife, person_ent)
        graph.create_triple(birth, p.P82_atSomeTimeWithin, date)

    # Birth place
    if person.birth_place:
        geoplace = graph.create_entity_aial(c.C13_geographicalPlace, person.birth_place)
        birth = graph.create_entity(c.E67_birth, person.name)
        graph.create_triple(birth, p.P98_broughtIntoLife, person_ent)
        graph.create_triple(birth, p.P8_tookPlaceOnOrWithin, geoplace)

    # Death date
    if person.death_date:
        death = graph.create_entity(c.E69_death, person.name)
        date = graph.create_entity(c.E61_timePrimitive, person.death_date)
        graph.create_triple(death, p.P100_wasDeathOf, person_ent)
        graph.create_triple(death, p.P82_atSomeTimeWithin, date)

    # Death place
    if person.death_place:
        geoplace = graph.create_entity_aial(c.C13_geographicalPlace, person.death_place)
        death = graph.create_entity(c.E69_death, person.name)
        graph.create_triple(death, p.P100_wasDeathOf, person_ent)
        graph.create_triple(death, p.P8_tookPlaceOnOrWithin, geoplace)

    # Parents
    if person.father_name or person.mother_name:
        # Unions names are ordered alphabetically so that their label match
        union_name = ' and '.join(sorted([person.father_name or "Unknown", person.mother_name or "Unknown"]))
        union = graph.create_entity(c.C9_relationship, union_name)
        # Create parents
        if person.father_name:
            father_ent = graph.create_entity_aial(c.E21_person, person.father_name)
            graph.create_triple(union, p.P20_hadPartner, father_ent)
        if person.mother_name:
            mother_ent = graph.create_entity_aial(c.E21_person, person.mother_name)
            graph.create_triple(union, p.P20_hadPartner, mother_ent)
        # Create the birth, and link it to the union
        birth = graph.create_entity(c.E67_birth, person.name)
        graph.create_triple(birth, p.P98_broughtIntoLife, person_ent)
        graph.create_triple(birth, p.P22_stemmedFrom, union)