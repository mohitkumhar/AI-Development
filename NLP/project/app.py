import streamlit as st
import helper
import pickle

model = pickle.load(open('model.pkl','rb'))

st.header('Duplicate Question Pairs')

q1 = st.text_input(label='Enter Question 1')
q2 = st.text_input(label='Enter Question 2')

if st.button('Find'):
    query = helper.query_point_creator(q1, q2)
    prediction = model.predict(query)
    
    if prediction:
        st.header('Duplicate')
    else:
        st.header('Not Duplicate')

