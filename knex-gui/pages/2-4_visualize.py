from typing import List
import pandas as pd, numpy as np
from pyvis.network import Network
import streamlit as st
from components.init import init
from components.menu import menu
from components.create_entity import create_entity
from components.create_triple import create_triple
from knex.constants import colors
from knex import Graph


# Initialize the page
init(layout='wide')

# Display the left menu
menu()


def get_graph_depth(entity_display, depth):
    """Given an entity disply label and a depth, get the sub graph of this entity"""
    entities_to_fetch = [entity_display]
    graph = st.session_state['graph_df']
    for _ in range(depth):
        selection = graph[[ row['subject_display'] in entities_to_fetch or row['object_display'] in entities_to_fetch for _, row in graph.iterrows()]]
        entities_to_fetch += selection['subject_display'].tolist()
        entities_to_fetch += selection['object_display'].tolist()
        entities_to_fetch = list(np.unique(entities_to_fetch))
    return selection.copy()


# From state
graph: Graph = st.session_state['graph']
graph_df: pd.DataFrame = st.session_state['graph_df']
onto_properties: pd.DataFrame = st.session_state['onto_properties']
entity_displays: List[str] = st.session_state['entity_displays']


# Title
st.title("Visualize graph")


# Visualization options: entity selection + graph depth
col1, col2 = st.columns([5, 1])
index = None if st.session_state['selected_entity'] == None else entity_displays.index(st.session_state['selected_entity'])
selected_display = col1.selectbox("Select an entity:", entity_displays, index=index, placeholder='Choose an entity')
graph_depth = col2.number_input('Graph depth', min_value=1, step=1)


# The Graph
if selected_display and graph_depth:
    # Save it
    st.session_state['selected_entity'] = selected_display

    # Get graph from memory
    graph_df = get_graph_depth(selected_display, graph_depth)

    # A bit of formating
    graph_df['subject_display'] = graph_df['subject_display'].str.replace(' (', '\n(') 
    graph_df['object_display'] = graph_df['object_display'].str.replace(' (', '\n(') 

    # Add node colors:
    graph_df['subject_color'] = [colors[klass] if pd.notna(klass) else '#000' for klass in graph_df['subject_class_pk']]
    graph_df['object_color'] = [colors[klass] if pd.notna(klass) else '#000' for klass in graph_df['object_class_pk']]

    # Extract nodes
    nodes_subject = graph_df[['subject', 'subject_display', 'subject_color']].drop_duplicates(subset=['subject'])
    nodes_object = graph_df[['object', 'object_display', 'object_color']].drop_duplicates(subset=['object'])

    # Add the node to the network
    network = Network()
    network.add_nodes(nodes_subject['subject_display'].tolist(), color=nodes_subject['subject_color'].tolist())
    network.add_nodes(nodes_object['object_display'].tolist(), color=nodes_object['object_color'].tolist())

    # Add the edges
    for _, row in graph_df.iterrows():
        network.add_edge(str(row['subject_display']), str(row['object_display']), label=row['property_label'])

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

    # Save and display the network in Streamlit
    network.save_graph('network.html')
    HtmlFile = open("network.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    st.components.v1.html(source_code, height=620)


# Additional feature: Add a triple to the graph
create_triple()

# Additional feature: Add a triple to the graph
create_entity()