import streamlit as st

#Questão 1:
st.title("Questão 1")
st.write("Sou servidor público")

st.divider()
#Questão 2:
st.title("Questão 1")

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

#Questão 4:
