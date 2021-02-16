# -*- coding: utf-8 -*-
"""
Erros e Tratamento de Exceções no Python

Desenvolvimento por Janio Lima

Vídeo com aula sobre tratamento de exceções:
    https://www.youtube.com/playlist?list=PL0XxTDj23A1H-1NxZiOVKkMeCS44EIxih
"""


"""
No exemplo abaixo não é apresentado nenhuma exceção
no Python, mas note que a lógica está errada.
Este tipo de erro é uma armadilha comum e o tratamento
precisa ser feita com a conferência dos resultados,
seja em uma análise mais simples e manual ou com
ajuda de ferramentas de debug.
"""
#Erro de lógica
numero1 = 5
numero2 = 3

if numero1 > numero2:
    print('O primeiro número é menor que o segundo')


"""
Nos exemplos trabalhos com erros que geram mensagens
de exeção no Python, seja por sintaxe inválida,
nomes de variáveis ou funções digitadas erradamente,
variáveis inexistentes, etc.

Para este tipo de situação é possível a análise interativa
e correção do erro, ou o tratamento da exceção
usando a estrutura try - except
"""
#Erro sem tratamento
print(a)


#Erro com tratamento de exceção básico
try:
    print(a)
except:
    print('Ocorreu uma falha. Acione o suporte técnico')



#Erro com tratamento de exceção intermediário
try:
    print('Iniciando o programa...')
    print(a)
    print('Programa Concluído com sucesso')
except Exception as erro:
    print('Ocorre um erro')
    print(f'Detalhe do erro: {erro}')



#Erro com tratamento de exceção e geração de log
try:
    print('Iniciando o programa...')
    print(a)
    print('Programa Concluído com sucesso')
    
except Exception as err:
    print('Ocorre um erro. Acione o suporte técnico')
    with open('log.txt', 'w') as log:
        print(f'Detalhe do erro: {err}', file=log)


