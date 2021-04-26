print('Python DS - Lógica Condicional')
print('=' * 40)

nome = input('Digite o seu nome: ')
print(f'Olá {nome}!')

print('-' * 40)
primeiroNum = int(input('Digite um número inteiro: '))
segundoNum = int(input('Digite outro número interiro: '))

print('-' * 40)
print('Escolha a operação desejada:')

oper = int(input('1. Soma 2. Subtração'))
if oper == 1:
    resultado = primeiroNum + segundoNum
    tipo = 'soma'
else:
    tipo = 'subtração'
    resultado = primeiroNum - segundoNum
    
print(f'Resultado da operação {tipo}: {resultado}')
print('=' * 40)
