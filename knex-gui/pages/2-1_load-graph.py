import streamlit as st
import pickle
from components.init import init
from components.menu import menu
import knex
from datetime import datetime

# Initialize the page
init()

# Display the left menu
menu()


# Graph source radio options
radio_options = [
    "Load from disk (pickle file)",
    "Generate using Ollama server",
    "Generate using OpenAI API key",
]


# -------------------------------

def put_graph_in_session(graph):
    """This function write the given graph into the session state."""

    if 'selected_entity' in st.session_state:
        del st.session_state['selected_entity']
    st.session_state['graph'] = graph

    # Load the graph as dataframe (will be used for reading access and display)
    st.session_state['graph_df'] = graph.to_dataframe()

    # Put the ontology in memory
    _, _, classes, properties = graph.dataframes()
    classes['display'] = classes['label'] + ' (' + classes['id'] + ')'
    properties['display'] = properties['label'] + ' (' + properties['id'] + ')'
    st.session_state['onto_classes'] = classes
    st.session_state['onto_properties'] = properties


def update_radio():
    """This function is called on radio change. It is needed so that it remeberrs the radio state when changing the page."""
    st.session_state['graph_source'] = st.session_state['radio_widget']

# -------------------------------


# Init State: Set the radio as Disk graph
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
    st.session_state['openai_api_key'] = ''
# Init State: Default value for model name
if 'openai_model_name' not in st.session_state:
    st.session_state['openai_model_name'] = 'gpt-4o'
# Init State: Default value for the extraction text
if 'raw_text' not in st.session_state:
    st.session_state['raw_text'] = ''


# Main display of the page
st.title("Load a graph")
st.radio(
    'Select your graph source:', 
    radio_options, 
    radio_options.index(st.session_state['graph_source']),
    key='radio_widget',
    on_change=update_radio
)


### FROM DISK ###

st.divider()
if st.session_state['graph_source'] == radio_options[0]:

    # If no file is loaded, allow to choose
    if 'file_name' not in st.session_state:
        uploaded_file = st.file_uploader("Choose a graph file (Pickle)")
        if uploaded_file is not None:
            # Save the file name
            st.session_state['file_name'] = uploaded_file.name

            # Load the graph and save it
            graph = pickle.load(uploaded_file)
            put_graph_in_session(graph)

            # Rerun to display things correctly
            st.rerun()

    # Otherwise, just display the file name
    else:
        st.markdown(f'Graph name: ***{st.session_state["file_name"]}***')


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
                    graph = knex.knowledge_extraction(raw_text, verbose=True)
                    put_graph_in_session(graph)
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
                    put_graph_in_session(graph)
                    st.success('Graph extracted')
                except Exception as err:
                    st.error(err)



st.divider()

# If there is a graph in memory
if 'graph' in st.session_state:

    # Reset the graph (erase) with confirmation
    if st.button('Clear graph'):
        if st.session_state['clear_count'] == 0:
            st.session_state['clear_count'] = 1
            st.warning('You are about to clear the in memory graph. Changes will be deleted. Click again to confirm.')
        else:
            if 'file_name' in st.session_state: del st.session_state['file_name']
            if 'graph' in st.session_state: del st.session_state['graph']
            if 'graph_df' in st.session_state: del st.session_state['graph_df']
            if 'onto_classes' in st.session_state: del st.session_state['onto_classes']
            if 'onto_properties' in st.session_state: del st.session_state['onto_properties']
            if 'selected_entity_history' in st.session_state: del st.session_state['selected_entity_history']
            st.session_state['clear_count'] = 0
            st.rerun()

    # Allow to export the graph (save)
    now = datetime.now()
    col1, col2 = st.columns([5, 2], vertical_alignment="bottom")
    file_name = col1.text_input('File name', value=f"graph_{now.strftime('%Y-%m-%d_%H:%M:%S')}.pkl")
    col2.download_button("Export graph", data=pickle.dumps(st.session_state['graph']), file_name=file_name)
