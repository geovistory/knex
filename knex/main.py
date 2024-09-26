from typing import Dict
from .extraction import extract_names, extract_persons, extract_activities, extract_relationships
from .knowledge import Graph, parse_person, parse_activity, parse_relationship

def extraction(text: str, verify=True, verbose=False):
    """
    Extract a dedicated topic from the given text.

    Parameters:
    text [str]: The text to extract information from
    verify [bool]: either or not re-query LLM after extraction to verify assertions
    verbose [bool]: either or not display logs during extractions
    """

    to_return = {}
    to_return['names'] = extract_names(text, verify, verbose)
    to_return['persons'] = extract_persons(text, to_return['names'], verify, verbose)
    to_return['activities'] = extract_activities(text, to_return['names'], verify, verbose)
    to_return['relationships'] = extract_relationships(text, to_return['names'], verify, verbose)

    return to_return


def knowledge(result: Dict) -> Graph:
    """
    Transform the extracted information into a graph

    Parameters:
    result [Any]: the extracted model from the text (output of extraction() function)
    """

    graph = Graph()

    if 'persons' in result.keys(): 
        for person in result['persons']: 
            parse_person(person, graph)

    if 'activities' in result.keys(): 
        for activity in result['activities']: 
            parse_activity(activity, graph)

    if 'relationships' in result.keys(): 
        for relationship in result['relationships']: 
            parse_relationship(relationship, graph)

    return graph

