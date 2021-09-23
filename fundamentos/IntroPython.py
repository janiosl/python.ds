nome = 'Janio'
ano_nascimento = 1981
tem_filhos = True

idade = 2021 - ano_nascimento

print('Relatório:')
print('Nome:', nome)
print('Idade:', idade, 'anos')

if tem_filhos == True:
  print('Tem filhos')
else:
  print('Não tem filhos')

print('Tipos das variáveis')
print(type(nome), type(ano_nascimento), type(tem_filhos))


print()

salario = 5000
print('Saláro:', salario)


ajustePercentual = 10.5
aumento = (salario * ajustePercentual)/100
salario = salario + aumento

print('Ajuste:', ajustePercentual,'%', 'R$', aumento)
print('Novo salário: R$', salario)
