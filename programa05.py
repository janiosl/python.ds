print('Python DS - Lógica Condicional')
print('=' * 40)

nome = input('Digite o seu nome: ')
cidade = input('Digite a cidade onde nasceu: ')

print(f'Olá {nome}!')

if nome[0] == cidade[0]:
    print('As iniciais de seu nome e sua cidade natal são iguais')
else:
    print('As iniciais de seu nome e sua cidade natal são diferentes')

print('=' * 40)
