#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px
from dash.dependencies import Input, Output
from jupyter_dash import JupyterDash
import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

import warnings
warnings.filterwarnings("ignore")

# Leia o arquivo CSV e faça as modificações necessárias
try:
    # Leia o arquivo CSV e faça as modificações necessárias
    df = pd.read_csv('/Users/batistajunior/Downloads/Desafio Técnico - Analista Jr. de Projetos com foco em Dados - Dados.csv', encoding='utf-8', delimiter=',')
    df = df.iloc[1:].reset_index(drop=True)
    df.columns = ['Método', 'Turma', 'Nome Completo', 'Fase Empresa', 'Faturamento Antes',
                  'Faturamento Depois', 'Empregos Gerados', 'Conexões Relevantes',
                  'Importância Acelerar', 'Importância Crescer Renda', 'Motivação e Comprometimento',
                  'Novas Ideias Soluções', 'Acesso Novos Clientes', 'Fazer Conexões Relevantes',
                  'Melhorar Competitividade', 'Ganhar Visibilidade', 'Satisfação Geral',
                  'Grau de Escolaridade', 'Auto Declaração', 'Gênero', 'Ramo do Negócio']

    # Verifique os valores nulos em cada coluna
    valores_nulos = df.isnull().sum()

    # Trate os valores nulos, se necessário
    # Se as colunas tiverem muitos valores nulos, você pode optar por preenchê-los ou remover as colunas.
    # Exemplo: Removendo colunas com mais de 50% de valores nulos
    limite_nulos = len(df) * 0.5
    df = df.dropna(thresh=limite_nulos, axis=1)

except Exception as e:
    print("Erro ao carregar o arquivo CSV:", str(e))

# Criação do Dash app
app = dash.Dash(__name__)

# Layout do dashboard
app.layout = html.Div(
    children=[
        html.H1('Dashboard de Análise de Startups', style={'text-align': 'center'}),
        
        html.H2('Distribuição dos Métodos (On-line e Presencial)'),
        dcc.Graph(
            figure=px.pie(df, names='Método', title='Distribuição dos Métodos', hole=0.3)
        ),
        
        html.H2('Distribuição das Startups em diferentes fases após o Programa'),
        dcc.Graph(
            figure=px.bar(df, x='Fase Empresa', title='Fase da Empresa após o Programa', 
                          labels={'Fase Empresa': 'Fase', 'index': 'Quantidade'}, color_discrete_sequence=px.colors.qualitative.Set2)
        ),

        html.H2('Faturamento Antes e Depois por Método'),
        dcc.Graph(
            figure=px.box(df, x='Método', y=['Faturamento Antes', 'Faturamento Depois'], title='Faturamento Antes e Depois do Programa',
                          labels={'Método': 'Método', 'value': 'Faturamento'}, color_discrete_sequence=px.colors.qualitative.Set1)
        ),

        html.H2('Importância das Características do Programa'),
        dcc.Graph(
            figure=px.box(df, y=['Importância Acelerar', 'Importância Crescer Renda', 'Motivação e Comprometimento',
                                 'Novas Ideias Soluções', 'Acesso Novos Clientes', 'Fazer Conexões Relevantes',
                                 'Melhorar Competitividade', 'Ganhar Visibilidade'], title='Importância das Características do Programa',
                          labels={'value': 'Importância'}, color_discrete_sequence=px.colors.qualitative.Pastel)
        ),

        html.H2('Satisfação Geral com a Metodologia do Programa'),
        dcc.Graph(
            figure=px.histogram(df, x='Satisfação Geral', title='Satisfação Geral com a Metodologia do Programa',
                                labels={'Satisfação Geral': 'Nível de Satisfação', 'index': 'Quantidade'}, color_discrete_sequence=px.colors.qualitative.Safe)
        ),

        html.H2('Visualização de empregos gerados em cada método'),
        dcc.Graph(
            figure=px.bar(df, x='Método', y='Empregos Gerados', title='Empregos Gerados em cada Método', 
                          labels={'Método': 'Método', 'Empregos Gerados': 'Quantidade de Empregos'}, color_discrete_sequence=px.colors.qualitative.Set3)
        ),

        html.H2('Visualização da distribuição por grau de escolaridade'),
        dcc.Graph(
            figure=px.histogram(df, x='Grau de Escolaridade', title='Distribuição por Grau de Escolaridade',
                                labels={'Grau de Escolaridade': 'Grau de Escolaridade', 'index': 'Quantidade'}, color_discrete_sequence=px.colors.qualitative.Set2)
        ),

        html.H2('Visualização da distribuição por gênero'),
        dcc.Graph(
            figure=px.pie(df, names='Gênero', title='Distribuição por Gênero', hole=0.3, color_discrete_sequence=px.colors.qualitative.Pastel)
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)


# In[ ]:




