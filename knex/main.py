from typing import Dict
import pandas as pd
from pyvis.network import Network
from .globals import nlp, graph
from .components import *
from .graphs import *
from .constants.colors import colors
from .llm import build_prompt, ask_ollama
from .model.response import Response
from gmpykit import wrap

# For the Ollama server
glo_ollama_url = 'http://localhost:11434/api/generate'
glo_ollama_model_name = 'mistral'

# For convenience
glo_debug = False
glo_visual = False
glo_visual_path = './graph.html'
glo_ask_llm = True


def init(ollama_url: str = None, ollama_model_name: str = None, debug: bool = False, visual: bool = False, visual_path: str = './graph.html', ask_llm: bool = True):
    global glo_ollama_url, glo_ollama_model_name
    global glo_debug, glo_visual, glo_visual_path, glo_ask_llm

    if ollama_url: glo_ollama_url = ollama_url
    if ollama_model_name: glo_ollama_model_name = ollama_model_name
    glo_debug = debug
    glo_visual = visual
    glo_visual_path = visual_path
    glo_ask_llm = ask_llm


def run(input_text: str) -> pd.DataFrame:
    global glo_debug, glo_visual, glo_visual_path, glo_ask_llm

    if glo_debug: 
        print('\033[1m[KNEX] > Input text:\033[0m')
        print(wrap(input_text, length=100))

    # Get LLM understanding of the input text
        if glo_debug: print('\033[1m[KNEX] > Assertions:\033[0m')
    if glo_ask_llm: assertions = structure_data(input_text)
    else: assertions = list(map(lambda sentence: sentence.text, nlp(input_text).sents))
    if glo_debug: [print(assertion.strip()) for assertion in assertions]

    # Extract Knowledge graph from assertions
    if glo_debug: print('\033[1m[KNEX] > Extracted data:\033[0m')
    for doc in nlp.pipe(assertions):
        graph.extract(doc)

    # Add usefull information for the graph
    graph_df = widen_graph()
    if glo_debug: 
        print('\033[1m[KNEX] > Graph dataframe:\033[0m')
        print(graph_df)

    # Generate the visual
    if glo_visual: generate_visual(graph_df, glo_visual_path)

    return Response(input_text, assertions, graph_df)
    


def structure_data(input_text: str) -> str:
    global glo_ollama_url, glo_ollama_model_name

    prompt = build_prompt(input_text)
    llm_answer = ask_ollama(glo_ollama_url, glo_ollama_model_name, prompt)

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