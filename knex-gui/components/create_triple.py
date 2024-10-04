import streamlit as st

        
def create_triple(entity_display_list, graph, onto_properties):

    st.markdown('---')
    
    st.markdown('### Add a new triple:')
    col1, col2, col3, col4 = st.columns([10, 10, 10, 1], vertical_alignment='bottom')
    new_subject = col1.selectbox("Subject", entity_display_list, index=None, placeholder='Choose a subject')
    new_property = col2.selectbox("Property", st.session_state['onto_properties']['display'], index=None, placeholder='Choose a property')
    new_object = col3.selectbox("Object", entity_display_list, index=None, placeholder='Choose a object')

    # When new triple is validated
    if col4.button('✅', type='primary', key='create-triple'): 

        # It is mandatory to have subject, properties and object
        if not new_subject or not new_property or not new_object:
            st.warning('Can not create new triple: subject, property and object needs to be filled.')

        # Create the triple in the main graph
        else:
            # Extract new subject and object pks
            pk_subject = int(new_subject[new_subject.index('pk'):].replace('pk', '').replace(')', '').strip())
            subject_obj = list(filter(lambda entity: entity.pk == pk_subject, graph.entities))[0]
            pk_object = int(new_object[new_object.index('pk'):].replace('pk', '').replace(')', '').strip())
            object_obj = list(filter(lambda entity: entity.pk == pk_object, graph.entities))[0]
            # Find the pk property
            pk_property = int(onto_properties[onto_properties['display'] == new_property].iloc[0]['pk'])
            # Add the new triple to the graph
            graph.create_triple(subject_obj, pk_property, object_obj)
            # And then regenerate the graph dataframe
            st.session_state['graph_df'] = graph.to_dataframe()

            st.rerun()
