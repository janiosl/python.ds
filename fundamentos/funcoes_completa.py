# -*- coding: utf-8 -*-
"""
Python DS - Funções
@author: janio
"""

#Função vazia sem retorno
def funcao_vazi():
    #Variáveis locais
    a = 2
    b = 3
    print(f'{a} x {b} = {a*b}')


#Chamada da função
funcao_vazi()

#Função com parâmetros, sem retorno
def funcao(a,b):
    print(f'{a} x {b} = {a*b}')


#Chamadas da função
num1 = 2
num2 = 3
funcao(num1, num2)

funcao(3,7)

#Função com retorno
def multiplica(a,b):
    res = a*b
    return res


#Chamada da função
multiplica(3,7)

#Tratando retorno
resultado = multiplica(3,7)
print(resultado)

#Retorno de múltiplos valores e integração de funções
def novoSalario(salario, taxa):
    aumento = multiplica(salario, taxa_ajuste)
    novo = salario + aumento
    return aumento, novo

#Chamada da função
salario = 29000
taxa_ajuste = 0.085

novoSalario(salario, taxa_ajuste)

#Diferentes formas de tratamento do retorno múltiplo
#Cada item retornado em uma variável
aumento, ns = novoSalario(salario, taxa_ajuste)
print(f'Aumento: R$ {aumento:.2f}')
print(f'Salário atualizado: R$ {ns:.2f}')

#Usar apenas um item
_, ns = novoSalario(salario, taxa_ajuste)
print(f'Salário atualizado: R$ {ns:.2f}')

aumento, _ = novoSalario(salario, taxa_ajuste)
print(f'Aumento: R$ {aumento:.2f}')
print(f'Salário atualizado: R$ {ns:.2f}')

#Acesso exclusivo a um dos itens do retorno múltiplo
novoSalario(salario, taxa_ajuste)[0]
novoSalario(salario, taxa_ajuste)[1]

#Armazenar retorno em uma tupla
ajustes = novoSalario(salario, taxa_ajuste)
ajustes

#Construir dicionário com retornos múltiplos
ajustes = dict(zip(['Aumento', 'Salário'], novoSalario(salario, taxa_ajuste)))
ajustes

#Uso de bibliotecas
#Declara fora (preferencialmente no topo do arquivo .py)
import numpy as np

def analisa_folha(salarios):
    media = np.mean(salarios)
    desvio = np.std(salarios)
    maior = max(salarios)
    menor = min(salarios)
    
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

analisa_folha(list(folha_pagamento.values()))

#Escopo de variável
#Variável apenas no escopo da função
def y_inexistente(x):
    y = x ** 2
    print(y)
    

x = 4
y_inexistente(x)
print(y)
#O print acima deve gerar o erro a seguir:
#NameError: name 'y' is not defined
#Variável criada apenas no escopo da função y_inexistente

#Solução:
#ATENÇÃO: só deve ser feito se realmente fizer sentido a variável fora da função
def y_existente(x):
    global y
    y = x ** 2
    print(y)

y_existente(7)
print(y)


#Variável fora do escopo da função
def x_inexistente(a):
    y = x ** 2
    print(y)
    return y

#Apaga o x da memória da seção atual antes de testar
x_inexistente(4)
#A chamada função acima deve gerar o erro a seguir:
#  Cell In[63], line 2 in x_inexistente
#    y = x ** 2
#NameError: name 'x' is not defined

#Solução:
#ATENÇÃO: Não recomendo "corrigir" este caso, pois é necessariamente um erro
