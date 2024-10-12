"""
Disciplina: Programação de Computadores (PPPRO-CEFET/RJ)
Funções dos exercícios da disciplina
Aluno: Janio de Souza Lima
"""

#Definição de funções

#Funções da aula 01 - Slides 21 a 23
#====================================================
#Questão 1 - Área do retângulo
def area_ret(l1,l2):
    """
    Função calcula a área de um retangulo
    dados os lados (l1, l2)
    """
    return l1*l2


#Questão 2 - Coroa
def potencia(x,y=2):
    """
    Função calcula a potência dada a base (x) e expoente (y)
    Caso o valor de y não seja declarado na chamada será usado
    o valor padrão de expoente = 2.
    """
    return x**y

    
def areac(r):
    """
    Função calcula a área de um círuclo dado o valor do raio (r).
    """
    PI = 3.14
    return PI*potencia(r)


def coroa(r1,r2):
    """
    Função calcula a coroa circular de dois circulos
    dados os valores dos raios (r1, r2).
    """
    return areac(r1) - areac(r2)


#Questão 3 - Resultado e resto da divisão de inteiros
def div_rest(int1, int2):
    """
    Função calcula a divisão inteira e o resto da divisão de dois
    números inteiros (int1, int2)
    int -> tuple.
    """
    return int1//int2, int1%int2


#Questão 4 - Ordenana função segundo grau
def ord_seg_grau(a, b, c, absc):
    #f(x) = ax² +bx + c
    #return a*(x**2) + b*x + c
    return 0


#Questão 5 - Gorjeta 10%
def gorjeta(conta):
    """
    Função calcula a gorjeta de 10% dado o valor total de uma conta.
    """
    return conta * 0.10


#Questão 6 - Média de dois números
def media(x,y):
    """
    Função calcula a média de dois números (x,y).
    """
    return (x+y)/2

#Questão 7 - Média ponderada de dois números
def media_pond(x, px, y, py):
    """
    Função calcula a média ponderada de dois números (x,y),
    dados pesos (px, py).
    """    
    return (sum([x*px, y*py])) / (sum([px,py]))


#Questão 8 - Distância barco na correnteza


#Questão 9 - Saldo final - Juros simples
def saldo_final(saldo_inicial, meses, taxa):
    """
    Função calcula o saldo final de uma conta, dado um saldo inicial,
    taxa de juros e tempo em meses, usando juros simples.
    """    
    return saldo_inicial * (1 + taxa * meses)


#Questão 10 - Erro soma PG infinita e n primeiros termos
def erro_soma_pg():
    return 0


#Questão 11 - Tempo total prova corredor
def tempo_total(hi, mi, si, hf, mf, sf):
    return 0


#Questão 12 - Gorjeta e divisão da conta
def gorjeta_div(conta, pessoas):
    """
    Função calcula uma gorjeta de 10% e a divisão da conta entre as 
    pessoas de uma mesa, dado o valor da conta e quantidade de pessoas.
    """        
    return gorjeta(conta), (conta + gorjeta(conta))/pessoas


#Questão 13 - Área do cubo com aresta c
def area_cubo(c):
    """
    Função calcula a área da superfície de um cubo de aresta = c.
    """        
    return 6*c**2


#Funções da aula 01 - Slides 39 a 41
#====================================================

#Questão 1a - Calcular média de quatro números (usar função média de 2 números)
def media_quatro(a,b,c,d):
    return media(media(a,b), media(c,d))


#Questão 1b - Maior números de bombons e troco
#SOLUÇÃO 1 - Criar uma função do zero
def bombons(dinheiro, preco):
    return dinheiro // preco, dinheiro % preco

#SOLUÇÃO 2 - Criar uma função copiando a anterior que realiza o mesmo calculo
fun_bb = div_rest


#Questão 2a - Calcular hipotenusa dados os catetos
def hipotenusa(c1, c2):
    from math import pow, sqrt
    return sqrt(pow(c1, 2) + pow(c2, 2))


#Questão 2b - Distância no plano carteseano
def distancia_plano(xa, ya, xb, yb):
    from math import pow, sqrt
    return sqrt(pow(xb-xa, 2)+pow(yb-ya,2))


#Questão 2c - Perímetro de triângulo reto dados os catetos
def perimetro_tri(c1, c2):
    return c1 + c2 + hipotenusa(c1, c2)


#Questão 3 - Comprimento do círculo
def comprimento_circ(r):
    PI = 3.14
    return 2*PI*r


def voltas(r,dist):
    return dist / comprimento_circ(r)


#Funções da aula 02
#====================================================
