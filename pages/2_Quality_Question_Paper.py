import streamlit as st
import altair
import pandas as pd

st.set_page_config(page_title="Quality_Question_Paper", page_icon="📊", initial_sidebar_state="expanded")

exam = st.multiselect("Filter exam type", ["CAT1","CAT2","ENDSEM"], default=["CAT1","CAT2","ENDSEM"])

qp_data = pd.DataFrame({
    'Subject': ['Compiler', 'Green Design', 'SPM', 'Operating System', 'Cloud Computing'],
    'year': [1,2,2,3,3],
    'Subject Code': ['CS 201', 'CS 301', 'CS 401', 'CS 501', 'CS 601'],
    'CAT1': [76, 99, 97, 86, 82],
    'CAT2': [76, 99, 97, 86, 82],
    'ENDSEM': [76, 99, 97, 86, 82],
})

df = pd.DataFrame({
    'Exam': ['CAT1', 'CAT2', 'ENDSEM'],
    'Compiler': [40, 90, 35],
    'Green Design': [70, 31, 75],
    'SPM': [83, 85, 90],
    'Operating System': [36, 52, 96],
    'Cloud Computing': [76, 99, 57],
})

df = df[df['Exam'].isin(exam)]

st.line_chart(df, x='Exam', y=['Compiler', 'Green Design', 'SPM', 'Operating System', 'Cloud Computing'])

st.dataframe(df)