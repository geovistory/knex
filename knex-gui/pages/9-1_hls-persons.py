import pandas as pd
import streamlit as st
from components.init import init
from components.menu import menu
import clipboard


# Initialize the page
init()

# Display the left menu
menu()

st.title('HLS persons')

hls_persons = pd.read_csv('./hls_persons.csv')

st.markdown(f'''
This page regroup {len(hls_persons)} texts of persons extracted and reformated from the [HLS base](https://hls-dhs-dss.ch/).

They are available here in order to easily test the Knex tool: take someone from the list, copy the text, and insert it in the [Knowledge Extraction / Graph](/graph) page to get the extracted graph.
''')

person = st.selectbox("Look for a person", hls_persons['name'].tolist(), index=None)

if person:

    row = hls_persons[hls_persons['name'] == person].iloc[0]

    st.divider()
    col1, col2 = st.columns([5, 1])
    col1.markdown(f"### {row['name']}")
    if col2.button("Copy notice"):
        clipboard.copy(row['notice'])
    st.page_link(row['url'], label=row['url'], icon='↗️')
    st.write(row['notice'].replace('\n', '<br />'), unsafe_allow_html=True)
