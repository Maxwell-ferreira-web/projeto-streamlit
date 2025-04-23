import streamlit as st
import pandas as pd

# Aqui, como NÃO VAMOS TRABALHAR COM GRANDES MASSAS DE DADOS, nem precisa usar aquela função com DECORATOR,
# vista em aulas anteriores.

dados = pd.read_csv('clientes.csv') # Veja que aqui, mesmo fazendo a leitura em uma pasta diferente (pq
                                    # 'Consulta.py' está na Pasta "pages" e 'clientes.csv' está na raiz),
                                    # não precisa colocar o caminho do arquivo 'clientes.csv', pq o Streamlit
                                    # já faz isso internamente pra gente.

st.title('Clientes cadastrados')
st.divider()

st.dataframe(dados)