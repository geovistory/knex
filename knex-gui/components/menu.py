import streamlit as st

def menu():
    has_graph = 'graph' not in st.session_state

    st.sidebar.markdown('## KNEX GUI')
    st.sidebar.page_link('pages/1-1_presentation.py', label="Presentation")
    st.sidebar.page_link('pages/1-2_extracted-data.py', label="Extracted data")


    st.sidebar.write('')
    st.sidebar.markdown('## Knowledge Extraction')
    st.sidebar.page_link('pages/2-1_load-graph.py', label="Load graph")
    st.sidebar.page_link('pages/2-2_explore.py', label="Explore", disabled=has_graph)
    st.sidebar.page_link('pages/2-3_visualize.py', label="Visualize", disabled=has_graph)
    st.sidebar.page_link('pages/2-4_interact.py', label="Interact", disabled=has_graph)

    st.sidebar.write('')
    st.sidebar.markdown('## LOD')
    st.sidebar.page_link('pages/3-1_add_lod_silos.py', label="Add data from LOD silos", disabled=has_graph)
    st.sidebar.page_link('pages/3-2_reconciliation.py', label="Identify Geovistory entities", disabled=has_graph)
    st.sidebar.page_link('pages/3-3_export.py', label="Export to Geovistory", disabled=has_graph)
    
    st.sidebar.divider()

    st.sidebar.page_link('pages/9-1_hls-persons.py', label="HLS persons")