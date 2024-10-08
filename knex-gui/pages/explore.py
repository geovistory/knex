import streamlit as st
from components.init import init
from components.menu import menu
from components.create_entity import create_entity
from components.create_triple import create_triple


# Initialize the page
init(layout='wide')

# Display the left menu
menu()


#### NO GRAPH IN MEMORY ####

if 'graph' not in st.session_state:
    st.title("Explore graph")
    st.write('No graph is loaded')
    if st.button('Go to graph loading page'):
        st.switch_page("pages/graph.py")


#### DISPLAY GRAPH ####

else: 
    # Init State: Selected entity history
    if 'selected_entity_history' not in st.session_state:
        st.session_state['selected_entity_history'] = []
    # Init State: Delete triple confirmation
    if 'delete' not in st.session_state:
        st.session_state['delete'] = False


    # Load the graph instance from state (for editing)
    graph = st.session_state['graph']
    # Load the graph dataframe from state (for displays and usage)
    graph_df = st.session_state['graph_df']
    # Load the ontology from state
    onto_properties = st.session_state['onto_properties']


    # Get the name of all entities
    entity_display_list = list(map(lambda ent: ent.get_display(), graph.entities))
    

    # Page title
    col1, col2 = st.columns([5, 10])
    col1.title("Explore graph of:")
    st.write('')
    st.write('')


    # Entity history breadcrumbs
    st.write('History breadcrumbs')
    history_cols = st.columns(5, vertical_alignment='center')
    for i, entity_display in enumerate(st.session_state['selected_entity_history']):
        # On click on a breadcrumbs
        if history_cols[i].button(entity_display, key=f"history-{entity_display}"): 
            # If the entity has triple select the entity as main
            if entity_display in entity_display_list:
                st.session_state['selected_entity'] = entity_display
            # Else inform that there is nothing for this entity
            else: 
                st.session_state['selected_entity'] = entity_display
                st.write('This entity has no more triples in the graph')
    st.write('')
    st.markdown('---')

    # If at this point an entity is already set as selected (eg via click on breakcrumbs, or click on an entity), it should be filled automatically

    index = None if 'selected_entity' not in st.session_state else entity_display_list.index(st.session_state['selected_entity'])
    # Select the entity to display
    selected_display = col2.selectbox("Select an entity:", entity_display_list, index=index, placeholder='Choose an entity')

    # The entity graph
    if selected_display:
        st.session_state['selected_entity'] = selected_display

        # Add to the history list: only if not already present
        if selected_display not in st.session_state['selected_entity_history']:
            st.session_state['selected_entity_history'].append(selected_display)
            # If there is more than 5 records in history, remove the first one (fifo)
            if len(st.session_state['selected_entity_history']) > 5: 
                st.session_state['selected_entity_history'] = st.session_state['selected_entity_history'][-5:]
            st.rerun()


        # Select the lvl 1 graph for the entity
        selected_graph = graph_df[(graph_df['subject_display'] == selected_display) | (graph_df['object_display'] == selected_display)].copy()
        selected_graph.sort_values(['property'], inplace=True)


        # Safe guard in case their is no triple for this entity
        if len(selected_graph) == 0: 
            st.write("This entity has no statements")
        else: 

            # Display the graph (triple list)
            for _, row in selected_graph.iterrows():
                col1, col2, col3, col4 = st.columns([10, 10, 10, 1], vertical_alignment='center')

                # Subject
                with col1: 
                    # If the subject is the main entity, displays it normally
                    if row['subject_display'] == selected_display: 
                        st.write(row['subject_display'])

                    # Else display a button to allow naviguation
                    else:
                        if st.button(row['subject_display'], type='primary'):
                            st.session_state['selected_entity'] = row['subject_display']
                            st.rerun()

                # Property: always display normally
                with col2: 
                    st.write(f"{row['property_label']}")

                # Object
                with col3: 
                    # If the object is the main entity, displays it normally
                    if row['object_display'] == selected_display: 
                        st.write(row['object_display'])
                    # Else display a button to allow naviguation
                    else:
                        if st.button(row['object_display'], type='primary'):
                            st.session_state['selected_entity'] = row['object_display']
                            st.rerun()


                # Delete button (with verificaiton)
                if col4.button('🗑️', key=f"{row['subject']}-{row['property']}-{row['object']}", type='primary'):
                    st.warning('You are about to delete this triple, make sure you really want to delete it, then click again on the same icon')

                    # On first click, prepare the deletion for this row only
                    if st.session_state['delete'] != (row['subject'], row['property'], row['object']):
                        st.session_state['delete'] = (row['subject'], row['property'], row['object'])

                    # On second click, remove the statement and rerun
                    else:
                        # Remove the triple from the graph
                        graph.delete_triple(row['subject'], row['property'], row['object'])
                        # And then regenerate the graph dataframe
                        st.session_state['graph_df'] = graph.to_dataframe()

                        st.rerun()
                st.write('')


    # Additional feature: Add a triple to the graph
    create_triple(entity_display_list, graph, onto_properties)

    # Additional feature: Add a triple to the graph
    create_entity(graph)


