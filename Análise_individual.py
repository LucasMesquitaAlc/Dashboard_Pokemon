import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv('DataframeModificado.csv')

pokemon_escolhido = st.text_input('Qual pokémon você deseja pesquisar?').title()
if pokemon_escolhido:

    try:
        numDoPok = df.loc[df['Nome'] == pokemon_escolhido].index[0]
        NomePokemon = df.iloc[numDoPok]['Nome']
        
        verificacao = True

    except IndexError:
        st.write('Pokemon não encontrado.')
        verificacao = False

    if verificacao == True:
        col1, col2, col3 = st.columns([1,1,1])  
        with col1:
            st.write("Sua geração:")
            st.write(f'{df.iloc[numDoPok]["Geração"]}ª geração')
        with col2:
            st.write(f'É lendário?')
            msg = "Sim, é lendário" if df.iloc[numDoPok]['Lendário?'] else "Não, não é lendário"
            st.write(msg)
        with col3:
            st.write(f'Tipagem:')
            st.write(f'{df.iloc[numDoPok]["Tipo 1"]}/{df.iloc[numDoPok]["Tipo 2"]}')


        #Gráfico de barra
        status = df.iloc[numDoPok].to_dict()
        lista = list(status.items())[4:10]
        status = dict(lista)

        fig, ax = plt.subplots()
        ax.bar(status.keys(), status.values(), color='skyblue', edgecolor='black')

        ax.set_title(f'{NomePokemon} - Total de: {df.iloc[numDoPok]["Total"]}')
        ax.set_xlabel('atributos')
        ax.set_ylabel('Valores')
        plt.grid(axis='y', linestyle='--', alpha=0.7)

        st.title("Status do Pokémon")
        plt.xticks(rotation=20, fontsize=12)
        st.pyplot(fig)


        #grafico de pizza
        fig, ax = plt.subplots() 
        ax.pie(status.values(), labels=status.keys(), autopct='%1.1f%%', startangle=140,
            colors=['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'salmon', 'lightblue', 'orange'])

        ax.set_title("Distribuição de atributos")
        st.pyplot(fig)  



        #grafico de radar

        categorias = list(status.keys())
        valores = list(status.values())
        num_vars = len(categorias)
        angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
        valores += valores[:1]
        angles += angles[:1]
        fig, ax = plt.subplots(figsize=(6, 6), dpi=100, subplot_kw=dict(polar=True))
        ax.plot(angles, valores, linewidth=2, linestyle='solid', label='Desempenho')
        ax.fill(angles, valores, color='blue', alpha=0.25)
        ax.set_yticklabels([])  
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(categorias)
        ax.set_title("Distribuição de atributos", size=20, weight='bold', va='bottom')

        st.pyplot(fig)

