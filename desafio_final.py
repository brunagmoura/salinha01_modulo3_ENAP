#Bibliotecas

import requests
import pandas as pd
import plotly.express as px

#Manipulação da base de dados
st.warning("Para o código comentado, consulte o caderno "Salinha_ProfaBruna_18_11_2024")

url_mulheres = 'https://dadosabertos.camara.leg.br/api/v2/deputados?siglaSexo=F&ordem=ASC&ordenarPor=nome'
resposta_mulheres = requests.get(url_mulheres)
dadosJSONmulheres = resposta_mulheres.json()
df_mulheres = pd.DataFrame(dadosJSONmulheres['dados'])
df_mulheres['Sexo'] = "Feminino"

url_homens = 'https://dadosabertos.camara.leg.br/api/v2/deputados?siglaSexo=M&ordem=ASC&ordenarPor=nome'
resposta_homens = requests.get(url_homens)
dadosJSONhomens = resposta_homens.json()
df_homens = pd.DataFrame(dadosJSONhomens['dados'])
df_homens['Sexo'] = "Masculino"

df_total = pd.concat([df_mulheres, df_homens])

st.title("Base de dados")
st.header("Base de dados completa")
st.write(df_total)

df_total_agregado = df_total.groupby(['siglaUf', 'Sexo'])['id'].count().reset_index()
df_total_agregado = df_total_agregado.rename(columns={'siglaUf': 'UF', 
                                                      'id': 'Contagem'})

st.header("Base de dados agregada por Estado e por Sexo")
st.write(df_total_agregado)

# Criando o gráfico de barras empilhadas
fig_barras = px.bar(
    df_grouped,
    x='siglaUf',
    y='Quantidade',
    color='Sexo',
    labels={'siglaUf': 'Unidade Federativa', 'Quantidade': 'Quantidade'},
    barmode='group', #Gráfico de barras
    title='Quantidade de Deputados por UF e Sexo (barras)'
)

fig_barras_empilhadas = px.bar(
    df_grouped,
    x='siglaUf',
    y='Quantidade',
    color='Sexo',
    labels={'siglaUf': 'Unidade Federativa', 'Quantidade': 'Quantidade'},
    barmode='stack', #Gráfico de barras empilhadas
    title='Quantidade de Deputados por UF e Sexo (barras empilhadas)'
)

# Exibindo o gráfico no Streamlit
st.title("Exibições gráficas")
st.header("Gráfico de barras)
st.plotly_chart(fig_barras)
st.plotly_chart(fig_barras_empilhadas)

st.title("Utilizando o select box para que o usuário possa escolher um determinado Estado")

#Selectbox para seleção do estado
#Primeiro fazemos a lista de opções. O unique() é utilizado para mostrar as ocorrências únicas de uma determinada coluna.

opcoes = df_total_agregado['UF'].unique()

estado_selecionado = st.selectbox(
    "Selecione o estado que deseja visualizar:", #mensagem de texto
    opcoes, #opções do selectbox
    index=0  #define o primeiro estado como padrão
)

#Depois filtramos os dados pelo estado selecionado
df_filtrado = df_total_agregado[df_total_agregado['UF'] == estado_selecionado]

#Agora criamos o gráfico de barras empilhadas
fig_barras = px.bar(
    df_filtrado,
    x='UF',
    y='Contagem',
    color='Sexo',
    labels={'UF': 'Unidade Federativa', 'Contagem': 'Quantidade'},
    barmode='stack', 
    title=f'Quantidade de Deputados por Sexo no Estado {estado_selecionado}' #Aqui colocamos o estado_selecionado como um parâmetro, que é o definido na caixa de seleção
)

st.plotly_chart(fig_barras_empilhadas)

