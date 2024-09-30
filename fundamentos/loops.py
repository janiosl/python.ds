salarios = [1600, 9500, 29000]

print('Loop for')
for s in salarios:
    print(f'Salário atual: {s}')
    print(f'Novo salário: {s * 1.08}')
    print('-' * 30)


print('=' * 50)


contador = 0
print('Loop while')
while contador < len(salarios):
    print(f'Salário atual: {salarios[contador]}')
    print(f'Novo salário: {salarios[contador] * 1.08}')
    print('-' * 30)
    contador += 1
