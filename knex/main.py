from typing import List

from .schema import Information, Graph
from .extraction import extract_names, extract_persons, extract_activities, extract_relationships
from .knowledge import person_to_graph, activity_to_graph, relationship_to_graph


def extraction(text: str, verify: bool = False, verbose: bool = False) -> Information:
    """
    Extract a dedicated topic from the given text.

    Args:
        text (str): The text to extract information from.
        verify (bool): This option allows to ask if every assumption is correct or not (requery LLM). At the moment do nothing else than to print log.
        verbose (bool): either or not display logs during extractions.

    Return:
        KnexResult: an instance that regroups all result of this library.
    """

    extracted = Information()
    extracted.persons_names = extract_names(text, verify, verbose)
    extracted.persons = extract_persons(text, extracted.persons_names, verify, verbose)
    extracted.activities = extract_activities(text, extracted.persons_names, verify, verbose)
    extracted.relationships = extract_relationships(text, extracted.persons_names, verify, verbose)
    return extracted


def knowledge(information: Information, graph: Graph = None) -> Graph:
    """
    Transform the extracted information into a graph.

    Args:
        information (Information): the extracted model from the text (output of extraction() function).
        graph (Graph): if a graph is specified, add the information to the given one, otherwise create a new one.

    Returns:
        Graph: the populated graph.
    """

    if not graph: graph = Graph()

    # Add all persons to the graph
    if information.persons and len(information.persons) > 0:
        for person in information.persons:
            person_to_graph(person, graph)

    # Add all activities to the graph
    if information.activities and len(information.activities) > 0:
        for activity in information.activities:
            activity_to_graph(activity, graph)

    # Add all relationships to the graph
    if information.relationships and len(information.relationships) > 0:
        for relationship in information.relationships:
            relationship_to_graph(relationship, graph)
            

    return graph


def knowledge_extraction(text: str, graph: Graph = None, verify: bool = False, verbose: bool = False) -> Graph:
    """
    Run the full pipeline on the given text:
    1/ Extract the information from the text and transform it into Python classes instances.
    2/ Transform the Python classes instance into a graph (respecting the ontology).

    Args:
        text (str): The text to run the pipeline on.
        graph (Graph): if a graph is specified, add the information to the given one, otherwise create a new one.
        verify (bool): This option allows to ask if every assumption is correct or not. At the moment do nothing else than to print log.
        verbose (bool): If True, the pipeline will display all information in the logs (only for extraction step).

    Returns:
        pandas.DataFrame: The resulting graph.
    """

    information = extraction(text, verify, verbose)
    graph = knowledge(information, graph)

    return graph