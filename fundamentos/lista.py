#Criação de lista
lista = [1,3,5,7]
print(lista)
lista


#Listas de diferentes tipos de dados
ls = [1,3,'janio', 3.5, True, False]
ls

ls = ['Janio', 43, 'João', 27, 'Maria', 30]
ls


for i in range(1, len(ls), 2):
    print(ls[i])

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
#[0, 1, 3, 5, 7, 9]

lista.insert(1,2) #Adiciona na posição 1 o valor 2
#[0, 2, 1, 3, 5, 7, 9]

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
frutas.insert(1, 'mamão')
print(frutas)


#Remover um item específico da lista pela localização
#Descobrir a localização de um item na lista
frutas.index('alface')
frutas[5]
frutas[-2]

frutas.index('mamão')
frutas[1]

#Alface não é fruta
frutas[-2]
del frutas[-2]
print(frutas)

#Não gosto de mamão
frutas[1]
del frutas[1]

print(frutas)

for fruta in frutas:
    if fruta == 'mamão':
        print(f'A fruta {fruta} é igual a mamão')
        idx = frutas.index(fruta)
        del frutas[idx]
        print('Fruta removida da cesta')
    else:
        print(f'A fruta {fruta} é diferente de mamão')
        print('Fruta mantida na cesta')


#Remover último item da lista
#Repolho não é fruta
frutas.pop()
print(frutas)


#Desorganizando um pouco a lista anterior
lista
lista.append(0)
lista.append(3)
lista.append(33)
lista[2] = 5
lista[1] = 4
print(lista)


#Ordenando listas
lista.sort()
print(lista)

frutas.sort()
print(frutas)

#Contando itens em uma lista
frutas.count('banana')
frutas.append('banana')
lista.count(1)
lista.count(0)
lista.count(9)

#Outra forma de criar lista a partir de lista
#Listcomp
triplo = [x * 3 for x in lista]

print(triplo)
print(lista)

#Removendo um item pelo seu conteúdo - Apenas primeiro item encontrado
lista.remove(3)
lista.remove(0)
print(lista)

#Invertendo a ordem em uma lista
lista.reverse()
print(lista)

frutas.reverse()
print(frutas)
