#Primeiro importamos as bibliotecas (não esqueça de conferir o arquivo requirements.txt)

import streamlit as st
import pandas as pd
import plotly.express as px
import requests

#Acessando as URLs
url_mulheres = 'https://dadosabertos.camara.leg.br/api/v2/deputados?siglaSexo=F&ordem=ASC&ordenarPor=nome'
url_homens = 'https://dadosabertos.camara.leg.br/api/v2/deputados?siglaSexo=M&ordem=ASC&ordenarPor=nome'

#Fazendo as requisições
response_mulheres = requests.get(url_mulheres)
response_homens = requests.get(url_homens)

#Convertendo respostas JSON para DataFrames
dadosJSONmulheres = response_mulheres.json()
dadosJSONhomens = response_homens.json()

#Criando os DataFrames a partir da biblioteca pandas
df_mulheres = pd.DataFrame(dadosJSONmulheres['dados'])
df_homens = pd.DataFrame(dadosJSONhomens['dados'])

# Adicionando uma coluna de Sexo antes de combinar
df_mulheres['Sexo'] = 'Feminino'
df_homens['Sexo'] = 'Masculino'

# Concatenando ambos os DataFrames
df_total = pd.concat([df_mulheres, df_homens], ignore_index=True)

# Agrupando por UF e Sexo, contando o número de deputados (na aula 7 aprendemos o groupby!)
df_grouped = df_total.groupby(['siglaUf', 'Sexo']).size().reset_index(name='Quantidade')

#Verificando o DataFrame
st.write("Dados agrupados por UF e Sexo:", df_grouped)

# Criando o gráfico de barras empilhadas
fig = px.bar(
    df_grouped,
    x='siglaUf',
    y='Quantidade',
    color='Sexo',
    labels={'siglaUf': 'Unidade Federativa', 'Quantidade': 'Quantidade'},
    barmode='stack',  # Define gráfico empilhado
    title='Quantidade de Deputados por UF e Sexo'
)

# Exibindo o gráfico no Streamlit
st.plotly_chart(fig)
