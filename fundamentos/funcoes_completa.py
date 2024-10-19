# -*- coding: utf-8 -*-
"""
Python DS - Funções
@author: janio
"""
#Função vazia sem retorno
#========================================================
def funcao_vazi():
    #Variáveis locais
    a = 2
    b = 3
    print(f'{a} x {b} = {a*b}')


#Chamada da função
funcao_vazi()

#Função com parâmetros, sem retorno
#========================================================
def funcao(a,b):
    print(f'{a} x {b} = {a*b}')


#Chamadas da função
num1 = 2
num2 = 3
funcao(num1, num2)

funcao(3,7)

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
#ATENÇÃO: Deve ser feito se realmente fizer sentido a variável fora da função
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

#Documentação de ajuda - docstrings
#========================================================
#Função sem ajuda personalizada
def area_retangulo(b,h):
    return b*h


help(area_retangulo)

#Função com ajuda personalizada
def area_retangulo(b,h):
    """
    Função calcula área do retângulo
    Parâmetros:
        b (int ou float): base 
        h (int ou float): altura 
    Retorno:
        A (int ou float): área do retângulo
    """
    return b*h


help(area_retangulo)

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
   
    
#Criando o programa principal
def main():
    """
    Programa principal: Integra as funcionalidades de análise
    de informações salariais
    """
    global folha_pagamento
    
    folha_pagamento = {'João': 15000,
                       'Maria': 18000,
                       'Bruxa': 35000}
    
    analise = analisa_folha(list(folha_pagamento.values()))
    
    emp = input('Digite o nome de um empregado para análise: ')
    if emp in folha_pagamento.keys():
        analisa_empregado(emp, folha_pagamento, analise)
    else:
        print(f'{emp} não trabalha nesta empresa.')
        print('=' * 50)
    
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

    
main()