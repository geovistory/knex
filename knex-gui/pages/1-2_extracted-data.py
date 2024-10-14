import streamlit as st
from components.init import init
from components.menu import menu
from components.utils import describe_class
from knex import Person, Activity, Relationship


# Initialize the page
init()

# Display the left menu
menu()


st.markdown('# Extracted data')
st.markdown("""For now, the library extract the following information:""")

st.markdown("#### Person")
describe_class(Person)

st.markdown("### Activity")
describe_class(Activity)

st.markdown("#### Relationship")
describe_class(Relationship)
