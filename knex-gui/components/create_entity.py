import pandas as pd
import streamlit as st
from knex import Graph
from .utils import graph_updated


def create_entity() -> None:
    """Display the GUI to create an entity"""

    # From state
    graph: Graph = st.session_state['graph']
    onto_classes: pd.DataFrame = st.session_state['onto_classes']

    # Title
    st.divider()
    st.markdown('### Create a new entity:')

    # The select and input boxes plus the validation button
    col1, col2, col3 = st.columns([15, 15, 3], vertical_alignment='bottom')

    # Class selection
    class_display = col1.selectbox("Class:", options=onto_classes['display'], index=None, placeholder='Choose the class')

    # Label attribution
    label = col2.text_input("Label:", placeholder='Set the label')

    # Validation button
    if col3.button('Create', key='create-entity') and class_display and label: 
        pk_class = int(onto_classes[onto_classes['display'] == class_display].iloc[0]['pk'])
        graph.create_entity_aial(pk_class, label)
        graph_updated()
        st.rerun()


