# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 20:35:12 2024

@author: janio
"""
from matriz import *

#Criação da matriz A vazia
A = Matriz(3,2)
A
A.get_dim()
A.get_matriz()
#Preenchimento da matriz de zeros
A.set_matriz()
#Preenchimento de valores na matriz anteriormente preechida com zeros
A.fill_matriz([1,2,3,4,5,6])
A.get_matriz()
print(A)

#Criação da matriz B
B = Matriz()
B.get_matriz()
len(B.get_matriz())
#Preenchimento direto da matriz
B.fill_matriz([1])
print(B)

#Criação da matriz C
C = Matriz(3,2)
C.fill_matriz([6,5,4,3,2,1])
C.get_dim()
C.get_matriz()
print(C)


#Preenchimento de matriz com valores na criação
T = Matriz(2,3,[[1,2,3],[3,2,1]])
T

T.set_matriz()

#Operações entre matrizes
#Comparação de dimensões de matrizes
A == C
A == B
C == B


#Multiplicação diagonal por escalar
A.get_matriz()
len(A.get_matriz())
A.mult_diag(2)
D = Matriz(4,4)
D.fill_matriz(list(range(16)))
print(D)
D.mult_diag(2)

'''
Resultado
[0, 1, 2, 3],
[4, 10, 6, 7],
[8, 9, 20, 11],
[12, 13, 14, 30]

Original
[0, 1, 2, 3],
[4, 5, 6, 7],
[8, 9, 10, 11],
[12, 13, 14, 15]
'''

#Adição de matrizes
A.get_matriz()
B.get_matriz()
A + B
#'Impossível calcular: Dimensões diferentes'

C.get_matriz()
A.__add__(C)

A + C

N = A + C
N
#[[7, 7], [7, 7], [7, 7]]


#Multiplicação de matrizes
A * C
#'Impossível calcular: Dimensões incompatíveis'
A * B
#'Impossível calcular: Dimensões incompatíveis'

Z = Matriz(2,3)
Z
Z.fill_matriz([3,3,3,3,3,3])
A.get_matriz()
A * Z
### BUG - CORRIGIR ###
#Matriz 3 linhas x 3 colunas
#[[0, 0, 0], [0, 0, 0], [0, 0, 0]]

newA = Matriz(3,2)
newA.set_matriz()
newB = Matriz(2,5)
newB.set_matriz()
AB = newA * newB
AB
### BUG - CORRIGIR ###
#Matriz 3 linhas x 5 colunas
#[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]


A = Matriz(2,2)
A.fill_matriz([3,2,5,-1])
A

B = Matriz(2,3)
B.fill_matriz([6,4,-2,0,7,1])
B

A * B
