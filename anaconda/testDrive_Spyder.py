# -*- coding: utf-8 -*-
"""
Este é um código simples para exemplificar o uso
do Python através do Spyder. Seu objetivo é compor 
material complementar aos estudos da plataforma de 
Ciência de Dados Anaconda através do Canal Python DS.
Para assistir aos tutoriais em vídeo acesse:
https://www.youtube.com/playlist?list=PL0XxTDj23A1Ftg-rb_pIaFE3pPROwWtbw


"""

print('Olá Python DS')

a = 2
b = 3

soma = a + b

print(soma)


import numpy as np
numeros = np.random.randn(1000)

from matplotlib import pyplot as plt
plt.hist(numeros)

plt.plot(numeros)


np.mean(numeros)

import os
os.getcwd()

caminho = r'D:\Python'
os.chdir(caminho)

