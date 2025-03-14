import streamlit as st

def menu():
    st.sidebar.markdown('## KNEX GUI')
    # st.sidebar.page_link('pages/1-1_presentation.py', label="Presentation")
    st.sidebar.page_link('pages/1-2_extracted-data.py', label="Extracted data")


    st.sidebar.write('')
    st.sidebar.markdown('## Knowledge Extraction')
    st.sidebar.page_link('pages/2-1_add-graph.py', label="Add a graph")
    st.sidebar.page_link('pages/2-2_add-tabular.py', label="Add tabular data")
    st.sidebar.page_link('pages/2-3_explore.py', label="Explore")
    st.sidebar.page_link('pages/2-4_visualize.py', label="Visualize")

    # st.sidebar.write('')
    # st.sidebar.markdown('## LOD')
    # st.sidebar.page_link('pages/3-1_add_lod_silos.py', label="Add data from LOD silos")
    # st.sidebar.page_link('pages/3-2_reconciliation.py', label="Identify Geovistory entities")
    # st.sidebar.page_link('pages/3-3_export-gv.py', label="Export to Geovistory")
    # st.sidebar.page_link('pages/3-4_export_sparql.py', label="Export to a SPARQL endpoint")
    
    st.sidebar.divider()

    st.sidebar.page_link('pages/9-1_hls-persons.py', label="HLS persons")