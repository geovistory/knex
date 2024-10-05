import streamlit as st

def menu():
    st.sidebar.page_link('pages/graph.py', label="Graph") #, use_container_width=True)
    st.sidebar.page_link('pages/explore.py', label="Explore") #, use_container_width=True)
    st.sidebar.page_link('pages/visualize.py', label="Visualize") #, use_container_width=True)
    
    st.sidebar.divider()

    st.sidebar.page_link('pages/hls-persons.py', label="HLS persons")
    st.sidebar.page_link('pages/export-gv.py', label="Export to Geovistory")