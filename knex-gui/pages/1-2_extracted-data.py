import pandas as pd
import streamlit as st
import geovpylib.database as db
from components.init import init
from components.menu import menu
from knex.schema import Person, Activity, Relationship


# Initialize the page
init()

# Display the left menu
menu()


def describe_class(cls):
    st.markdown('*' + cls.__doc__.strip() + '*')
    text = ''
    for field_name, field in cls.__fields__.items():
        text += f"**{field_name}** - {field.description}<br />"
    st.markdown(text, unsafe_allow_html=True)


st.markdown('# Extracted data')
st.markdown("""For now, the library extract the following information:""")

st.markdown("#### Person")
describe_class(Person)

st.markdown("### Activity")
describe_class(Activity)

st.markdown("#### Relationship")
describe_class(Relationship)
