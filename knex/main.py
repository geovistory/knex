import warnings
warnings.filterwarnings("ignore")

from typing import List
import pandas as pd
from pyvis.network import Network
from gmpykit import wrap, cli_bold, cli_italic, cli_underline
from .globals import nlp, graph
from .spacy_components import *
from .graphs import *
from .constants import colors
from .debug import debug, init_debug
from .assertions import get_assertions


def extract(
        text: str,
        reset_graph: bool = True,
        compute_assertions: bool = True,
        ollama_url: str = 'http://localhost:11434/api/generate',
        model_name: str = 'llama3',
        debug_list: List[str] = [],
    ):
    """
    Extract the knowledge graph from the given text.

    Args:
    - text (str): the text to extract the graph from.
    - reset_graph (bool): Start from a clean graph when executing. If this is False, it keeps the latest graph in memory in order to avoid duplicates.
    - compute_assertions (bool): Whether or not to compute (ask llm) to simplify the initial text.
    - ollama_url (string): The Ollama server URL the LLM is going to be asked from
    - model_name (string): which model is going to be queried.
    - debug_list (List[str]): The list of things to debug, for all, set debug=['all']
    """

    # init phase
    if reset_graph: graph.reset()
    input_text = text.strip()
    init_debug(debug_list)
    feedbacks = []

    # Display initial text
    if debug('init'):
        print(cli_bold('[KNEX] > Input text:'))
        print(wrap(input_text, length=100))

    # Compute assertions or parse them from input text
    if debug('assertions'): print(cli_bold('[KNEX] > Assertions:'))
    if compute_assertions: assertions = get_assertions(text, ollama_url, model_name)
    else: assertions = list(map(lambda sentence: sentence.text.strip(), nlp(input_text).sents))
    if debug('assertions'): [print(assertion.strip()) for assertion in assertions]

    # Extraction
    if debug('extraction'): print(cli_bold('[KNEX] > Extract data from assertions:'))
    for doc in nlp.pipe(assertions): # According to spaCy documentation, this is the most efficient way of running pipeline on a string.
        if debug('extraction'): print(cli_bold(f'>> "{doc.text}"'))
        graph.extract(doc)

        # Compute feedbacks
        text_ = list(map(lambda token: token.text, doc))
        for ent in doc.ents:
            if not ent._.linked:
                for i in range(ent.start, ent.end):
                    text_[i] = '\033[4m' + text_[i] + '\033[0m'
            for i in range(ent.start, ent.end):
                text_[i] = '\033[1m' + text_[i] + '\033[0m' + f' ({ent.label_})' 
        feedbacks.append(' '.join(text_))


    # Return part
    return graph.to_dataframe(), '\n'.join(feedbacks)



def generate_visual(graph: pd.DataFrame, path: str) -> None:
    """
    From a graph DataFrame generate a html file with a graph visual

    Args:
    - graph (pd.DataFrame): A DataFrame whose columns are at least ['subject_pk', 'subject_label', 'subject_class_pk', 'property_label', 'object_class_pk', 'object_pk', 'object_label', ]
    - path (str): The place were to save the file
    """


    if len(graph) == 0: return

    # Add node colors:
    graph['subject_color'] = [colors[klass] for klass in graph['subject_class_pk']]
    graph['object_color'] = [colors[klass] for klass in graph['object_class_pk']]

    # Extract nodes
    nodes_subject = graph[['subject_pk', 'subject_label', 'subject_color']].drop_duplicates(subset=['subject_pk'])
    nodes_object = graph[['object_pk', 'object_label', 'object_color']].drop_duplicates(subset=['object_pk'])

    # Add the node to the network
    network = Network(height=750, width=1500, notebook=False, cdn_resources='remote')
    network.add_nodes(nodes_subject['subject_label'].tolist(), color=nodes_subject['subject_color'].tolist())
    network.add_nodes(nodes_object['object_label'].tolist(), color=nodes_object['object_color'].tolist())

    # Add the edges
    for i, row in graph.iterrows():
        network.add_edge(str(row['subject_label']), str(row['object_label']), label=row['property_label'])

    # Set the options
    network.set_options("""
        const options = {
            "nodes": {"font": {"face": "tahoma"}},
            "edges": {
                "arrows": {"to": {"enabled": true}},
                "font": {"size": 10,"face": "tahoma","align": "top"}
            }
        }
    """)

    # network.show_buttons(filter_=['physics'])
    network.show(path, local=True, notebook=False)