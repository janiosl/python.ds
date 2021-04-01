import numpy as np
import matplotlib.pyplot as plt
import os
from parte5.minimizar_funcao import minimizar_funcao
from custo_reglin_regularizada import custo_reglin_regularizada

def learningCurve(theta, X, y, X_val, y_val, _lambda):
    m = len(X)
    erros_treino = np.zeros(m)
    erros_val = np.zeros(m)
    qtds_exemplos = []
    
    for i in range(1,m+1):
        X_train = X[:i,:]
        y_train = y[:i]
        qtds_exemplos.append(len(X_train))
        
        result = minimizar_funcao(theta, X_train, y_train, _lambda)
        theta = result[0]
        
        J_train = custo_reglin_regularizada(theta, X_train, y_train, _lambda=0)
        J_val = custo_reglin_regularizada(theta, X_val, y_val, _lambda)
        
        erros_treino[i-1] = J_train
        erros_val[i-1] = J_val
    
    return qtds_exemplos, erros_treino, erros_val
