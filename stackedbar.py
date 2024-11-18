import streamlit as st
import pandas as pd
import plotly.express as px
import requests

url_mulheres = 'https://dadosabertos.camara.leg.br/api/v2/deputados?siglaSexo=F&ordem=ASC&ordenarPor=nome'
url_homens = 'https://dadosabertos.camara.leg.br/api/v2/deputados?siglaSexo=M&ordem=ASC&ordenarPor=nome'

response_mulheres = requests.get(url_mulheres)
response_homens = requests.get(url_homens)

data_mulheres = response_mulheres.json()
data_homens = response_homens.json()

df_mulheres = df_mulheres['siglaUf'].value_counts().reset_index()
#Temos que contar a quantidade de mulheres por UF
df_mulheres.columns = ['UF', 'Quantidade']
df_mulheres['Sexo'] = 'Feminino'

df_homens = df_homens['siglaUf'].value_counts().reset_index()
#Temos que contar a quantidade de homens por UF
df_homens.columns = ['UF', 'Quantidade']
df_homens['Sexo'] = 'Masculino'

df = pd.concat([df_mulheres, df_homens])

st.write(df)

fig = px.bar(
    df,
    x='UF',
    y='Quantidade',
    color='Sexo',
    labels={'Quantidade': 'Quantidade', 'UF': 'Unidade Federativa'},
    barmode='stack'  # Define o gráfico como empilhado
)

st.plotly_chart(fig)
