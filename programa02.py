print('Python DS - Lógica Condicional')
print('=' * 40)

nome = input('Digite o seu nome: ')
print(f'Olá {nome}!')

print('-' * 40)
primeiroNum = int(input('Digite um número inteiro: '))
segundoNum = int(input('Digite outro número interiro: '))

print('-' * 40)
soma = primeiroNum + segundoNum

print(f'Resultado: {soma}')

if (soma % 2) == 0:
    print('O resultado é par')
else:
    print('O resultado é impar')

print('=' * 40)
