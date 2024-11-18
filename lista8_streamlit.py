import streamlit as st
import pandas as pd

#Questão 1:
st.title("Questão 1")
st.write("Sou servidor público")

st.divider()
#Questão 2:
st.title("Questão 2")

#Aqui vamos usar as formatações de texto padrões do streamlit
#Eu amo a documentação da página oficial do streamlit, eles trazem vários exemplos e aplicações com imagens:
#https://docs.streamlit.io/develop/api-reference/write-magic/st.write

#Título
st.title("Este é o título do app")

#Subtítulo
st.header("Este é o subtítulo")

#Sub-sub-título
st.subheader("Este é o terceiro subtítulo")

#Texto markdown
st.markdown("Este é texto")

#Legenda para gráficos
st.caption("Esta é a a legenda")

#Código
st.code("x=2021")

#E ainda podemos usar latex!
st.latex(r''' a+a r^1+a r^2+a r^3 ''')

st.divider()
#Questão 3:
st.title("Questão 3")

st.write("Slider: ")
#Usamos min_value como o valor mínimo do nosso seletor e max_value como valor máximo do seletor

numero = st.slider('Selecione um número', min_value = 0, max_value = 100) 
st.text("Seu número é " + str(numero))

#Outra opção:
#st.text(f'Seu número é {numero}')

st.divider()
#Questão 4:
st.title("Questão 4")

st.header("Interagir com a aplicação")

st.subheader("Caixa de seleção")
x = st.checkbox('Sim')
st.write(x)

st.subheader("Botão")
if st.button('Clique'):
    st.write('Botão clicado!')

st.subheader("Seleção em uma lista")
genero = st.radio('Selecione seu gênero', ['Masculino', 'Feminino'])
st.write(f'Você escolheu: {genero}')

st.subheader("Seleção única em uma lista suspensa")
genero = st.selectbox('Selecione seu gênero', ['Masculino', 'Feminino'])
st.write(f'Você escolheu: {genero}')

st.subheader("Seleção múltipla em uma lista")
deptos = st.multiselect('Escolha um departamento', ['DCS', 'DE', 'DIR'])
st.write('Você escolheu:', deptos)

st.subheader("Seleção de uma lista, mas usando o slider como seletor")
resposta = st.select_slider('Selecione uma resposta', ['Ruim', 'Bom', 'Excelente'])
st.write(f'Você selecionou: {resposta}')

st.subheader("Seleção usando o slider, mas em um intervalo numérico")
numero = st.slider('Selecione um número', 0, 50)
st.write(f'Você selecionou: {numero}')

st.subheader("Entrada numérica com botões para aumentar ou diminuir um valor")
num = st.number_input('Selecione um número', 0, 10)
st.write(f'Número escolhido: {num}')

st.subheader("Entrada textual")
email = st.text_input('Endereço de e-mail')
st.write(f'E-mail inserido: {email}')

st.subheader("Selecionar uma data")
data = st.date_input('Data de viagem')
st.write(f'Data escolhida: {data}')

st.subheader("Selecionar um horário")
tempo = st.time_input('Tempo de escola')
st.write(f'Tempo selecionado: {tempo}')

st.subheader("Inserir várias linhas")
descricao = st.text_area('Descrição')
st.write(f'Descrição fornecida: {descricao}')

st.subheader("Fazer upload de uma foto")
foto = st.file_uploader('Atualize uma foto')
if foto:
    st.image(foto)

st.subheader("Selecionar uma cor")
cor = st.color_picker('Escolha sua cor favorita')
st.write(f'A cor escolhida foi: {cor}')

st.header("Mensagens de status")

st.subheader("Mensagem de sucesso")
st.success("Você conseguiu!")

st.subheader("Mensagem de erro")
st.error("Erro!")

st.subheader("Mensagem de aviso")
st.warning("Advertência")

st.subheader("Mensagem informativa")
st.info("Esta é uma informação")

st.divider()
#Questão 5:
st.title("Questão 5")

#Primeiro passo: criar o DataFrame com as servidoras e os salários
df = pd.DataFrame({
    'nomeServidor': ['Adriana', 'Monica', 'Samara'],
    'salario': [1200,300,5000]
})

#Segundo passo: exibir a tabela com a base de dados
st.header("Base de dados que criamos")
st.write(df)

st.header("Caixa de seleção")
#Esse é o código padrão:
#opcao = st.selectbox(
#    'Qual servidor você gostaria de selecionar?',
#     df['nomeServidor'])

#Mas podemos melhorá-lo, incluindo o comando "Selecione um servidor"

#Para isso, vamos criar uma lista de opções possíveis. Essas opções serão o comando "Selecione um servidor" ou 
#O nome dos servidores da coluna "nomeServidor" do nosso DataFrame

lista_de_opcoes = ['Selecione um servidor'] + df['nomeServidor'].tolist()
opcao = st.selectbox(
    'Qual servidor você gostaria de selecionar?',
    lista_de_opcoes
)

st.write('Você selecionou: ', opcao)

#Terceiro passo: filtrar apenas o servidor escolhido
#Qual a base de dados que queremos filtrar? df! E vamos filtrar a partir de qual coluna? nomeServidor
#Por isso vamos começar com df['nomeServidor']
#O que queremos filtrar? a opcao escolhida, que está armazenada como "opcao"
#Por isso vamos usar: df['nomeServidor'] == opcao
#Finalmente, queremos aplicar este filtro na base de dados df
#Por isso: df[df['nomeServidor'] == opcao]

st.header("Exibir apenas o servidor selecionado")
dfFiltrado = df[df['nomeServidor'] == opcao]
st.write(dfFiltrado)

st.divider()
#Questão 6

st.title("Questão 6")

st.header("Atividade 1")
#Primeiro passo: importar a base de dados usando o pandas
df = pd.read_csv('https://raw.githubusercontent.com/adrianalite/datasets/main/BR_LQs_CD2022.csv')

#Segundo passo: implementar um slider para que o usuário escolha quantas linhas ele quer visualizar no DataFrame
#Aprendemos que o comando df.head() pode receber como parâmetro a quantidade de linhas a serem exibidas
#Por exemplo: df.head(5) exibe as 5 primeiras linhas do data frame
#Podemos fazer com que esse 5 seja um número dinâmico, de modo que o próprio usuário deverá fazer essa escolha

numero_de_linhas = st.slider('Quantas linhas você deseja exibir?', min_value = 0, max_value = 100) #Aqui colocamos 
#Em min_value o valor mínimo que o usuário pode escolher e max_value o valor máximo que o usuário pode escolher
#Finalmente, aplicamos no nosso df.head: df.head(numero_de_linhas).
#Para exibir no streamlit não podemos esquecer de usar o st.write. Assim:

st.write(df.head(numero_de_linhas))

st.header("Atividade 2")
#Para construir o gráfico, podemos usar a função nativa bar_chart
st.subheader("Usando a função nativa do streamlit bar_chart")

#Para essa atividade vamos usar o comando value_counts, que exibe a qantidade de ocorrências de uma determinada informação
#Qual informação/coluna desejamos calcular a quantidade de ocorrências? NM_UF!
#Por isso, usamos df['NM_UF']
#Ficará assim:

qtde_comunidades_estado = df['NM_UF'].value_counts()
st.write(qtde_comunidades_estado)

#Agora plotamos com a função nativa "bar_chart"
st.bar_chart(df['NM_UF'].value_counts())

st.subheader("Usando a biblioteca plotly")
#Infelizmente com o bar_chart não conseguimos personalizar os títulos dos eixos, mas podemos usar o plotly junto com o streamlit
#Parece que a função nativa bar_chart também tem um problema coma  ordenação das informações. Usando o plotly também conseguimos atacar
#Este problema

#Ficaria assim:

df_contagem = df['NM_UF'].value_counts().reset_index()
#Porque usar o reset_index? Usamos o reset_index porque quando montamos a base de dados com o value_counts, o Python considera
#Que a NM_UF não é uma simples coluna, mas sim o "index" do DataFrame
#Quando usamos o reset_index(), nós fazemos com que NM_UF vire uma coluna como outra qualquer!

#ATENÇÃO: Não podemos esquecer de importar o plotly

import plotly.express as px
fig = px.bar(
    df_contagem,
    x='NM_UF',
    y='count',
    labels={'NM_UF': 'Unidade Federativa', 'count': 'Número de Registros'},
    title='Distribuição por Unidade Federativa'
) #Criar o gráfico com o plotly

st.plotly_chart(fig) #Exibir o gráfico no streamlit
