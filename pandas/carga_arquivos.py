# -*- coding: utf-8 -*-
"""
@author: Janio Lima
Canal Python DS:
https://www.youtube.com/channel/UCdpQJDGrM3Xj58ZFF-2UNBA?view_as=subscriber

Explicações adicionais na playlist a seguir:
https://www.youtube.com/playlist?list=PL0XxTDj23A1GSZuDOn5w3gunJKOhV267t
    
Referências:
MCKINNEY, Wes. Python para análise de dados. São Paulo: Novatec, 2018.
"""

#Bibliotecas
import pandas as pd
import os

#Dados do arquivo
os.chdir(r'D:\git\python.ds\data')
arquivo = 'yahoo_stock_12-12-2020.csv'

#Carregar os dados
data = pd.read_csv(arquivo)

#Analisar caracterísitcas dos dados
data.describe()
data.columns

#Analisar um atributo específico
data['Close'].describe()

#Consultar primeiras e últimas ocorrências
data.head()
data.tail()

#Consultar linhas específicas
data.loc[0]
data.iloc[0]
data.iloc[1000:]
data.iloc[:100]

#Amostragem a partir dos dados
from random import sample
samp = sample(list(data.index), 10)
test = data.iloc[samp]
#Outra opção de amostra
#samp2 = sample(list(range(0,2666)), 10)

#Consultar atribustos específicos (filtrar colunas)
price = data.Close
price = data['Date', 'Close'] #ERRADO
price = data.loc[:, ['Date', 'Close']] #CORRETO

#Outras opções de carga de dados
#Carregar os dados a partir de um URL
arquivo_online = 'https://raw.githubusercontent.com/janiosl/python.ds/master/data/yahoo_stock_12-12-2020.csv'
data_online = pd.read_csv(arquivo_online)

#Carregar dados a partir de planilha
data_xls = pd.read_excel(r'..\data\yahoo_stock_12-12-2020.xlsx')
