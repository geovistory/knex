import pandas as pd
import streamlit as st
import geovpylib.database as db
from components.init import init
from components.menu import menu


# Initialize the page
init()

# Display the left menu
menu()


st.markdown('# What it is')

st.markdown('''
Knex is a Python library which intends to extract knowledge information from raw texts.
            
It is developed by the [Digital History department of the university of Bern](https://www.dh.unibe.ch/) and by [KleioLab](https://kleiolab.ch/) for the [Geovistory](https://www.geovistory.org/) and LOD4HSS project.
''')


st.markdown('# How it works')

st.markdown('''
Knex uses LLMs and chains of actions on them in order to extract Python class instances from the text. 

Then, in a second step, those instances are transformed in modeled data respecting the [OntoMe ontology](https://ontome.net/).

The final result is reshaped in form of a graph, which make it easier to use, edit, display, ... In short, work with.
            
Also, to make the data LOD and FAIR, it is possible to first add open data from LOD silos like DBpedia and Wikidata, and then reconcile them against Geovistory data, in order to import them.
''')
