# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 08:49:52 2021

@author: janio
"""

import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

import os

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

os.chdir(r'D:\Python\estatística')

arquivo = 'loan.csv'
#Conjunto de dados original disponível no Kaggle
emprestimos = pd.read_csv('loan.csv', low_memory=False)

#Análise do conteúdo do arquivo
emprestimos.columns
emprestimos.head(5)


#Pré-Processamento dos dados
emprestimos['loan_amnt'] = emprestimos['loan_amnt'].fillna(0)
emprestimos['annual_inc'] = emprestimos['annual_inc'].fillna(0)


y = np.array(emprestimos['annual_inc'])
x = np.array(emprestimos['loan_amnt'])
print(y,
      x)


#Visualização dos dados
fig, (ax1, ax2) = plt.subplots(1, 2)

ax1.hist(x, density=True)
ax2.scatter(x, y)
sns.despine()


#Criação do modelo
lm_model = LinearRegression(normalize=True)
lm_model.fit(x.reshape(-1, 1), y)


#Recuperação do parâmetros
a = lm_model.intercept_ #Interseção do eixto y
b = lm_model.coef_ #Inclinação em relação ao eixo x


plt.scatter(x, y)
plt.plot(x, (x * b + a), 'r')

emprestimos['annual_inc'].corr(emprestimos['loan_amnt'])


r2 = lm_model.score(x.reshape(-1, 1), y)
print(f'R² do modelo: {r2:.3f}')

