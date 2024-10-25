# -*- coding: utf-8 -*-
"""
Programa com Função Integradora
@author: janio
"""
import numpy as np


#Criação das funções dos módulo do programa principal
#======================================================================
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
        

def consulta(emp, folha, analise):
    if emp in folha.keys():
        analisa_empregado(emp, folha, analise)
    else:
        print(f'{emp} não trabalha nesta empresa.')
        print('=' * 50)
    

#Programa principal (função integradora)
#======================================================================
def main():
    """
    Programa principal: Integra as funcionalidades de análise
    de informações salariais
    """    
    #Criação da folha de pagamentos
    #------------------------------
    global folha_pagamento
    folha_pagamento = {'João': 15000,
                       'Maria': 18000,
                       'Bruxa': 35000}
    
    #Análise da folha de pagamentos
    #------------------------------
    analise = analisa_folha(list(folha_pagamento.values()))
    
    #Consulta de empregado
    #------------------------------
    emp = input('Digite o nome de um empregado para análise: ')    
    consulta(emp, folha_pagamento, analise)
        
    #Atualização da folha de pagamento
    #------------------------------
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
#======================================================================
main()
