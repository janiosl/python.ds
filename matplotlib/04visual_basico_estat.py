# -*- coding: utf-8 -*-
"""
Visualização de dados com incorporação de cálculos estatísticos
Biblioteca:
    Matplotlib
    Pandas
    Numpy
"""
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

"""
Incorporação de informações estatística dos dados no gráfico
"""
#Criação de séries de dados de exemplo
np.random.seed(1234) #Esta linha garante a repetiação dos dados de exemplo
dados = pd.Series(np.arange(10))
dados2 = pd.Series(np.arange(9, -1, -1))
dados3 = pd.Series(np.random.randn(33))


"""
Exemplo 1
Gráfico de linhas com média plotada como uma reta
"""
#Média das observações de dados2
media = dados3.mean()
media

#Acrescentando mais de uma linha no mesmo gráfico
#Plotagem dos dados no gráfico
plt.plot(dados3,
         color='g')

plt.plot([media for k in range(0, len(dados3))],
         'b:')

#Elementos auxiliares no gráfico
#Título
plt.title('Histórico dos valores')

#Legenda dos dados
plt.legend(['Dados 3', 'Média'],
           loc='best',
           fontsize='small')

#Legenda dos eixos
plt.ylabel('Valores',
           fontsize='small')
plt.xlabel('Tempo',
           fontsize='small')


"""
Exemplo 2
#Geração de uma análise gráfica de disperção entre dados e dados2
"""
#Gráfico para apoio na análsie estatística

plt.scatter(dados, dados2,
            color='orange')
plt.title('Disperção de dados e dados2')


#Inserindo anotações sobre os dados
plt.scatter(dados, dados2,
            color='orange')
plt.title('Disperção de dados e dados2')

cor = dados.corr(dados2)
cor = str(f'{cor:.3f}')

plt.annotate('Correlação: ' + cor,
             xy=(4, 6))


"""
Exemplo 3
#Geração de uma análise histograma de um conjunto de dados
"""

#Criação de uma série de dados de exemplo com Distribuição Normal
np.random.seed(1234)
dados4 = pd.Series(np.random.randn(1000))

#Geração do histograma de dados3 com frequências calculadas automáticas
plt.hist(dados4)

#Geração do histograma com classes arbitradas pelo analista
plt.hist(dados4,
         bins=20) #Quantidade de classes
