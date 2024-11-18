import streamlit as st
import pandas as pd
st.info("Para visualizar o código com comentários, acesse o caderno 'Salinha_ProfaBruna_14_11_2024' ")

#Questão 1
st.title("Questão 1")
st.warning("A resolução desta questão está na lista 8: https://github.com/brunagmoura/salinha01_modulo3_ENAP/blob/main/lista8_streamlit.py")

st.divider()
#Questão 2

st.title("Questão 2")

#Confira a explicação detalhada no caderno "Salinha_ProfaBruna_14_11_2024"

df = pd.read_csv('https://raw.githubusercontent.com/adrianalite/datasets/main/BR_LQs_CD2022.csv')
df['Lat_d'] = pd.to_numeric(df['Lat_d'], errors='coerce')
df['Long_d'] = pd.to_numeric(df['Long_d'], errors='coerce')
estados = df['NM_UF'].unique()
estadoFiltro = st.selectbox(
    'Qual estado selecionar?',
     estados)
dadosFiltrados = df[df['NM_UF'] == estadoFiltro]
st.map(dadosFiltrados, latitude="Lat_d", longitude="Long_d")

#Podemos exibir a quantidade de municípios no Estado selecionado usando a função len(), que mede a quantidade de linhas
#de um dataframe
#Somado a ele, vamos usar o unique, que informa quantas ocorrências únicas existe em uma coluna

qtdeMunicipios = len(df['NM_MUNIC'].unique())
st.write("A quantidade de municípios com localização quilombola é " + str(qtdeMunicipios))

qtdeComunidades = len(df['NM_AGLOM'].unique())
st.write("A quantidade de comunidades quilombolas é " + str(qtdeComunidades))

st.header('Número de comunidades por UF - usando a função nativa do streamlit')
st.bar_chart(df['NM_UF'].value_counts())

st.header('Número de comunidades por UF - usando o plotly')
df_contagem = df['NM_UF'].value_counts().reset_index()
import plotly.express as px
fig = px.bar(
    df_contagem,
    x='NM_UF',
    y='count',
    title='Distribuição por Unidade Federativa',
    labels={'NM_UF': 'Unidade Federativa', 'count': 'Número de Registros'},
    text='count'  # Exibir os valores em cada barra
)
st.plotly_chart(fig)

#Podemos usar a função nativa do streamlit para fazer bar_chart
st.header('Os dez municípios com mais comunidades quilombolas - usando a função nativa do streamlit')
st.bar_chart(df['NM_MUNIC'].value_counts()[:10])


st.header('Os dez municípios com mais comunidades quilombolas - usando o plotly')
df_contagem_municipios = df['NM_MUNIC'].value_counts()[:10].reset_index()
fig_municipios = px.bar(
    df_contagem_municipios,
    x='NM_MUNIC',
    y='count',
    title='Distribuição por Unidade Federativa',
    labels={'NM_MUNIC': 'Unidade Federativa', 'count': 'Número de Registros'},
    text='count'  # Exibir os valores em cada barra
)
st.plotly_chart(fig_municipios)

st.header('Selecionar quantidade de linhas a serem exibidas')

numero_de_linhas = st.slider('Quantas linhas você deseja exibir?', min_value = 0, max_value = 100)
st.write(df.head(numero_de_linhas))
