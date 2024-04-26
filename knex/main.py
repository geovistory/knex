import warnings
warnings.filterwarnings("ignore")

from typing import List
import pandas as pd
from pyvis.network import Network
from gmpykit import wrap
from .globals import nlp, graph, params
from .model import Response, Graph
from .components import *
from .graphs import *
from .constants import colors
from .llm import build_prompt, ask_ollama


def init(
        debug = False,
        debug_list: List[str] = [],
        ask_llm = True,
        ollama_url = 'http://localhost:11434/api/generate',
        llm_name = 'mistral',
        visual = False,
        visual_path = './graph.html'
    ):
    params.debug = debug
    params.debug_list = debug_list
    params.ask_llm = ask_llm
    params.ollama_url = ollama_url
    params.llm_name = llm_name
    params.visual = visual
    params.visual_path = visual_path

    graph.reset()


def run(input_text: str) -> Response:
    input_text = input_text.strip()

    if params.debug: 
        print('\033[1m[KNEX] > Input text:\033[0m')
        print(wrap(input_text, length=100))

    # Get LLM understanding of the input text
        if params.debug: print('\033[1m[KNEX] > Assertions:\033[0m')
    if params.ask_llm: assertions = structure_data(input_text)
    else: assertions = list(map(lambda sentence: sentence.text.strip(), nlp(input_text).sents))
    if params.debug: [print(assertion.strip()) for assertion in assertions]

    # Extract Knowledge graph from assertions
    if params.debug or len(params.debug_list) > 0: print('\033[1m[KNEX] > Extract data from assertions:\033[0m')
    feedbacks = []
    for doc in nlp.pipe(assertions):
        if params.debug or len(params.debug_list) > 0: print(f'\033[1m>> "{doc.text}"\033[0m')
        graph.extract(doc)

        # For feedback
        text_ = list(map(lambda token: token.text, doc))
        for ent in doc.ents:
            if not ent._.linked:
                for i in range(ent.start, ent.end):
                    text_[i] = '\033[4m' + text_[i] + '\033[0m'
            for i in range(ent.start, ent.end):
                text_[i] = '\033[1m' + text_[i] + '\033[0m' + f' ({ent.label_})' 
        feedbacks.append(' '.join(text_))
    feedbacks = '\n'.join(feedbacks)
    if params.debug or len(params.debug_list) > 0: print('\033[1m==============\033[0m')
    

    if params.debug:
        print('\033[1m[KNEX] > Feedback text\033[0m')
        print('\n' + feedbacks + '\n')


    # Add usefull information for the graph
    graph_df = widen_graph()    
    if params.debug: 
        print('\033[1m[KNEX] > Graph dataframe:\033[0m')
        print(graph_df)

    # Generate the visual
    if params.visual: generate_visual(graph_df, params.visual_path)

    return Response(input_text, assertions, graph_df, feedbacks)
    


def structure_data(input_text: str) -> str:
    prompt = build_prompt(input_text)
    llm_answer = ask_ollama(prompt)

    assertions = [line[line.find(' ') + 1:] for line in llm_answer.split('\n')]

    return assertions



def widen_graph() -> pd.DataFrame:

    graph_list = []

    # Populate the graph with usefull information
    # graph['subject_pk_class'] = pd.NA
    for triple in graph.triples:
        subject = graph.get_entity(triple.subject_pk)
        subject_class = Klass.find(pk=subject.pk_class)
        property = Property.find(pk=triple.property_pk)
        object = graph.get_entity(triple.object_pk)
        object_class = Klass.find(pk=object.pk_class)

        graph_list.append({
            'subject_pk': subject.pk_entity,
            'subject_label': f'{subject.label}\n({subject_class.label})',
            'subject_class_pk': subject_class.pk,
            'subject_class_label': subject_class.label,
            'property_pk': property.pk,
            'property_label': property.label,
            'object_pk': object.pk_entity,
            'object_label': f'{object.label}\n({object_class.label})',
            'object_class_pk': object_class.pk,
            'object_class_label': object_class.label
        })
    
    return pd.DataFrame(data=graph_list)



def generate_visual(graph: pd.DataFrame, path: str) -> None:

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