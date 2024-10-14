import os, pandas as pd
from datetime import datetime
import streamlit as st
from components.init import init
from components.menu import menu
from components.utils import expand_graph, graph_updated
import knex
from knex import Graph

# Initialize the page
init()

# Display the left menu
menu()


# Graph source radio options
radio_options = [
    "Load from disk (CSV)",
    "Generate using Ollama server",
    "Generate using OpenAI API key",
]


def update_radio():
    """This function is called on radio change. It is needed so that it remembers the radio state when changing the page."""
    st.session_state['graph_source'] = st.session_state['radio_widget']


# Init State: Set the radio as "Load from disk" (default)
if 'graph_source' not in st.session_state:
    st.session_state['graph_source'] = radio_options[0]
# Init State: Clear validation
if 'clear_count' not in st.session_state: 
    st.session_state['clear_count'] = 0
# Init State: Default value for Ollama server URL
if 'ollama_server_url' not in st.session_state:
    st.session_state['ollama_server_url'] = 'http://localhost:11434'
# Init State: Default value for model name
if 'ollama_model_name' not in st.session_state:
    st.session_state['ollama_model_name'] = 'llama3.1'
if 'openai_api_key' not in st.session_state:
    if 'OPENAI_API_KEY' in os.environ: st.session_state['openai_api_key'] = os.getenv('OPENAI_API_KEY')
    else: st.session_state['openai_api_key'] = ''
# Init State: Default value for model name
if 'openai_model_name' not in st.session_state:
    st.session_state['openai_model_name'] = 'gpt-4o'
# Init State: Default value for the extraction text
if 'raw_text' not in st.session_state:
    st.session_state['raw_text'] = ''


# Title and main option
st.title("Load a graph")
st.radio(
    'Select your graph source:', 
    radio_options, 
    radio_options.index(st.session_state['graph_source']),
    key='radio_widget',
    on_change=update_radio
)


st.divider()


### FROM DISK ###

if st.session_state['graph_source'] == radio_options[0]:

    paths = st.file_uploader("Add a graph file to current graph (format: CSV)", accept_multiple_files=True, type=['CSV'])
    for path in paths:
        new_graph = Graph.from_dataframe(pd.read_csv(path))
        expand_graph(new_graph)


### FROM OLLAMA ###

if st.session_state['graph_source'] == radio_options[1]:

    # Ollama options
    col1, col2 = st.columns([5, 1])
    ollama_server_url = col1.text_input("Ollama server URL", value=st.session_state['ollama_server_url'])
    ollama_model_name = col2.text_input("Model name", value=st.session_state['ollama_model_name'])

    # The text to extract
    raw_text = st.text_area("Raw text to extract information from:", placeholder='Write, paste a text', value=st.session_state['raw_text'], height=280)

    # Check if every information is present
    if ollama_server_url and ollama_model_name and raw_text:

        # Save param in memory
        st.session_state['ollama_server_url'] = ollama_server_url
        st.session_state['ollama_model_name'] = ollama_model_name
        st.session_state['raw_text'] = raw_text

        # On generate button click, call the right server to extract the information and put it in session state
        if st.button("Generate graph"):
            with st.spinner(text="Extracting... (can take some minutes)"):
                try:
                    knex.init('ollama', model=ollama_model_name, url=ollama_server_url)
                    expand_graph(knex.knowledge_extraction(raw_text, verbose=True))
                    st.success('Graph extracted')
                except Exception as err:
                    st.error(err)


### OPENAI ###

if st.session_state['graph_source'] == radio_options[2]:

    # OpenAI options
    col1, col2 = st.columns([5, 2])
    openai_api_key = col1.text_input("OpenAI API key", value=st.session_state['openai_api_key'])
    openai_model_name = col2.text_input("Model name", value=st.session_state['openai_model_name'])

    # The text to extract
    raw_text = st.text_area("Raw text to extract information from:", placeholder='Write, paste a text', value=st.session_state['raw_text'], height=280)

    # Check if every information is present
    if openai_api_key and openai_model_name and raw_text:

        # Save param in memory
        st.session_state['openai_api_key'] = openai_api_key
        st.session_state['openai_model_name'] = openai_model_name
        st.session_state['raw_text'] = raw_text

        # On generate button click, call the right server to extract the information and put it in session state
        if st.button("Generate graph"):
            with st.spinner(text="Extracting... (can take some minutes)"):
                try:
                    knex.init('openai', model=openai_model_name, api_key=openai_api_key)
                    graph = knex.knowledge_extraction(raw_text, verbose=True)
                    expand_graph(knex.knowledge_extraction(raw_text, verbose=True))
                    st.success('Graph extracted')
                except Exception as err:
                    st.error(err)


# Reset the graph (erase) with confirmation
st.divider()
if st.button('Clear graph'):
    if st.session_state['clear_count'] == 0:
        st.session_state['clear_count'] = 1
        st.warning('You are about to clear the in memory graph. Changes will be deleted. Click again to confirm.')
    else:
        # Clear the graph
        st.session_state['graph'] = Graph()
        graph_updated()

        # Clear the remaining state
        del st.session_state['selected_entity']
        del st.session_state['clear_count']
        del paths
        st.rerun()


# Allow to export the graph (save)
st.divider()
if st.button('Download graph'):
    now = datetime.now()
    graph: Graph = st.session_state['graph']
    col1, col2 = st.columns([5, 2], vertical_alignment="bottom")
    file_name = col1.text_input('File name', value=f"graph_{now.strftime('%Y-%m-%d_%H:%M:%S')}.pkl")
    col2.download_button("Export graph", data=graph.to_dataframe().to_csv(index=False).encode('utf-8'), file_name=file_name)
