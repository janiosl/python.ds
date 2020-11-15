import numpy as np

dados = [10, 20, 25, 33, 25, 77]
pesos = [1, 2, 3, 4, 5, 6]
print(dados)
print(pesos)

#Média simples
media = np.mean(dados)
print(f'Média simples dos dados: {media:.1f}')

#Média ponderada
dividendo = 0
for k in range(0, len(dados)):
    produto = 0
    produto = dados[k] * pesos[k]
    print(f'Número: {dados[k]} x Peso: {pesos[k]}')
    dividendo += produto
    print(f'Dividendo: {dividendo}')
    

divisor = sum(pesos)

media_pond = dividendo / divisor

print(f'Dividendo = {dividendo}')
print(f'Divisor = {divisor}')
print(f'Média Ponderada = {media_pond:.1f}')


#Média geométrica
produto = dados[0] * dados[1] * dados[2] * dados[3] * dados[4] * dados[5]
media_geo = produto ** (1 / len(dados))
print(f'Média Geométrica = {media_geo:.1f}')

#Teste 2
produto = 0
k = len(dados) - 1
while k >= 0:
    print(k)
    parcial = dados[k] * dados[k - 1]
    produto += parcial
    print(produto)
    k -= 1
