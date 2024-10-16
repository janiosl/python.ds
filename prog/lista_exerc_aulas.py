"""
Disciplina: Programação de Computadores (PPPRO-CEFET/RJ)
Exercícios Aula 1 - Lista de Exercícios
Aluno: Janio de Souza Lima
"""

from pppro_func import *

#Funções da aula 01 - Slides 21 a 23
#====================================================
#Testes das funções criadas

#Questão 1 - Área do retângulo
print(area_ret(5,7))
print(area_ret(15,2))
print(area_ret(500,700))
print(area_ret(5,0))


#Questão 2 - Coroa
print(coroa(2,1))
print(coroa(15,5))
print(coroa(100,0))


#Questão 3 - Resultado e resto da divisão de inteiros
div_rest(5,2)

teste = div_rest(5,2)
teste

div, rest = div_rest(5,2)
div
rest


#Questão 4 - Ordenana função segundo grau


#Questão 5 - Gorjeta 10%
gorjeta(1000)
gorjeta(175)
gorjeta(225.70)


#Questão 6 - Média de dois números
media(-5,7)
media(2, -2)
media(5,5)
media(3,4)
media(3.0, 4.0)


#Questão 7 - Média ponderada de dois números
media_pond(10, 1, 9, 2)
media_pond(9, 1, 10, 2)

#Questão 8 - Distância barco na correnteza


#Questão 9 - Saldo final - Juros simples
inicial = 100
taxa = 0.1
meses = 3

saldo_final(inicial, taxa, meses)
saldo_final(5000, 0.05, 12)


#Questão 10 - Erro soma PG infinita e n primeiros termos

#Questão 11 - Tempo total prova corredor

#Questão 12 - Gorjeta e divisão da conta
gorjeta_div(100, 2)
gorjeta_div(520, 3)


#Questão 13 - Área do cubo com aresta c
area_cubo(3)
area_cubo(9)

#Funções da aula 01 - Slides 39 a 41
#====================================================

#Questão 1a - Calcular média de quatro números (usar função média de 2 números)
media_quatro(4,4,2,4)
media_quatro(2,4,2,4)
media_quatro(2,2,2,2)


#Questão 1b - Maior números de bombons e troco
#Resposta com Solução 1
bombons(7, 0.75)
bombons(25, 2)

#Resposta com Solução 2
fun_bb(7, 0.75)
fun_bb(25, 2)

#Resposta com Solução 3
div_rest(7, 0.75)
div_rest(25, 2)


#Questão 2a - Calcular hipotenusa dados os catetos
hipotenusa(4,3)
hipotenusa(6,8)
hipotenusa(9,12)


#Questão 2b - Distância no plano carteseano
distancia_plano(3,5,6,1)
distancia_plano(-3,2, 3,-2)
distancia_plano(-2,13,6,7)


#Questão 2c - Perímetro de triângulo reto dados os catetos
perimetro_tri(4,3)
perimetro_tri(6,8)
perimetro_tri(9,12)


#Questão 2d
#Questão 2e


#Questão 3 - Comprimento do círculo
comprimento_circ(4)
comprimento_circ(5)
comprimento_circ(15)


#Questão 4 - Voltas em pista circular
voltas(4,50)
voltas(4,60)
voltas(15,300)


#Funções da aula 04 - Slides 24 a 25
#====================================================
#Questão 1
prime_div(4)
prime_div(5)
prime_div(8)
prime_div(9)
prime_div(7)


#Questão 2
soma_n_imp(7)
soma_n_imp(3)
soma_n_imp(13)


#Questão 3
soma_fatorial()

#Questão 4
#Questão 5

#Questão 6
cont_div(10)
cont_div(7)
cont_div(8)
cont_div(5)
cont_div(1)


#Questão 7
cont_letra('casa', 'a')
cont_letra('janio', 'o')
cont_letra('a casa de janio', 'a')
cont_letra('a casa de janio', 'j')