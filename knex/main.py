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
from spacy.tokens import Doc


class KnexOptions:    
    def __init__(self, 
                 reset_graph = True, 
                 ollama_url = 'http://localhost:11434/api/generate', 
                 model_name = 'llama3', 
                 compute_assertions = True, 
                 return_feedbacks = False
                 ):
        """
        Create an option instance for the extraction function

        Args
        - reset_graph (bool): Start from a clean graph when executing. If this is False, it keeps the latest graph in memory in order to avoid duplicates.
        - ollama_url (string): The Ollama server URL the LLM is going to be asked from
        - model_name (string): which model is going to be queried.
        - compute_assertions (bool): Whether or not to compute (ask llm) to simplify the initial text.
        - return_feedbacks (bool): Whether or not the Return object should have the feedback string or not.
        """
        self.reset_graph = reset_graph
        self.ollama_url = ollama_url
        self.model_name = model_name
        self.compute_assertions = compute_assertions
        self.return_feedbacks = return_feedbacks



class KnexReturn:
    graph: pd.DataFrame
    feedback: str
    assertions: List[str]
    docs: List[Doc]


def extract(
        text: str,
        options: KnexOptions = KnexOptions(),
        debug_list: List[str] = [],
    ) -> KnexReturn:
    """
    Extract the knowledge graph from the given text.

    Args:
    - text (str): the text to extract the graph from.
    - debug_list (List[str]): The list of things to debug, for all, set debug=['all']
    - options (KnexOptions): Allow to modify default options

    Return:
    Instance of KnexReturn, with different content:
        - graph (pd.DataFrame): the full built graph (increased in case of not reset)
        - feedback (str): the same string as input, with highlighted content, given caller feedback of what happend
        - assertions (str): depending on the option, returns either a list of sentences from the input, or the list of assertions from the Model
        - docs (List[spacy.Doc]): the list of piped document by spacy and additionals components
    """

    # init phase
    if options.reset_graph: graph.reset() # If the graph needs to be reset or not (in case it is ran on multiple text from same corpus)
    input_text = text.strip() # In case their is trailing spaces
    init_debug(debug_list) # Initialize the debuging handling
    to_return = KnexReturn()

    # Display initial text
    if debug('init'):
        print(cli_bold('[KNEX] > Input text:'))
        print(wrap(input_text, length=100))

    # Compute assertions or parse them from input text
    if debug('assertions'): print(cli_bold('[KNEX] > Assertions:'))
    if options.compute_assertions: to_return.assertions = get_assertions(text, options.ollama_url, options.model_name)
    else: to_return.assertions = list(map(lambda sentence: sentence.text.strip(), nlp(input_text).sents))
    if debug('assertions'): [print(assertion.strip()) for assertion in to_return.assertions]

    # Extraction
    if debug('extraction'): print(cli_bold('[KNEX] > Extract data from assertions:'))
    to_return.docs = list(nlp.pipe(to_return.assertions))
    for doc in to_return.docs: # According to spaCy documentation, this is the most efficient way of running pipeline on a string.
        if debug('extraction'): print(cli_bold(f'>> "{doc.text}"'))
        graph.extract(doc)
    to_return.graph = graph.to_dataframe()

    # Generate the feedback string 
    if options.return_feedbacks:
        feedbacks = []
        for doc in to_return.docs:
            # Compute feedbacks
            text_ = list(map(lambda token: token.text, doc))
            for ent in doc.ents:
                if not ent._.linked:
                    for i in range(ent.start, ent.end):
                        text_[i] = '\033[4m' + text_[i] + '\033[0m'
                for i in range(ent.start, ent.end):
                    text_[i] = '\033[1m' + text_[i] + '\033[0m' + f' ({ent.label_})' 
            feedbacks.append(' '.join(text_))
        to_return.feedback = '\n'.join(feedbacks)

    return to_return



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