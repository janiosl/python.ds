# -*- coding: utf-8 -*-
"""
Python DS - Funções
@author: janio
"""
#========================================================
### PRIMEIRA PARTE ###
#========================================================

#Função vazia sem retorno
#========================================================
def funcao_vazia():
    #Variáveis locais
    a = 2
    b = 3
    print(f'{a} x {b} = {a*b}')


#Chamada da função
funcao_vazia()


#Função com parâmetros, sem retorno
#========================================================
def funcao(a,b):
    print(f'{a} x {b} = {a*b}')


#Chamadas da função
num1 = 2
num2 = 3
funcao(num1, num2)

funcao(3,7)

a = 5
b = 8
funcao(a,b)
funcao(b,a)


#Função com retorno
#========================================================
def multiplica(a,b):
    res = a*b
    return res


#Chamada da função
multiplica(3,7)

#Tratando retorno
resultado = multiplica(3,7)
print(resultado)

#Retorno de múltiplos valores e integração de funções
#========================================================
def novoSalario(salario, taxa):
    """
    Função realiza atualização do valor do salário
    Argumentos:
        salario (float): salário do empregado
        taxa (float): taxa decimal a ser usada na atualização
    Retorno:
        aumento (float): valor do aumento do salário
        novo (float): novo valor de salário        
    """
    aumento = multiplica(salario, taxa)
    novo = salario + aumento
    return aumento, novo

help(novoSalario)
novoSalario(29000, 0.085)

import numpy as np
np.sqrt(25)

help(np.sqrt)

import modulo
modulo.sum(2,2)
modulo.sqrt(16)

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
type(ajustes)


#Construir dicionário com retornos múltiplos
ajustes = dict(zip(['Aumento', 'Salário'], novoSalario(salario, taxa_ajuste)))
ajustes


#========================================================
### SEGUNDA PARTE ###
#========================================================

#Escopo de variável
#Variável apenas no escopo da função
def y_inexistente(x):
    y = x ** 2
    print(y)
    return y
    

x = 4
y_inexistente(x)
y_inexistente(10)

y = y_inexistente(10)

print(y)
#O print acima deve gerar o erro a seguir:
#NameError: name 'y' is not defined
#Variável criada apenas no escopo da função y_inexistente

#Solução:
#ATENÇÃO: Deve ser feito se realmente fizer sentido a variável fora da função
def y_existente(x):
    global y
    y = x ** 2
    print(y)


y_existente(7)
print(y)

del y
del x

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
#ATENÇÃO: Não recomendo "corrigir" este caso, pois não é um erro


#Documentação de ajuda - docstrings
#========================================================
#Função sem ajuda personalizada
def area_retangulo(b,h):
    #Função calcula área do retângulo
    return b*h


help(area_retangulo)

help(sum)
help(print)

#Função com ajuda personalizada
def area_retangulo(b,h):
    """
    Função calcula área do retângulo
    Parâmetros:
        b (int ou float): base do retângulo
        h (int ou float): altura do retângulo
    Retorno:
        A (int ou float): área do retângulo
    """
    return b*h


help(area_retangulo)


#========================================================
### TERCEIRA PARTE ###
#========================================================

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

#Programa principal (função integradora)
#======================================================================
#Funções analisa_folha() e novoSalario() usadas das seções anteriores

#Criando mais algumas funções
def analisa_empregado(nome, folha, analise):
    if folha[nome] > analise[0]:
        print('Seu salário está acima da média da equipe')
    elif folha[nome] < analise[0]:
        print('Seu salário está abaixo da média da equipe')
    else:
        print('Seu salário está na média da equipe')
    
    if folha[nome] == analise[-1]:
        print('Seu salário é o menor da equipe')
    else:
        print('Seu salário não é o menor da equipe')
   
   
def consulta(nome):
    """
    Implemente esta função para evitar a lógica de consulta
    de empregado embutida na função main()
    """
    pass
   
#Criando o programa principal
def main():
    """
    Programa principal: Integra as funcionalidades de análise
    de informações salariais
    """
    global folha_pagamento
    
    #Criação da folha de pagamentos
    folha_pagamento = {'João': 15000,
                       'Maria': 18000,
                       'Bruxa': 35000}
    
    #Análise da folha de pagamentos
    analise = analisa_folha(list(folha_pagamento.values()))
    
    #Consulta de empregado
    emp = input('Digite o nome de um empregado para análise: ')
    if emp in folha_pagamento.keys():
        analisa_empregado(emp, folha_pagamento, analise)
    else:
        print(f'{emp} não trabalha nesta empresa.')
        print('=' * 50)
    
    #Atualização da folha de pagamento
    print('Atualização da folha de pagamento:')
    print('-' * 50)
    
    for k,v in folha_pagamento.items():
        print(f'Empregado: {k} - Salário atual: R${v:.2f}')

        if v < analise[0]:
            t = 0.2
            _, ns = novoSalario(v, t)
            folha_pagamento[k] = ns
            print(f'Novo salário: R$ {ns:.2f}. Aumento de {t*100}%')
        else:
            print('Não houve aumento de salário.')


#Chamada do Programa Principal
main()
