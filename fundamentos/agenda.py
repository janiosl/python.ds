# -*- coding: utf-8 -*-
"""
Python DS - Projeto de conclusão - Juntando as peças
@author: janio
"""

#Funções auxiliares da agenda
def cadastro(ag):
    """Função de cadastro de contatos"""
    print('-' * 60)
    while True:        
        print('Cadastro de novos registros')
        nome = input('Primeiro nome do contato: ')
        telefone = int(input('Telefone: '))
        ag[nome] = telefone
        print('-' * 60)
        continuar = input('Deseja adicionar outro registro? [S/N] ')
        if continuar[0].upper() == 'N':
            print('Módulo cadastro finalizado...')
            break
    print('-' * 60)


def exibe(ag):
    """Função exibe a agenda completa"""
    print('-' * 60)
    print('Consulta completa:')
    for chave, valor in ag.items():
        print('Nome:', chave, '- Telefone:', valor)
    print('-' * 60)


def consulta(ag):
    """Função consulta um contato pelo primeiro nome"""
    n = input('Digite o nome para consulta: ')
    print('-' * 60)
    if n in ag.keys():        
        print(f'Resultado da consulta:\nNome: {n} - Telefone: {ag[n]}')
    else:
        print('Contato não cadastrado')
    print('-' * 60)


def salvar(ag, saida='agenda.csv'):
    with open(saida, 'a') as arquivo:
        print('Nome,Telefone' , file=arquivo)
        for k,v in ag.items():
            print(k,v, sep=',', file=arquivo)
        print(f'Agenda salva no arquivo: {saida}')
        print('-' * 60)

        
#Programa principal
def main():
    global agenda
    agenda = dict()
    print('=' * 60)
    print('Agenda Telefônica 2024 - Python DS')
    print('=' * 60)
    
    while True:
        print('Selecione uma função:\n1 - Cadastro\n2 - Exibir agenda')
        print('3 - Consulta\n4 - Gravar em arquivo\n99 - SAIR')
        op = int(input('Opção: '))
        
        if op == 1:
            cadastro(agenda)
        elif op == 2:
            exibe(agenda)
        elif op == 3:
            consulta(agenda)
        elif op == 4:
            saida = input('Nome do arquivo (sem extensão): ')
            saida = saida+'.csv'
            salvar(agenda, saida)
        elif op == 99:
            break
        else:
            print('Opção inválida ou não implementada')
            print('-' * 60)
    
    print('=' * 60)
    print('Programa Agenda Finalizado...')
    print('=' * 60)


#Chamada do programa
if __name__ == "__main__":
    main()
