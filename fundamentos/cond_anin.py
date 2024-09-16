a = 7
b = 5

if a == b:
    print('a igual a b')
    soma = a + b
    print('a + b =', soma)
else:
    print('a é diferente de b')
    if a > b:
        diferenca = a - b
        print('a - b =', diferenca)
    elif a < b:
        produto = a * b
        print('a x b =', produto)
    else:
        print('Nenhuma das alternativas')
    
