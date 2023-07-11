import streamlit as st
import application_assistant
import pickle

model = pickle.load(open('random_forest.pkl', 'rb'))

st.header('Question Pair Similarity')

q1 = st.text_input('Question 1')
q2 = st.text_input('Question 2')

if st.button('Check'):
    query = helper.query_point_creator(q1,q2)
    result = model.predict(query)[0]

    if result:
        st.header('Similar')
    else:
        st.header('Not quite similar!')


