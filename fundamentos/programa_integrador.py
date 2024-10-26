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


#Seção do Programa Principal
#================================================================
def principal():
    #Criação da folha de pagamento
    #-----------------------------------
    
    #Resumo estatístico da folha
    #-----------------------------------
    
    #Consulta de empregados
    #-----------------------------------
    
    #Atualização dos salários
    #-----------------------------------
    pass


#Chamada do Programa principal
#================================================================
principal()
