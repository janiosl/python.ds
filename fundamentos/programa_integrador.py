# -*- coding: utf-8 -*-
"""
Python DS - Programa com Função Integradora

@author: janio
"""
#Seção de importação de bibliotecas
#================================================================
import numpy as np


#Seção de criação das funções (organização modular do programa)
#================================================================
def multiplica(a,b):
    res = a*b
    return res


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


def consulta(nome, folha, analise):
    if nome in folha.keys():
        print(f'{nome} é empregado desta empresa')
        analisa_empregado(nome, folha, analise)
    else:
        print(f'{nome} não é empregado desta empresa')


#Seção do Programa Principal
#================================================================
def principal():
    #Criação da folha de pagamento
    #-----------------------------------
    global folha_pagamento
    folha_pagamento = {'João': 15000,
                       'Maria': 18000,
                       'Bruxa': 30000}
    print('Folha de pagamento criada com sucesso')
    print('-' * 50)
    
    #Resumo estatístico da folha
    #-----------------------------------
    analise = analisa_folha(list(folha_pagamento.values()))
    
    #Consulta de empregados
    #-----------------------------------
    print('Consultando empregado')
    nome = input('Digite o nome do empregado a ser consultado: ')
    consulta(nome, folha_pagamento, analise)
    print('-' * 50)
    
    #Atualização dos salários
    #-----------------------------------
    print('Atualizando folha de pagamento')
    t = 0.2
    for k,v in folha_pagamento.items():
        print(k,v)
        if v < analise[0]:
            _, ns = novoSalario(v, t)
            folha_pagamento[k] = ns
    
    print('Folha de Pagamento atualizada')
    print('Novos salários')
    print(folha_pagamento)
    print('Programa Encerrado')
    print('-' * 50)


#Chamada do Programa principal
#================================================================
principal()
