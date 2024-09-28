# -*- coding: utf-8 -*-
"""
Classe cria um tipo de dado personalizado para ser usado
na construção de matrizes.

@author: janio
"""

class Matriz:
    def __init__(self, n=1,m=1, matriz=[]):
        self.n = n
        self.m = m
        self.matriz = matriz
        
    def set_matriz(self):
        self.matriz = []
        for i in range(self.n):
            linha = []
            for j in range(self.m):
                list.append(linha,0)
            self.matriz = self.matriz + [linha]
        return self.matriz

    def get_matriz(self):
        return self.matriz

    def get_dim(self):
        return self.n, self.m

    def fill_matriz(self, valores):
        if len(valores) != self.n * self.m:
            return 'Quantidade de valores inválidos'
        if len(self.get_matriz()) == 0:
            self.set_matriz()
        v = 0
        for i in range(self.n):
            for j in range(self.m):
                self.matriz[i][j] = valores[v]
                v += 1
        return self.matriz
    
    def __repr__(self):
        return f'Matriz {self.n} linhas x {self.m} colunas\n{self.matriz}'
    
    def mult_diag(self, k):
        if self.n != self.m:
            return 'Operação inválida para matrizes não quadradas'
        for i in range(len(self.matriz)):
            self.matriz[i][i] *= k
        return self.matriz
    
    def __add__(self, M2):
        if self != M2:
            return 'Impossível calcular: Dimensões diferentes'
        M3 = []
        for i in range(len(self.matriz)):
            linha = []
            for j in range(len(self.matriz[0])):
                list.append(linha, self.matriz[i][j] + M2.matriz[i][j])
            list.append(M3, linha)
        linha = []
        return M3
    
    def __mul__(self, M2):
        #Em construção-Código ainda não implementa a multiplicação de matrizes
        #Número de colunas de A deve ser igual ao número de linhas de B
        #Matriz resultante é números de linhas da matriz A e colunas de B
        #Linhas --> M2.n, Colunas --> self.m
        #Há um bug para alguns casos - Verificando
        if not self.m == M2.n:
            return 'Impossível calcular: Dimensões incompatíveis'
        
        l = self.n
        c = M2.m
        M3 = Matriz(l,c)
        M3.set_matriz()
        
        Ma = list(self.matriz)
        Mb = list(M2.matriz)
        
        for l in range(len(M3.matriz)):
            print('Linha', l)
            for c in range(len(M3.matriz[0])):
                print('    Coluna', c)
                for k in range(len(M3.matriz)):
                    print('      Item k', k)
                    print(Ma[l][k])
                    #pass
                    M3.matriz[l][c] += Ma[l][k] * Mb[k][c]
            print('*' * 40)
        
        return M3
    
    def __eq__(self, M2):
        if self.n == M2.n and self.m == M2.m:
            return True
        return False
