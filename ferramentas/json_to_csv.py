# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 20:24:29 2021

@author: janio
"""

import os
#ALTERAR PARA O DIRETÓRIO DESEJADO
path = r'E:\Users\janio\Documents\Education\Mestrado e Doutorado\CEFET\2. Pesquisa\DAL_Events\Azure Harbinger\ms_an_detector'
os.chdir(path)

import pandas as pd


def json_to_csv(arquivo, output):
    """
    Função recebe um arquivo json e gera um arquivo csv com os mesmos dados.
    Adicionalmente, é gerado um data frame com estes dados para análise e
    conferência.

    Parameters
    ----------
    arquivo : str
        Nome do arquivo original em formato json.
    output : str
        Nome desejado para o arquivo de saída em formato csv.

    Returns
    -------
    csv_file : pandas data frame
        Variável data frame com os mesmos dados do arquivo csv.

    """
    sample = pd.read_json(arquivo,
                      orient='values')
    series = []
    for k in range(0, len(sample.series)):
        series.append(dict(sample.series[k]))

    csv_file = pd.DataFrame(series)
    
    csv_file.to_csv(output,
              index=False)

    return csv_file


arquivo = 'sample.json'
output = 'sample.csv'

arquivo = 'sample_hourly.json'
output = 'sample_hourly.csv'

sample = json_to_csv(arquivo, output)

from matplotlib import pyplot as plt
plt.plot(sample.value)
