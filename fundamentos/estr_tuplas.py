# -*- coding: utf-8 -*-
"""
Python DS - Tuplas (tuple)
@author: janio
"""

#Criação
tp = (1,3,5,7)

#Também pode ser criada assim
type(tp)

tp = 1,3,5,7
tp

#Acesso aos elementos - Igual a listas
print(tp)
tp[0]
tp[-1]
tp[0:2]


for item in tp:
    print(item)

ls = [1,2,3]
print(ls)    

ls[0] = 2
print(ls)

#Não é possível alterar um valor (tipo imutável) - Códigos abaixo geram erro
print(tp)
tp[0] = 9
#TypeError: 'tuple' object does not support item assignment

tp_vazia = ()

#Tupla com apenas um objeto
tp = ('Janio',)

tp.count('Janio')
tp.index('Janio')

tp = (1,3,5,7,7,1)
tp.index(5)
tp.count(7)

quadrado = []

for item in tp:
    print(item ** 2)
    quadrado.append(item ** 2)
    
quadrado


#Tuplas podem conter listas
tp_ls = (['Janio', 43, True], ['José', 72, True])

#Continuo sem poder alterar os items
tp_ls[0]
tp_ls[0][0]


tp_ls[0] = ['Tatiane', 38, False]
#TypeError: 'tuple' object does not support item assignment

#Mas posso alterar o conteúdo da lista que compoe a tupla
tp_ls[0][0] = 'Janio Lima'
tp_ls[0][1] = 45
print(tp_ls)

#Posso também inverter a lógica - Uma lista de tuplas
ls_tp = [('Janio', 43, True), ('José', 72, True)]
print(ls_tp)


#Neste caso não consigo alterar os elementos internos
ls_tp[0][0] = 'Joaquim'
#TypeError: 'tuple' object does not support item assignment

#Mas posso alterar os itens externos da lista
ls_tp[0] = ('Janio Lima', 45, True)
print(ls_tp)

#Também posso adicionar novas tuplas normalmente
ls_tp.append(('Tatiane', 38, False))
print(ls_tp)

dir(list)
dir(tuple)
