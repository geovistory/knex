from ..schema import Graph, Activity
from ..constants import properties as p, classes as c


def activity_to_graph(activity: Activity, graph: Graph) -> None:
    """
    Transform an object instance into a list of entities and statements.

    Args:
        activity (Activity): the activity to be added to the graph.
        graph (Graph): the graph to add the activity to.
    """

    # If the activity or person does not have a name, set a default value
    if not activity.name:
        activity.name = "Unknown Activity " + str(graph.get_current_index())
    if not activity.person_name:
        activity.person_name = "Unknown Person " + str(graph.get_current_index())

    # The related person
    person = graph.create_entity_aial(c.E21_person, activity.person_name)

    # In case of an Occupation
    if activity.activity_type == 'job':
        occupation_peit = graph.create_entity_aial(c.C7_occupation, activity.name)
        occupation_teen = graph.create_entity(c.C8_occupationTemporalEntity, activity.name)
        graph.create_triple(occupation_teen, p.P4_isOccupationOf, person)
        graph.create_triple(occupation_teen, p.P5_isAbout, occupation_peit)

        # Temporal informations
        if activity.date_begin:
            date = graph.create_entity(c.E61_timePrimitive, activity.date_begin)
            graph.create_triple(occupation_teen, p.P82a_beginOfTheBegin, date)
        if activity.date_end:
            date = graph.create_entity(c.E61_timePrimitive, activity.date_end)
            graph.create_triple(occupation_teen, p.P82b_endOfTheEnd, date)

        # The geographical place
        if activity.place:
            geoplace = graph.create_entity_aial(c.C13_geographicalPlace, activity.place)
            graph.create_triple(occupation_teen, p.P6_tookPlaceAt, geoplace)

        # If there is a company name
        if activity.institution:
            company = graph.create_entity_aial(c.E74_group, activity.institution)
            graph.create_triple(occupation_teen, p.P7_onBehalfOf, company)

    # In case of a Social Role
    if activity.activity_type == 'social role':
        social_role = graph.create_entity_aial(c.C12_actorSSocialRole, activity.name)
        social_role_emb = graph.create_entity(c.C13_socialRoleEmbodiment, activity.name)
        graph.create_triple(social_role_emb, p.P4_isOccupationOf, person)
        graph.create_triple(social_role_emb, p.P5_isAbout, social_role)

        # Temporal informations
        if activity.date_begin:
            date = graph.create_entity(c.E61_timePrimitive, activity.date_begin)
            graph.create_triple(social_role_emb, p.P82a_beginOfTheBegin, date)
        if activity.date_end:
            date = graph.create_entity(c.E61_timePrimitive, activity.date_end)
            graph.create_triple(social_role_emb, p.P82b_endOfTheEnd, date)

        # The geographical place
        if activity.place:
            geoplace = graph.create_entity_aial(c.C13_geographicalPlace, activity.place)
            graph.create_triple(social_role_emb, p.P6_tookPlaceAt, geoplace)

        # If there is a institution
        if activity.institution:
            institution = graph.create_entity_aial(c.E74_group, activity.institution)
            graph.create_triple(social_role_emb, p.P56_carriedOutInTheContextOf, institution)

    # In case of a Formation
    if activity.activity_type == 'formation':
        study = graph.create_entity(c.C2_study, activity.name)
        graph.create_triple(study, p.P2_isTheStudyBy, person)

        # Temporal informations
        if activity.date_begin:
            date = graph.create_entity(c.E61_timePrimitive, activity.date_begin)
            graph.create_triple(study, p.P82a_beginOfTheBegin, date)
        if activity.date_end:
            date = graph.create_entity(c.E61_timePrimitive, activity.date_end)
            graph.create_triple(study, p.P82b_endOfTheEnd, date)

        # The geographical place
        if activity.place:
            geoplace = graph.create_entity_aial(c.C13_geographicalPlace, activity.place)
            graph.create_triple(study, p.P6_tookPlaceAt, geoplace)

        # If there is a school name
        if activity.institution:
            institution = graph.create_entity_aial(c.E74_group, activity.institution)
            graph.create_triple(study, p.P1_isStudyAt, institution)

        # If there is a discipline
        if activity.discipline:
            discipline = graph.create_entity_aial(c.C5_academicDiscipline, activity.discipline)
            graph.create_triple(study, p.P12_isStudyOf, discipline)