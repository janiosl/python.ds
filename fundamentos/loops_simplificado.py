salarios = [1600, 9500, 29000]

novos_salarios_for = []
for s in salarios:
    novos_salarios_for.append(s * 1.08)


contador = 0
novos_salarios_while = []
while contador < len(salarios):
    novos_salarios_while.append(salarios[contador] * 1.08)
    contador += 1

    
print('Atualização de salários concluída')
