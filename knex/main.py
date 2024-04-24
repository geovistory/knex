from typing import Dict
import pandas as pd
from pyvis.network import Network
from .globals import nlp, graph
from .components import *
from .graphs import *
from .constants.colors import colors

def init():
    pass


def run(input_text: str, debug: bool = False, visual: bool = False, path: str = './graph.html') -> Dict:
    graph.debug_mode(debug)

    structured_text = structure_data(input_text)

    for statement in structured_text.split('\n'):
        extract_graph(statement)

    graph_df = widen_graph()
    if visual: generate_visual(graph_df, path)
    


def structure_data(input_text: str) -> str:
    # Ask the LLM to reformulate
    return input_text



def extract_graph(statement: str):

    doc = nlp(statement)
    graph.extract(doc)



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