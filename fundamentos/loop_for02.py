"""
Python DS - Loop for

#Exemplos de iteração com loop for evitar repetição de códigos com cálculos
ou outras instruções.

Explicações adicionais na playlist a seguir:
https://www.youtube.com/playlist?list=PL0XxTDj23A1H-1NxZiOVKkMeCS44EIxih

Mais projetos e tutoriais em:
http://www.pythonds.com.br
Instagram: @python.ds
https://www.youtube.com/channel/UCdpQJDGrM3Xj58ZFF-2UNBA?view_as=subscriber
"""

#Loop para realizar cálculos repetitivos sem repetir o código
numeros = [1, 2, 3, 4]

#Loop realiza os cálculos e exibe na tela
for k in range(0, len(numeros)):
    item = numeros[k] * 2
    print(item)


#Loop anterior adaptado para armazenar o resultado dos códigos em uma variável
dobro = []

#Loop realiza os cálculos e armazena em uma nova variável
for k in range(0, len(numeros)):
    item = numeros[k] * 2
    dobro.append(item)

print(dobro)
