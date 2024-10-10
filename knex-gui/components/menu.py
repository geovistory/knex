import streamlit as st

def menu():

    st.sidebar.markdown('## KNEX GUI')
    st.sidebar.page_link('pages/1-1_presentation.py', label="Presentation")
    st.sidebar.page_link('pages/1-2_extracted-data.py', label="Extracted data")


    st.sidebar.write('')
    st.sidebar.markdown('## Knowledge Extraction')
    st.sidebar.page_link('pages/2-1_load-graph.py', label="Load graph")
    st.sidebar.page_link('pages/2-2_explore.py', label="Explore")
    st.sidebar.page_link('pages/2-3_visualize.py', label="Visualize")
    st.sidebar.page_link('pages/2-4_interact.py', label="Interact")

    st.sidebar.write('')
    st.sidebar.markdown('## Geovistory')
    st.sidebar.page_link('pages/3-1_reconciliation.py', label="Data reconciliation")
    st.sidebar.page_link('pages/3-2_export.py', label="Export to Geovistory")
    
    st.sidebar.divider()

    st.sidebar.page_link('pages/9-1_hls-persons.py', label="HLS persons")