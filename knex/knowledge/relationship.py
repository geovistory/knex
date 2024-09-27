from ..schema import Graph, Relationship
from ..constants import properties as p, classes as c


def relationship_to_graph(relationship: Relationship, graph: Graph):
    """
    Transform an object instance into a list of entities and statements.

    Args:
        relationship (Relationship): the relationship to be added to the graph.
        graph (Graph): the graph to add the relationship to.
    """

    # Take only the ones we want to
    valid = ['romantic', 'marriage', 'friendship', 'mentorship', 'colleagues']
    if relationship.relationship_type not in valid: return

    # Person involved in the relationship
    if relationship.person1_name:
        p1_name = relationship.person1_name
        person1 = graph.create_entity_aial(c.E21_person, p1_name)
    else: p1_name = "Unknown Person " + str(graph.get_current_index())
    if relationship.person2_name:
        p2_name = relationship.person2_name
        person2 = graph.create_entity_aial(c.E21_person, p2_name)
    else: p2_name = "Unknown Person " + str(graph.get_current_index())

    # The relationship itself
    relationship_name = ' and '.join(sorted([p1_name, p2_name]))
    relationship_ent = graph.create_entity(c.C9_relationship, relationship_name)
    graph.create_triple(relationship_ent, p.P20_hadPartner, person1)
    graph.create_triple(relationship_ent, p.P20_hadPartner, person2)

    # The relationship type
    rel_type = graph.create_entity_aial(c.C10_typeOfPersonsInteraction, relationship.relationship_type.capitalize())
    graph.create_triple(relationship_ent, p.P21_hasTypeOfInteraction, rel_type)

    # Timing information
    if relationship.date_begin:
        date = graph.create_entity(c.E61_timePrimitive, relationship.date_begin)
        graph.create_triple(relationship_ent, p.P82a_beginOfTheBegin, date)
    if relationship.date_end:
        date = graph.create_entity(c.E61_timePrimitive, relationship.date_end)
        graph.create_triple(relationship_ent, p.P82b_endOfTheEnd, date)