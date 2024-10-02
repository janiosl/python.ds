# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 21:10:19 2024

@author: janio
"""

#Criando conjunto a partir de uma lista
lista = [0, 2, 1, 33, 4, 5, 7, 0, 3, 33, 9, 2]
set(lista)
tuple(lista)


sem_duplicatas = set(lista)
sem_duplicatas

#Criando conjunto do zero
cj = {0,10,2,1}
cj

cj = {0,0,1,2,3,5,77,3,0,5,9}
cj

#Conjunto de letras não repetidas
set('abracadabra')

#Operações com conjuntos
cj.pop()
cj

cj.remove(77)
cj

#Outro exemplo a partir de uma lista
frutas = ['banana', 'uva', 'maça', 'banana', 'abacaxi']
frutas
set(frutas)

frutas = set(frutas)
frutas

vegetais = {'abacaxi', 'banana', 'maça', 'uva', 'alface', 'repolho', 'batata'}
vegetais


#Operações com conjuntos - Continuação
#Diferença de conjuntos
vegetais - frutas
frutas - vegetais
 
#Itens no primeiro conjunto ou no segundo
vegetais | frutas

#Item nos dois conjuntos
vegetais & frutas

#Itens em vegetais ou frutas, mas não nos dois
vegetais ^ frutas
#{'alface', 'batata', 'repolho'}

frutas.add('kwi')
frutas.add('Acerola')

vegetais ^ frutas
#{'Acerola', 'alface', 'batata', 'kwi', 'repolho'}
