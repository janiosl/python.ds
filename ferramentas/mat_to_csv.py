# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 11:01:18 2021

@author: janio
"""

import scipy.io as spio

#Carga do conjunto de dados originais
arquivo = r'E:\Users\janio\Documents\Education\Mestrado e Doutorado\CEFET\Disciplinas\4. Aprendizado de máquina\T2\code\data\ex7data1.mat'
colunas = ['X']


def mat_to_csv(arquivo, colunas):
    raw_mat = spio.loadmat(arquivo)
    
    conteudo = []
    
    for k in range(0, len(colunas)):
        conteudo.append(raw_mat[colunas[k]])
    
    return conteudo

X = mat_to_csv(arquivo, colunas)
X

raw_mat = spio.loadmat(arquivo)
