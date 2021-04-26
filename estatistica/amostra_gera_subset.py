# -*- coding: utf-8 -*-
"""
##=============================================================
##AMOSTRAS COM PANDAS E RANDOM
##=============================================================

Script para criação de subsets e gravação em arquivo csv

Created on Mon Apr 26 09:04:49 2021

@author: janio
"""
import os
import pandas as pd
from random import sample, seed


##=============================================================
##CARGA DOS DADOS ORIGINAIS
##=============================================================
#Configuração do diretório de trabalho e do arquivo original
#Substituir pelos dados de sua aplicação
os.chdir(r'D:\Python\estatística')
arquivo = 'loan.csv'

#Conjunto de dados original disponível no Kaggle
dados = pd.read_csv(arquivo, low_memory=False)


##=============================================================
##GERAÇÃO E ARMAZENAMENTO DO SUBSET
##=============================================================
#Semente para garantir a reprodutibilidade da amostra
seed(31)

#Índices do dataset
options = list(range(0, len(dados)))

#Definição do tamanho da amostra
percent_amostra = 0.1 #Percentual
tam_amostra = int((len(dados)) * percent_amostra) #Quantidade

#Índices da amostra
sampleIdx = sample(options, tam_amostra)

#Geração da amostra e armazenamento como csv
subset = dados.iloc[sampleIdx]
output = 'sub_set.csv'
subset.to_csv(output, index=False)
