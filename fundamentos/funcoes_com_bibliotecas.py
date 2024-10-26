# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 13:31:58 2024

@author: janio
"""

#Uso de bibliotecas
#========================================================
#Declara fora (preferencialmente no topo do arquivo .py)
import numpy as np


def analisa_folha(salarios):
    """
    Função calcula um resumo estatístico dos salários. Exibe o resultado
    na tela e retorna os valores calculados
    Parâmetros:
        salarios (list): Lista de valores (float) de salários 
    Retorno:
        media (float): Média salarial
        desvio (float): Desvio padrão dos salários
        maior (float): Maior salário
        menor (float): Menor salário
        
    """
    media = float(np.mean(salarios))
    desvio = float(np.std(salarios))
    maior = float(max(salarios))
    menor = float(min(salarios))
    
    print('Resumo estatístico de salários:')
    print('-' * 50)
    print(f'Média salarial: {media:.2f}\nDesvio padrão: {desvio:.2f}')
    print(f'Maior salário: {maior:.2f}\nMenor salário: {menor:.2f}')
    print('=' * 50)
    
    return media, desvio, maior, menor


#Aplicação
folha_pagamento = {'João': 15000,
                   'Maria': 18000,
                   'Bruxa': 35000}

folha_pagamento.values()
list(folha_pagamento.values())

analisa_folha(list(folha_pagamento.values()))
analise = analisa_folha(list(folha_pagamento.values()))
analise

dic_analise = dict(zip(['media', 'desvio', 'maior', 'menor'], analise))
dic_analise
