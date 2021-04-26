"""
Python DS - Sorteio de números aleatórios (SEM REPETIÇÃO)

#Resposta a comentário do canal do Youtube
sobre sortear números aleatórios sem repetição no
Python.

Duas opções de solução - Usando as funções sample e randint
da biblioteca random

Explicações adicionais na playlist a seguir:
https://www.youtube.com/playlist?list=PL0XxTDj23A1H-1NxZiOVKkMeCS44EIxih

Mais projetos e tutoriais em:
http://www.pythonds.com.br
Instagram: @python.ds
https://www.youtube.com/channel/UCdpQJDGrM3Xj58ZFF-2UNBA?view_as=subscriber
"""

#OPÇÃO 1 - Função sample
from random import sample

#Lista de opções do sorteio
options = list(range(1, 101))
print(f'Opções do sorteio:\n{options}')

#Sorteio de 3 números sem repetição
sorteados = sample(options, 3)
print(f'\nResultado do sorteio: {sorteados}')
print('=' * 60)


#OPÇÃO 2 - Função randint e sorteio passo a passo
from random import randint

#Lista vazia para registrar sorteados
sorteadosManual = []
j = 0

#Sorteio de 3 números
while j < 3:
    #Sorteio de 1 número entre 1 e 100
    x = randint(1, 100)

    #Validação do número e registro na lista de sorteados
    if x not in sorteadosManual:
        print(f'Número sorteado: {x}')
        sorteadosManual.append(x)
        print(f'Resultado parcial: {sorteadosManual}')
        j += 1
