import streamlit as st
import pandas as pd

#Questão 1
st.title("Questão 1")

df = pd.DataFrame({
    'nomeServidor': ['Adriana', 'Monica', 'Samara'],
    'salario': [1200,300,5000]
})

st.write("Criando uma tabela!")
st.write(df)
opcao = st.selectbox(
    'Qual servidor você gostaria de selecionar?',
     df['nomeServidor'])

st.write('Você selecionou: ', opcao)

dadosFiltrados = df[df['nomeServidor'] == opcao]
dadosFiltrados

#Questão 2

st.title("Questão 2")

df = pd.read_csv('https://raw.githubusercontent.com/adrianalite/datasets/main/BR_LQs_CD2022.csv')

st.header('Os dez municípios com mais comunidades quilombolas')
st.bar_chart(df['NM_MUNIC'].value_counts().head(10).sort_values(ascending=True))






















