import streamlit as st
from knex import Graph
from typing import Type
from pydantic import BaseModel


def graph_updated():
    """When the graph has been updated, some variables in states also need to be updated."""

    graph: Graph = st.session_state['graph']
    st.session_state['graph_df'] = graph.to_dataframe()
    st.session_state['entity_displays'] = list(map(lambda ent: ent.get_display(), graph.entities))


def expand_graph(new_graph):
    """Append the given graph to the existing one"""

    graph: Graph = st.session_state['graph']
    graph.merge_graph(new_graph)
    graph_updated()


def describe_class(cls: Type[BaseModel]):
    """Given a class (not an instance!) print out the pydantic field description"""

    st.markdown('*' + cls.__doc__.strip() + '*')
    text = ''
    for field_name, field in cls.model_fields.items():
        text += f"**{field_name}** - {field.description}<br />"
    st.markdown(text, unsafe_allow_html=True)

