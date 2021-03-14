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


os.chdir(r'[Diretório desejado]')

#Dados do arquivo
os.getcwd()
arquivo = 'yahoo_stock_12-12-2020.csv'

#Carregar os dados
data = pd.read_csv(arquivo)

#Sumário estatístico dos dados
data.describe()

data.columns
data.values
data.Close.describe()

#Medidas estatística de um atributo
data['Close'].count() #Total de observações
data['Close'].mean() #Média
data['Close'].median() #Mediana
data['Close'].max() #Valor máximo
data['Close'].min() #Valor mínimo
data['Close'].sum() #Soma dos valores
data['Close'].cumsum() #Soma cumulativa
data['Close'].prod() #Produto da multiplicação de todos valores
data['Close'].var() #Variância
data['Close'].std() #Desvio padrão
data['Close'].pct_change() #Mudança percentual a cada observação

#Adicionar atributos
data['Tax_pct'] = 0.15
data.head()

#Atributos Calculados
data['Tax_value'] = data['Close'] * data['Tax_pct']
data.head()

#Gravar análise em novo arquivo
output = r'..\data\yahoo_stock_12-12-2020_analise.csv'
data.to_csv(output)

#Dados da aula passada
arquivo_online = 'https://raw.githubusercontent.com/janiosl/python.ds/master/data/yahoo_stock_12-12-2020.csv'
data_online = pd.read_csv(arquivo_online)

data_online['Double'] = data_online.Close * 2
data_online.to_excel('data_online.xlsx')
