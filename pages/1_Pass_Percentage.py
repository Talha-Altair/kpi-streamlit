import streamlit as st
import pandas as pd

st.set_page_config(page_title="Pass Percentage", page_icon="📊", initial_sidebar_state="expanded")

year = st.multiselect("Filter Year", [1,2,3,4], default=[1,2,3,4])

pass_data = pd.DataFrame({
    'Subject': ['Compiler', 'Green Design', 'SPM', 'Operating System', 'Cloud Computing'],
    'Pass Percentage': [76, 99, 97, 86, 82],
    'year': [1,2,2,3,3],
    'Subject Code': ['CS 201', 'CS 301', 'CS 401', 'CS 501', 'CS 601'],
})

pass_data = pass_data[pass_data['year'].isin(year)]

st.header("Pass Percentage Chart")
st.bar_chart(pass_data, x='Subject', y='Pass Percentage', width=1200, height=600)

st.header("Pass Percentage Table")
st.dataframe(pass_data)