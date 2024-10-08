import streamlit as st

def menu():

    st.sidebar.markdown('## Information')
    st.sidebar.page_link('pages/graph.py', label="Graph") #, use_container_width=True)
    st.sidebar.page_link('pages/explore.py', label="Explore") #, use_container_width=True)
    st.sidebar.page_link('pages/visualize.py', label="Visualize") #, use_container_width=True)

    st.sidebar.write('')
    st.sidebar.markdown('## Geovistory')
    st.sidebar.page_link('pages/reconciliation.py', label="Data reconciliation")
    st.sidebar.page_link('pages/export-gv.py', label="Export to Geovistory")
    
    st.sidebar.divider()

    st.sidebar.page_link('pages/hls-persons.py', label="HLS persons")