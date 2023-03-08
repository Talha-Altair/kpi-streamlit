import streamlit as st

st.set_page_config(page_title="Notes", page_icon="📊", initial_sidebar_state="expanded")

with open("docs.txt", "r") as f:
    notes = f.read()

    st.text(notes)