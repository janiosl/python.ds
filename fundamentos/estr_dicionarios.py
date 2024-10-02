# -*- coding: utf-8 -*-
"""
Python DS - Dicionários (dict)
@author: janio
"""

#Notação chave - valor
telefones = {'Janio': 99991234, 'João': 99990011}
print(telefones)

#Visualizar as chaves
telefones.keys()

#Visualizar os valores
telefones.values()

telefones['Janio']
telefones['João'] = 99880011

print(telefones)

for chave, valor in telefones.items():
    print('Chave:', chave, ', Valor:', valor)
    

for chave, valor in telefones.items():
    print('Nome:', chave, '- Telefone:', valor)
        

telefones['Olivia'] = 34351221
print(telefones)

del telefones['João']
print(telefones)

#Verificar existência de chaves em um dicionário
'João' in telefones
'Janio' in telefones

#Outra notação para criar dicionários
senhas = dict(usr1='segredo', usr2='senhaDificil', usr3='@PyDS_is_the_best')
senhas
senhas['usr1']
senhas['usr3']

for usr, senha in senhas.items():
    print(f'Usuário: {usr} - Senha: {senha}')


#Dicionários com dictcomp
numeros = [1,3,5,7,9]
dobro = {n: n * 2 for n in numeros}
dobro


#Dicionário a partir de listas ou tuplas usando zip
nome = ('João', 'Maria', 'Bruxa')
papel = ['Protagonista', 'Protagonista', 'Antagonista']

joao_e_maria = dict(zip(nome, papel))
joao_e_maria

caracteristica = [['Protagonista',9], ['Protagonista',10], ['Antagonista', 71]]
joao_e_maria = dict(zip(nome, caracteristica))
joao_e_maria['João']

joao_e_maria['João'][0] #Papel
joao_e_maria['João'][1] #Idade

joao_e_maria['João'].append('Coragem')
joao_e_maria['Maria'].append('Inteligência')
joao_e_maria['Bruxa'].append('Maldade')

print(joao_e_maria)

for k,v in joao_e_maria.items():
    print(f'Personagem: {k}.\nCaracterísticas:\n    Papel: {v[0]}, Idade: {v[1]}, Poder: {v[2]}')

#Remover último item
joao_e_maria.popitem()
print(joao_e_maria)

#Remover item pela chave
joao_e_maria.pop('João')
print(joao_e_maria)
