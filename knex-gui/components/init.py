import streamlit as st

def init(layout='centered'):
    st.set_page_config(page_icon=':link:', page_title='Knex GUI', layout=layout)

    # Change CSS
    st.markdown("""
        <style>
        button[kind="primary"] {
            background: none!important;
            border: none;
            padding: 0!important;
            color: #66f !important;
            text-decoration: none;
            cursor: pointer;
            border: none !important;
            text-align:left
        }
        button[kind="primary"]:hover {
            text-decoration: none;
            color: #aaf !important;
        }
        button[kind="primary"]:focus {
            outline: none !important;
            box-shadow: none !important;
            color: #ccf !important;
        }
        button[kind="secondary"]:hover {
            color: #aaf !important;
            border-color: #aaf !important;
        }
        button[kind="secondary"]:focus {
            outline: none !important;
            box-shadow: none !important;
            color: #ccf !important;
            border-color: #ccf !important;
        }
        </style>
        """, unsafe_allow_html=True)