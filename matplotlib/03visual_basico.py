# -*- coding: utf-8 -*-
"""
Visualização de dados - Ações básicas
Biblioteca:
    Matplotlib
    Pandas
    Numpy
"""
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

"""
Exemplo 1
Criação de gráficos simples
"""
#Criação de uma série de dados de exemplo
dados = pd.Series(np.arange(10))

#Geração de um gráfico simples com uma reta ascendente
plt.plot(dados)

#Criação de outra série de dados de exemplo
dados2 = pd.Series(np.arange(9, -1, -1))

plt.plot(dados2,
         color='r') #Cor da linha

"""
Exemplo 2
Personalizando as informações dos gráficos
"""
#Mais elementos do gráfico
plt.plot(dados2,
         color='g') #Cor da linha

plt.title('Aniversário Python.DS') #Título
plt.ylabel('Valores') #Legenda do eixo Y
plt.xlabel('Linha do Tempo') #Legenda do eixo X

plt.show()


#Acrescentando mais de uma linha no mesmo gráfico
plt.plot(dados,
         color='red')

plt.plot(dados2,
         color='green')

plt.title('Título do gráfico')
plt.ylabel('Valores')
plt.xlabel('Observações')
plt.legend(['dados', 'dados2'],
            loc='best')



#Exercíco
np.random.seed(1234)
dados_exercicio = np.random.randn(54)
media = np.mean(dados_exercicio)
meta = [media for k in range(0, len(dados_exercicio))]
legendas = ['Resultados', 'Meta']

"""
Exemplo 2
Personalizando as informações dos gráficos
"""
#Plotar dados da variável dados_exercício
plt.plot(dados_exercicio,
         color='orange')

#Plotar dados da variável meta
plt.plot(meta,
         color='blue',
         alpha=0.3)

#Manter a linha abaixo inalterada (ele serve para criar as legendas)
plt.legend(legendas,
           loc='best')

#Configurar os dados adicionais de título, rótulo dos eixos y e x
plt.title('Título do gráfico')
#Título
plt.ylabel('Resultados')
#Legenda do eixo Y
plt.xlabel('Semana')
#Legenda do eixo X
