import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('DataframeModificado.csv')

st.title('Análise de atributos:')

col1, col2 = st.columns([1, 1])  
with col1:
    atributo = st.selectbox('Escolha um atributo:',('...','Vida','Ataque','Defesa','Atq. especial','Def. especial','Velocidade','Total'))
with col2:
    geracao = st.selectbox('Escolha a geração:',('...','Todas as gerações',1,2,3,4,5,6,7,8))
    if geracao == 'Todas as gerações':
        geracao = [1,2,3,4,5,6,7,8]
    else:
        geracao = [geracao]

parametro = st.radio(
    "Selecione o parâmetro da análise comparativa: ",
    ["***Média***", "***Máximo***", "***Mínimo***"],
    index=None,horizontal=True
)
if not parametro:
    parametro = 'Média'

if atributo != '...' and geracao != '...':
    parametro = parametro.strip('***')


    Tipos = ['Normal','Fire','Water','Grass','Flying','Fighting','Poison','Electric','Ground','Rock','Ice','Bug','Psychic','Ghost','Steel','Dragon','Dark','Fairy']
    dicionario_filtro = dict()
    for tipo in Tipos:
        filtro = df[((df['Tipo 1'] == tipo) | (df['Tipo 2'] == tipo)) & (df['Geração'].isin(geracao))]

        media = round(filtro[atributo].mean(),1)
        maximo = filtro[atributo].max()
        minimo = filtro[atributo].min()
        
        dicionario_filtro[tipo] = [media,maximo,minimo]

    escolha = 0
    if parametro == "Média":
        escolha = 0
    elif parametro == "Máximo":
        escolha = 1
    else:
        escolha = 2


    #Gráfico de barra
    valores = [dicionario_filtro[tipo][escolha] for tipo in Tipos]

    # Plotando o gráfico de barras
    fig, ax = plt.subplots()
    ax.bar(Tipos, valores, color='skyblue', edgecolor='black')
    ax.set_title(f'{parametro} de {atributo} por Tipo')
    ax.set_xlabel('Tipo de Pokémon')
    ax.set_ylabel(f'{parametro} de {atributo}')
    plt.xticks(rotation=45, fontsize=8)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Exibindo no Streamlit
    st.title(f"Gráfico de {parametro} por Tipo")
    st.pyplot(fig)