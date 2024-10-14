import streamlit as st
from knex import Graph, ontology
from .utils import graph_updated

def init(layout='centered'):

    st.set_page_config(page_icon=':link:', page_title='Knex GUI', layout=layout)

    # Change CSS
    st.markdown("""
        <style>
        button[kind="primary"] {
            background: none !important;
            border: none;
            padding: 0!important;
            color: #66f !important;
            text-decoration: none;
            cursor: pointer;
            border: none !important;
            text-align:left
        }
        button[kind="primary"]:hover {
            text-decoration: none;
            color: #aaf !important;
        }
        button[kind="primary"]:focus {
            outline: none !important;
            box-shadow: none !important;
            color: #ccf !important;
        }
        button[kind="secondary"]:hover {
            color: #aaf !important;
            border-color: #aaf !important;
        }
        button[kind="secondary"]:focus {
            outline: none !important;
            box-shadow: none !important;
            color: #ccf !important;
            border-color: #ccf !important;
        }
        button:active {
            background-color: #aaf !important;
        }
        </style>
        """, unsafe_allow_html=True)
    

    # Initialize ontology
    if 'onto_classes' not in st.session_state or 'onto_properties' not in st.session_state:
        classes_df, properties_df = ontology.to_dataframes()
        st.session_state['onto_classes'] = classes_df
        st.session_state['onto_properties'] = properties_df


    # Initialize state
    if 'graph' not in st.session_state:
        st.session_state['graph'] = Graph()
        graph_updated()
    if 'selected_entity' not in st.session_state:
        st.session_state['selected_entity'] = None
    if 'selected_entity_history' not in st.session_state:
        st.session_state['selected_entity_history'] = []
