from typing import List
import pandas as pd
import streamlit as st
from knex import Graph
from .utils import graph_updated


        
def create_triple():
    """Display the GUI to create a triple"""

    # From state
    graph: Graph = st.session_state['graph']
    onto_properties: pd.DataFrame = st.session_state['onto_properties']
    entity_displays: List[str] = st.session_state['entity_displays']

    # Title
    st.divider()
    st.markdown('### Add a new triple:')

    # The 3 elements of the triple, plus the creation button
    col1, col2, col3, col4 = st.columns([10, 10, 10, 3], vertical_alignment='bottom')

    new_subject = col1.selectbox("Subject", entity_displays, index=None, placeholder='Choose a subject')
    new_property = col2.selectbox("Property", onto_properties['display'], index=None, placeholder='Choose a property')
    new_object = col3.selectbox("Object", entity_displays, index=None, placeholder='Choose an object')

    # When new triple is validated
    # Create the triple in the main graph, only if all data are present
    if col4.button('Create', key='create-triple') and new_subject and new_property and new_object: 
        # Get the subject
        pk_subject = int(new_subject[new_subject.index('pk'):].replace('pk', '').replace(')', '').strip())
        subject = graph.get_entity(pk_subject)
        # Find the pk property
        pk_property = int(onto_properties[onto_properties['display'] == new_property].iloc[0]['pk'])
        # Get the object
        pk_object = int(new_object[new_object.index('pk'):].replace('pk', '').replace(')', '').strip())
        object = graph.get_entity(pk_object)

        # Add the new triple to the graph
        graph.create_triple(subject, pk_property, object)
        graph_updated()
        st.rerun()