# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 20:24:29 2021

@author: janio
"""

import os
import json
import pandas as pd

#ALTERAR PARA O DIRETÓRIO DESEJADO
path = r'E:\Users\janio\Documents\Education\Mestrado e Doutorado\CEFET\2. Pesquisa\DAL_Events\Azure Harbinger\ms_an_detector'
os.chdir(path)


def csv_to_json(arquivo, output, atributos, granularidade='daily'):
    """
    Função recebe um arquivo csv e gera um arquivo json com os mesmos dados.
    O formato do json gerado é compatível com a API da ferramenta Microsoft
    Anomaly Detector para realização de experimentos de detecção de eventos

    Parameters
    ----------
    arquivo : str
        String com nome do arquivo original em formato csv.
    output : str
        String com nome do arquivo de saída em formato json.
    atributos : list
        Lista com nome de duas variáveis. Tempo e série para análise
    granularidade : str
        Granularidade dos dados da série temporal
        Padrão: daily

    Returns
    -------
    json_file : pandas data frame
        Variável data frame com os mesmos dados do arquivo json.

    """
    #Carga do arquivo e seleção de variáveis
    sample = pd.read_csv(arquivo)
    sample = sample.loc[:,[atributos[0], atributos[1]]]
    
    
    #Criação da estrutura básica do json no padrão desejado
    json_file = {"granularity": granularidade,
                 "series": []
                 }
        
    #Adição das observações do csv no campo series do json
    for k in range(0, len(sample['pH'])):
        json_file['series'].append(
            {"timestamp": sample[atributos[0]][k],
             "value": sample[atributos[1]][k]})
    
    #Exportação dos dados para arquivo json
    with open(output, 'w') as file:
        json.dump(json_file, file)
    
    return json_file


#Preencher apenas o nome do arquivo original, sem extensão
nome_sem_extensao = 'water'

#Gerar nomes dos arquivos de entrada e saída
arquivo = nome_sem_extensao+'.csv'
output = nome_sem_extensao+'.json'

#Definição de parâmetros dos dados
atributos = ['Time', 'pH']
granularidade = 'minutely'

#sample = csv_to_json(arquivo, output, atributos)
sample = csv_to_json(arquivo, output, atributos, granularidade)

#Teste/Conferência
teste = pd.read_json(output,
                     orient='values')

