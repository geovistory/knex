from spacy.tokens import Doc
import pandas as pd
from pyvis.network import Network
from .globals import nlp, colors

Doc.set_extension('entities', default=[])
Doc.set_extension('graph', default=[])
Doc.set_extension('graph_keys', default=set())

def extract_graph(text):
    doc = nlp(text)

    entities = pd.DataFrame(data=doc._.entities)
    graph = pd.DataFrame(data=doc._.graph)

    for ent in doc.ents:
        print(ent.text, ent.label_)

    return entities, graph


def show_graph(graph, path='./graph.html'):

    # Add node colors:
    graph['subject_color'] = [colors[klass] for klass in graph['subject_class']]
    graph['object_color'] = [colors[klass] for klass in graph['object_class']]

    # Extract nodes
    nodes_subject = graph[['subject_pk', 'subject_label', 'subject_color']].drop_duplicates(subset=['subject_pk'])
    nodes_object = graph[['object_pk', 'object_label', 'object_color']].drop_duplicates(subset=['object_pk'])

    network = Network(height=750, width=1500, notebook=False, cdn_resources='remote')
    network.add_nodes(nodes_subject['subject_label'].tolist(), color=nodes_subject['subject_color'].tolist())
    network.add_nodes(nodes_object['object_label'].tolist(), color=nodes_object['object_color'].tolist())

    for i, row in graph.iterrows():
        network.add_edge(str(row['subject_label']), str(row['object_label']), label=row['property'])

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
    network.show('graph.html', local=True, notebook=False)