import pandas as pd
import streamlit as st
import geovpylib.database as db
from components.init import init
from components.menu import menu


# Initialize the page
init()

# Display the left menu
menu()


st.write("Add data from external LOD silos (Wikidata, DBpedia, ...)")

st.write('Not yet developed')
