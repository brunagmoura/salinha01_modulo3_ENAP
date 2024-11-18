import streamlit as st
import pandas as pd
#Questão 1
st.title("Questão 1")
st.warning("A resolução desta questão está na lista 8: https://github.com/brunagmoura/salinha01_modulo3_ENAP/blob/main/lista8_streamlit.py")

st.divider()
#Questão 2

st.title("Questão 2")

df = pd.read_csv('https://raw.githubusercontent.com/adrianalite/datasets/main/BR_LQs_CD2022.csv')
df['Lat_d'] = pd.to_numeric(df['Lat_d'], errors='coerce')
df['Long_d'] = pd.to_numeric(df['Long_d'], errors='coerce')
estados = df['NM_UF'].unique()
estadoFiltro = st.selectbox(
    'Qual estado selecionar?',
     estados)
dadosFiltrados = df[df['NM_UF'] == estadoFiltro]
st.map(dadosFiltrados, latitude="Lat_d", longitude="Long_d")


qtdeMunicipios = len(df['NM_MUNIC'].unique())
st.write("A quantidade de municípios com localização quilombola é " + str(qtdeMunicipios))

qtdeComunidades = len(df['NM_AGLOM'].unique())
st.write("A quantidade de comunidades quilombolas é " + str(qtdeComunidades))
st.header('Número de comunidades por UF')
st.bar_chart(df['NM_UF'].value_counts())
st.header('Os dez municípios com mais comunidades quilombolas')
st.bar_chart(df['NM_MUNIC'].value_counts()[:10])
numero = st.slider('Selecione um número de linhas a serem exibidas', min_value = 0, max_value = 100)
st.write(df.head(numero))
