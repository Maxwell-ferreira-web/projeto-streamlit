import streamlit as st
import pandas as pd
from datetime import date

# Aqui, vamos colocar uma validação dos dados a serem inputados...
def gravar_dados(nome, dt_nasc, tipo):
    if nome and dt_nasc <= date.today():
        with open('clientes.csv', 'a', encoding='utf-8') as file: # Atenção! Esse "a" é de APEND (UM COMANDO DE GRAVAÇÃO no array).
            file.write(f"{nome}, {dt_nasc}, {tipo}\n") # Atenção! Esse "\n" é para dar uma quebra de linha.
        st.session_state['Sucesso'] = True
    else:
        st.session_state['Sucesso'] = False
        

st.set_page_config(
    page_title='Cadastro de Clientes',
    page_icon='✔' # Clique entre as aspas: Tecla Windows + .
)

st.title('Cadadastro de Clientes')
st.divider() # Cria uma linha decorativa (questão de estética) após o título acima

nome = st.text_input('Digite o nome do cliente',
                     key='nome_cliente')

dt_nasc = st.date_input('Data nascimento', format='DD/MM/YYYY')

tipo = st.selectbox('Tipo do cliente',
                    ['Pessoa física', 'Pessoa jurídica'])

botao_cadastro = st.button('Cadastrar',
                           on_click=gravar_dados, # ao clicar no botão, chama a função criada lá em cima.
                           args=[nome, dt_nasc, tipo]) # isso é uma lista com os parâmentros que vamos passar pra função. 

# Aqui, uma verificação se cliquei no botão...
if botao_cadastro:
    if st.session_state['Sucesso']:
        st.success('Ciente cadastrado com sucesso!',
                   icon='🚀')
    else:
        st.error('Houve algum problema no cadastro!',
                 icon='❌')