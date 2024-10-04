import streamlit as st
from components.init import init
from components.menu import menu

init()
menu()

st.switch_page("pages/graph.py")