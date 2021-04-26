"""
Python DS - Loop for

#Exemplos de iteração com loop for para iteração com apoio da função
range, iterações diretamente em itens de listas, etc. e impressão do
conteúdo recuperado na tela.

OBSERVAÇÃO: Os comandos de impressão podem ser substituíods pelas instruções
que se deseja repetir no caso real em que a lógica for usada

Explicações adicionais na playlist a seguir:
https://www.youtube.com/playlist?list=PL0XxTDj23A1H-1NxZiOVKkMeCS44EIxih

Mais projetos e tutoriais em:
http://www.pythonds.com.br
Instagram: @python.ds
https://www.youtube.com/channel/UCdpQJDGrM3Xj58ZFF-2UNBA?view_as=subscriber
"""

#Loop simples para exibição de um range de 5 itens (0 a 4)
for k in range(5):
    print(5)


#Loop para iteração de itens de uma lista
lista = ['Python', 'Java', 'JS', 'C', 'Visual Basic', 'Fortran']

#Loop simples usando uma variável de controle para recuperar os itens diretamente
print('=' * 60)
for item in lista:
    print(item)


#Loop usando um variável de controle numérica (inteiro) para recuperar itens
print('=' * 60)
for k in range(0, len(lista)):
    print(lista[k])


#Loop para iteração de letras de uma string
print('=' * 60)
palavra = 'Python'

for letra in palavra:
    print(letra)
