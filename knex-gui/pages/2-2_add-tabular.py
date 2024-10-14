import pandas as pd
import streamlit as st
from components.init import init
from components.menu import menu
from components.utils import graph_updated
from knex.knowledge import person_to_graph
from knex import Graph, Person


# Initialize the page
init(layout='wide')

# Display the left menu
menu()


# From state
graph: Graph = st.session_state['graph']


# Title
st.title('Load tabular data')
st.markdown('You can transform into a graph special tabular data (as long as they respect the required format).')
st.markdown('The spreadsheet can have additional columns, but they will be ignored.')
st.markdown('If the table is missing a required column, it will be treated as empty.')
st.markdown('Only displayed column are supported.')


### PERSONS ###

# Init state: the person table 
if 'tabular_person' not in st.session_state:
    st.session_state['tabular_person'] = None

# Sub title
st.divider()
st.markdown('### Load Persons')
st.markdown('Table needs to be like:')

# Load example file
persons_table = pd.read_csv('./data/tabular_persons_example')
st.dataframe(persons_table)


if st.session_state['tabular_person'] is None:
    uploaded_persons = st.file_uploader("Load your table:", type=['csv'])
    if uploaded_persons: 
        st.session_state['tabular_person'] = pd.read_csv(uploaded_persons)
        st.rerun()

else:
    st.markdown('Your table is:')
    st.dataframe(st.session_state['tabular_person'])

    col1, col2, col3 = st.columns([2, 2, 10])
    if col1.button('Clear'):
        del st.session_state['tabular_person']
        st.rerun()

    if col2.button('Load'):
        for _, row in st.session_state['tabular_person'].iterrows():
            person_to_graph(Person(**(row.to_dict())), graph)
        del st.session_state['tabular_person']
        graph_updated()
        st.success('Table has added to graph')