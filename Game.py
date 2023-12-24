import streamlit as st
import random
st.title('Guessing number')
r = random.randint (1,10)
User_Input = st.slider('User_Input', min_value=0, max_value=10)
if st.button('Output'):
    Result = 'Congratulation!You won game' if r == User_Input else 'Better luck next time'
    st.write(Result)
    