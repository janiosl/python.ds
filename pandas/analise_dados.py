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


#os.chdir(r'D:\git\python.ds\data')

#Dados do arquivo
os.getcwd()
arquivo = r'..\data\yahoo_stock_12-12-2020.csv'

#Carregar os dados
data = pd.read_csv(arquivo)

#Sumário estatístico dos dados
data.describe()

data.columns
data.Close.describe()

#Medidas estatística de um atributo
data['Close'].mean()
data['Close'].max()
data['Close'].sum()

#Adicionar atributos
data['Tax_pct'] = 0.15
data.head()

#Atributos Calculados
data['Tax_value'] = data['Close'] * data['Tax_pct']
data.head()

#Gravar análise em novo arquivo
output = r'..\data\yahoo_stock_12-12-2020_analise.csv'
data.to_csv(output)


