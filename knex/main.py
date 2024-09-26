from typing import Dict
import pandas as pd
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



def knowledge_extraction(text: str, verify=False, verbose=False, output_csv:str=None, output_html:str=None) -> pd.DataFrame:
    """
    Run the full pipeline on the given text:
        1/ Extract the information from the text and transform it into Python classes instances
        2/ Transform the Python classes instance into a graph (respecting the ontology)

    Parameters:
    text [str]: The text to run the pipeline on
    output_csv [str]: If specified, will save the resulting graph in a CSV file, at the given path.
    output_html [str]: If specified, will save the resulting graph in a nice and shiny visual, allowing to see the graph in an interactive way.
    verify [bool]: This option allows to ask if every assumption is correct or not. At the moment doe nothing else than to print log.
    verbose [bool]: If True, the pipeline will display all information in the logs (only for extraction step).

    Return [pandas.DataFrame]: The resulting graph
    """


    extracted = extraction(text, verify, verbose)
    graph = knowledge(extracted)
    dataframe = graph.to_dataframe()

    if output_csv: dataframe.to_csv(output_csv, index=False)
    if output_html: graph.get_visuals(output_html)


    return dataframe

