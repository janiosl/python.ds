print('Python DS - Lógica Condicional e Loop')
print('Calculadora')
print('=' * 40)

while True:
    print('-' * 40)
    primeiroNum = int(input('Digite um número inteiro: '))
    segundoNum = int(input('Digite outro número interiro: '))

    print('-' * 40)
    print('Operações:')
    oper = int(input('1. Soma 2. Subtração 3. Multiplicação 4. Divisão 99. Encerrar calculadora\nEscolha a operação desejada: '))

    #Lógica de aplicação das operações
    if oper == 1:
        resultado = primeiroNum + segundoNum
        tipo = 'soma'
    elif oper == 2:
        tipo = 'subtração'
        resultado = primeiroNum - segundoNum
    elif oper == 3:
        tipo = 'multiplicação'
        resultado = primeiroNum * segundoNum
    elif oper == 4:
        tipo = 'divisão'
        resultado = primeiroNum / segundoNum
    elif oper == 99:
        break
    else:
        tipo = None
        print('Você digitou uma opção inválida')

    #Exibição do resultado, se  este não for nulo
    if tipo != None:
        print(f'Resultado da operação {tipo}: {resultado}')

    print('=' * 40)
