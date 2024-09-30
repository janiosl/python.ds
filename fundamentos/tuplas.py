# -*- coding: utf-8 -*-
"""
@author: janio
"""

#Criação
tp = (1,3,5,7)
#Também pode ser criada assim
tp = 1,3,5,7


#Acesso aos elementos - Igual a listas
print(tp)
tp[0]
tp[-1]


for item in tp:
    print(item)
    

#Não é possível alterar um valor (tipo imutável) - Códigos abaixo geram erro
tp[0] = 1
#TypeError: 'tuple' object does not support item assignment

tp_vazia = ()

#Tupla com apenas um objeto
tp = ('Janio',)

tp.count('Janio')
tp.index('Janio')

tp = (1,3,5,7)
tp.index(5)

for item in tp:
    print(item ** 2)
    

#Tuplas podem conter listas
tp_ls = (['Janio', 43, True], ['José', 72, True])

#Continuo sem poder alterar os items
tp_ls[0]
tp_ls[0] = ['Tatiane', 38, False]
#TypeError: 'tuple' object does not support item assignment

#Mas posso alterar o conteúdo da lista que compoe a tupla
tp_ls[0][0] = 'Janio Lima'
tp_ls[0][1] = 45
print(tp_ls)

#Posso também inverter a lógica - Uma lista de tuplas
ls_tp = [('Janio', 43, True), ('José', 72, True)]

#Neste caso não consigo alterar os elementos internos
ls_tp[0][0] = 'Joaquim'
#TypeError: 'tuple' object does not support item assignment

#Mas posso alterar os itens externos da lista
ls_tp[0] = ('Janio Lima', 45, True)
print(ls_tp)

#Também posso adicionar novas tuplas normalmente
ls_tp.append(('Tatiane', 38, False))
print(ls_tp)
