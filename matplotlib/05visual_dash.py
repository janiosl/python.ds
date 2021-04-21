# -*- coding: utf-8 -*-
"""
Visualização de dados com visual tabular/painel/subplots
Biblioteca:
    Matplotlib
    Pandas
    Numpy
    Seaborn
"""
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

"""
Incorporação de informações estatística dos dados no gráfico
"""
#Criação de séries de dados de exemplo
dados = pd.Series(np.arange(10))
dados2 = pd.Series(np.arange(9, -1, -1))
dados3 = pd.Series(np.random.randn(33))
dados4 = pd.Series(np.random.randn(1000))

#Média das observações de dados2
media = dados3.mean()
media

"""
Gráficos plotados em uma visão tabular/painel
Útil para análise de diferentes aspectos de um processo
"""

#Criar uma área para plotagem de gráficos lado a lado (2 x 2)
fig, axes = plt.subplots(2, 2, sharex=True)

"""
Cada área de plotagem é identificada por um axe no formato de matrix
Exemplo
a primeira área superior esquerda é axes[0,0]
A última inferior direita é axes[2,2]
"""

#Plotando um gráfico na primeira área do painel
#Criando área do painel
fig, axes = plt.subplots(2, 2)

#Plotando primeiro gráfico
axes[0, 0].plot(dados3, color='g')
axes[0, 0].plot([media for k in range(0, len(dados3))], 'b:')
axes[0, 0].set_title('Histórico dos valores', fontsize='small')
axes[0, 0].set_xticks([0, 15, 30])
axes[0, 0].legend(['Dados 3', 'Média'],
           loc='best',
           fontsize='small')


#Plotando segundo gráfico
axes[0, 1].scatter(dados, dados2, color='orange')
axes[0, 1].set_title('Disperção de dados e dados2', fontsize='small')
axes[0, 1].annotate('Correlação: ' + str(round(dados.corr(dados2), ndigits=5)),
             xy=(2, 8))

#Plotando 2 últimos gráficos de forma simples
axes[1, 0].hist(dados4)

axes[1, 1].hist(dados4, bins=4)

#Ajustes visuais
sns.despine()
#Espaço entre plots no boxe
plt.subplots_adjust(hspace=0.25)

nome = 'grafico_dash.png'
plt.savefig(nome, #Nome
            dpi=400, #Resolução
            bbox_inches='tight' #Espaços em branco
            )
