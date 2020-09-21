"""
Programa cria uma função para realizar
a soma de valores informados nos argumentos,
em seguida usa a função para somar variáveis

Canal Python DS
Aula de Fundamentos de Python
Criação de função com argumentos e retorno
do valor para reaproveitamento no código
"""

def soma(numero01, numero02):
    """
    Função soma - realiza a soma de dois valores
    Parâmetros:
    numero01: primeiro valor a ser somado
    numero02: segundo valor a ser somado

    Retorno: resultado da soma
    """
    total = numero01 + numero02

    return total


a = 2
b = 3

resultado = soma(a, b)

print(f'A soma dos números {a} e {b} é igual a {resultado}')
