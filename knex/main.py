from typing import Any
from .extraction import extract_persons, extract_occupations, extract_relationships
from .knowledge import Graph, parse_person


def extraction(text: str, verify=True, verbose=False):
    """
    Extract a dedicated topic from the given text.

    Parameters:
    text [str]: The text to extract information from
    verify [bool]: either or not re-query LLM after extraction to verify assertions
    verbose [bool]: either or not display logs during extractions
    """

    to_return = {}
    to_return['persons'] = extract_persons(text, verify, verbose)
    # to_return['occupations'] = extract_occupations(text, verify, verbose)
    # to_return['relationships'] = extract_relationships(text, verify, verbose)

    return to_return


def knowledge(result: Any) -> Graph:
    """
    Transform the extracted information into a graph

    Parameters:
    result [Any]: the extracted model from the text (output of extraction() function)
    """

    graph = Graph()

    for person in result['persons']: parse_person(person, graph)

    return graph