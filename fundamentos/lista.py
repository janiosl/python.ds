#Criação de lista
lista = [1,3,5,7]
print(lista)

#Acessar um item da lista por sua posição
lista[0] #Primeiro item da lista
lista[-1] #Último item da lista
lista[0:3] #Itens de 0 a 3, exclusive. Itens 0, 1 e 2.


#Exibe itens da lista
print('Itens da lista')
for item in lista:
    print(item)

#Calcula o dobro de cada item da lista
print('Itens da lista')
for item in lista:
    print(item * 2)

    

#Operações com valores da lista
lista[0] = 0 #Altera o valor do item 0 da lista
lista[0] += 1

#Adiciona um item ao final da lista
lista.append(9)

#Adiciona um item em um índice específico da lista
lista.insert(0, 0) #Adiciona na posição 0 o valor 0
lista.insert(1,2) #Adiciona na posição 1 o valor 2

#Criação de uma lista a partir de outra
dobro = []

for num in lista:
    dobro.append(num * 2)

print(lista)
print(dobro)

#Lista com qualquer tipo de valor
frutas = ['banana', 'maça', 'uva']
print(frutas)

frutas.append('abacaxi')
frutas.append('alface')
frutas.append('repolho')
frutas.insert(1, 'mamaão')

print(frutas)

#Remover um item específico da lista
#Alface não é fruta
frutas[-2]
del frutas[-2]
print(frutas)

#Não gosto de mamão
del frutas[1]
print(frutas)

#Remover último item da lista
#Repolho não é fruta
frutas.pop()
print(frutas)

#Descobrir a localização de um item na lista
frutas.index('banana')
frutas[0]
frutas.index('uva')
frutas[2]

