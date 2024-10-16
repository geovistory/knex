import pandas as pd
import streamlit as st
from components.init import init
from components.menu import menu


# Initialize the page
init()

# Display the left menu
menu()

st.write('Export your data into a specific SPARQL endpoint')

st.write('Not yet developed')