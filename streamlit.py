import streamlit as st

st.write("Sou servidor público")

numero = st.slider('Selecionar um número', min_value=0, max_value=100, label_visibility="hidden")
st.text(f'Seu número é {numero}')



st.color_picker('Escolha sua cor favorita')
