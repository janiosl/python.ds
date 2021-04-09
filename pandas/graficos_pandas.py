# -*- coding: utf-8 -*-
"""
@author: Janio Lima
Canal Python DS:
https://www.youtube.com/channel/UCdpQJDGrM3Xj58ZFF-2UNBA?view_as=subscriber

Explicações adicionais na playlist a seguir:
https://www.youtube.com/playlist?list=PL0XxTDj23A1GSZuDOn5w3gunJKOhV267t
    
Referências:
MCKINNEY, Wes (2018). Python para análise de dados. Novatec.
GÉRON, Aurélien (2019). Mãos à Obra Aprendizado de Máquina com Scikit-Learn &
TensorFlow. AltaBooks. 
"""
import pandas as pd

#Dados da aula passada
arquivo = 'https://raw.githubusercontent.com/janiosl/python.ds/master/data/yahoo_stock_12-12-2020.csv'
data = pd.read_csv(arquivo)

##==============================================
##Criação de gráficos com métodos embarcados
##==============================================

#Gráfico de linha do preço de fechamento
data.Close.plot()

#Gráfico de linha do preço de fechamento
data.plot(y='Close')

#Histograma do preço de fechamento
data.Close.hist()

#Dispersão entre preço de fechamento e preço máximo
data.plot(kind='scatter', x='Close', y='High', #alpha=0.4,
             figsize=(8,4))


#Boxplot de todos os atributos contínuos
data.plot.box()

#Boxplot do preço de fechamento
data.Close.plot.box()

#Boxplot dos preços
data.loc[:,['Open', 'High', 'Low', 'Close']].plot(kind='box')

#Comparação do preço de fechamento e da máxima diária
data.loc[:, ['Close', 'High']].plot()

#Comparação do preço de fechamento e das máximas e mínimas diárias
#Para os primeiros dez dias do período analisado
data.loc[:10, ['Close', 'High', 'Low']].plot()

#Para os últimos 60 dias do período analisado
start = len(data.Close) - 60
data.loc[start:, ['Close', 'High', 'Low']].plot()
