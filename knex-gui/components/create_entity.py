import streamlit as st


def create_entity(graph):

    # Feature: Create a new Entity
    st.markdown('---')
    onto_classes = st.session_state['onto_classes']
    st.markdown('### Create a new entity:')
    col1, col2, col3 = st.columns([15, 15, 1], vertical_alignment='bottom')
    class_display = col1.selectbox("Class:", options=onto_classes['display'], index=None, placeholder='Choose the class')
    label = col2.text_input("Label:", placeholder='Set the label')
    if col3.button('✅', type='primary', key='create-entity'): 
        # Get pk class
        pk_class = int(onto_classes[onto_classes['display'] == class_display].iloc[0]['pk'])
        entity = graph.create_entity_aial(pk_class, label)
        entity_display = entity.get_display()
        st.success(f'Entity "{entity_display}" created')
        st.rerun()


