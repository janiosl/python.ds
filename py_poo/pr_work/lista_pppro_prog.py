# -*- coding: utf-8 -*-
"""
Disciplina: Programação de Computadores (PPPRO-CEFET/RJ)
Lista de exercícios da disciplina
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


#Aplicação
print(area_ret(5,7))
print(area_ret(15,2))
print(area_ret(500,700))
print(area_ret(5,0))

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


#Aplicação
print(coroa(2,1))
print(coroa(15,5))
print(coroa(100,0))

#Questão 3 - Resultado e resto da divisão de inteiros
def div_rest(int1, int2):
    """
    Função calcula a divisão inteira e o resto da divisão de dois
    números inteiros (int1, int2)
    int -> tuple.
    """
    return int1//int2, int1%int2


div_rest(5,2)

teste = div_rest(5,2)
teste

div, rest = div_rest(5,2)
div
rest


#Questão 4 - Ordenana função segundo grau
def ord_seg_grau(a, b, c, absc):
    #Em desenvolvimento
    #f(x) = ax² +bx + c
    #return a*(x**2) + b*x + c
    return 0


#Questão 5 - Gorjeta 10%
def gorjeta(conta):
    """
    Função calcula a gorjeta de 10% dado o valor total de uma conta.
    """
    return conta * 0.10


#Aplicação
gorjeta(1000)
gorjeta(175)
gorjeta(225.70)

#Questão 6 - Média de dois números
def media(x,y):
    """
    Função calcula a média de dois números (x,y).
    """
    return (x+y)/2


#Aplicação
media(-5,7)
media(2, -2)
media(5,5)
media(3,4)
media(3.0, 4.0)

#Questão 7 - Média ponderada de dois números
def media_pond(x, px, y, py):
    """
    Função calcula a média ponderada de dois números (x,y),
    dados pesos (px, py).
    """    
    return (sum([x*px, y*py])) / (sum([px,py]))


#Aplicação
media_pond(10, 1, 9, 2)
media_pond(9, 1, 10, 2)

#Questão 8 - Distância barco na correnteza


#Questão 9 - Saldo final - Juros simples
def saldo_final(saldo_inicial, meses, taxa):
    """
    Função calcula o saldo final de uma conta, dado um saldo inicial,
    taxa de juros e tempo em meses, usando juros simples.
    """    
    return saldo_inicial * (1 + taxa * meses)


#Aplicação
inicial = 100
taxa = 0.1
meses = 3

saldo_final(inicial, taxa, meses)
saldo_final(5000, 0.05, 12)

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


#Aplicação
gorjeta_div(100, 2)
gorjeta_div(520, 3)

#Questão 13 - Área do cubo com aresta c
def area_cubo(c):
    """
    Função calcula a área da superfície de um cubo de aresta = c.
    """        
    return 6*c**2


#Aplicação
area_cubo(3)
area_cubo(9)


#Funções da aula 01 - Slides 39 a 41
#====================================================

#Questão 1a - Calcular média de quatro números (usar função média de 2 números)
def media_quatro(a,b,c,d):
    return media(media(a,b), media(c,d))


#Aplicação
media_quatro(4,4,2,4)
media_quatro(2,4,2,4)
media_quatro(2,2,2,2)

#Questão 1b - Maior números de bombons e troco
#SOLUÇÃO 1 - Criar uma função do zero
def bombons(dinheiro, preco):
    return dinheiro // preco, dinheiro % preco


#Aplicação
#Resposta com Solução 1
bombons(7, 0.75)
bombons(25, 2)

#SOLUÇÃO 2 - Criar uma função copiando a anterior que realiza o mesmo calculo
fun_bb = div_rest
#Resposta com Solução 2
fun_bb(7, 0.75)
fun_bb(25, 2)

#Resposta com Solução 3
div_rest(7, 0.75)
div_rest(25, 2)

#Questão 2a - Calcular hipotenusa dados os catetos
def hipotenusa(c1, c2):
    from math import pow, sqrt
    return sqrt(pow(c1, 2) + pow(c2, 2))


#Aplicação
hipotenusa(4,3)
hipotenusa(6,8)
hipotenusa(9,12)

#Questão 2b - Distância no plano carteseano
def distancia_plano(xa, ya, xb, yb):
    from math import pow, sqrt
    return sqrt(pow(xb-xa, 2)+pow(yb-ya,2))


#Aplicação
distancia_plano(3,5,6,1)
distancia_plano(-3,2, 3,-2)
distancia_plano(-2,13,6,7)

#Questão 2c - Perímetro de triângulo reto dados os catetos
def perimetro_tri(c1, c2):
    return c1 + c2 + hipotenusa(c1, c2)

#Aplicação
perimetro_tri(4,3)
perimetro_tri(6,8)
perimetro_tri(9,12)

#Questão 3 - Comprimento do círculo
def comprimento_circ(r):
    PI = 3.14
    return 2*PI*r


#Aplicação
comprimento_circ(4)
comprimento_circ(5)
comprimento_circ(15)

#Questão 4 - Voltas em pista circular
def voltas(r,dist):
    return dist / comprimento_circ(r)


#Aplicação
voltas(4,50)
voltas(4,60)
voltas(15,300)

#Funções da aula 02 - Slides 17 a 19
#====================================================
#Questão 1
def absoluto(num):
    if num < 0:
        return num * -1
    return num


#Aplicação
absoluto(5)
absoluto(-3)
absoluto(0)
absoluto(3)

#Questão 2
def raizes_sg(a,b,c):
    raizes = []
    #Equaçao do segundo grau: ax**2 + bx + c'
    if a == 0:
        print('Coeficiente a=0. Não há raízes')
        q = 0
    else:
        d = b*b - (4*a*c)
        
        if d < 0:
            print('Delta menor que 0. Raízes imaginárias')
            q = 0
        elif d == 0:
            raiz = -b / (2*a)
            print('Delta=0 , raiz = ',raiz)
            raizes.append(raiz)
            q = 1
        else:
            raiz1 = (-b + d**(1/2)) / (2*a)
            raizes.append(raiz1)
            raiz2 = (-b - d**(1/2)) / (2*a)
            raizes.append(raiz2)
            print('Raizes: ',raiz1,' e ',raiz2)
            
            q = 2
    return q, raizes


#Aplicação
raizes_sg(0,2,3)
raizes_sg(1,2,3)
raizes_sg(10,13,2)
raizes_sg(1,3,2)

#Questão 3
def rep_palavra(p):
    return 3*p


#Aplicação
rep_palavra('janio')
rep_palavra('casa')
rep_palavra('águia')

#Questão 4
#Questão 5
def min_max(n1,n2):    
    print(f'Mínimo: {min(n1,n2)}')
    print(f'Máximo: {max(n1,n2)}')
    return min(n1,n2), max(n1,n2)


#Aplicação
min_max(2,5)
min_max(33,2)
min_max(7,33)

#Questão 6
def meia(idade, rg=True, estudante=False):
    direito = False
    if rg == True:
        if idade < 21 or idade >= 65:
            direito = True            
        elif estudante == True:
            direito = True
    
    return direito


#Aplicação
meia(18)
meia(65)
meia(66)
meia(66, rg=False)
meia(50)
meia(50, estudante=True)
meia(43, estudante=True)


#Funções da aula 02 - Slides 40 a 43
#====================================================
## Parte 01 ----------------
#Questão 1
def analise_nome(nome):
    print(f'{nome} tem {len(nome)} letras e começa com {nome[0]}')
    return len(nome), nome[0]


#Aplicação
analise_nome('Janio de Souza Lima')
analise_nome('Cecilia')

#Questão 2
def inverte(p):
    return p[::-1]


#Aplicação
inverte('casa')
inverte('caneca')
inverte('tv')

#Questão 3
def letras_impares(palavra):
    return palavra[::2]


#Aplicação
letras_impares('Jano')
letras_impares('sapato')
letras_impares('Python')

#Questão 4
def concatena_si(a,b):
    return a[1:] + b[1:]


#Aplicação
a = 'Jano'
b = 'Minerva'
concatena_si(a,b)
concatena_si('Ada', 'Atena')
concatena_si('Oca', 'Madeira')

#Questão 5
def multi_final(s):
    return s[-2:] * 3


#Aplicação
multi_final('vaca')
multi_final('abcd')

#Questão 6
def concatena_ord(a, b):
    c = [a,b]
    c.sort()
    return c[0]+' '+c[1]


def concatena_ord2(a, b):
    if a[0] < b[0]:
        return a + ' ' + b
    else:
        return b + ' ' + a
    

#Aplicação
a = 'Janio'
b = 'Cecilia'
concatena_ord(a,b)
concatena_ord('xbcd', 'efghi')


concatena_ord2(a,b)
concatena_ord2('xbcd', 'efghi')
concatena_ord2('Zebra', 'Teste')


## Parte 02 ----------------
#Questão 1
def concatena_abba(a,b):
    return a+b+b+a


#Aplicação
concatena_abba('a', 'b')
concatena_abba('ca','sa')
concatena_abba('fa', 'to')

#Questão 2
def sorte(nome, idade):
    x = 0
    x = idade * 4
    x += 8
    x *= 60
    x /= 240
    x += 22
    x  -= idade
    return f'Parabéns {nome}, seu número da sorte é {x}'


#Aplicação
sorte('Janio', 43)
sorte('Igor', 40)

#Questão 3
def concatena_fatias(a,b):
    if len(a) < 15:
        return 'Inválido: Número de letras de a < 15'
    elif len(b) < 15:
        return 'Inválido: Número de letras de b < 15'

    return a[:5]+b[-10:]
        

#Aplicação
a = ''
b = 'O rato roeu a roupa do rei de Roma'
concatena_fatias(a, b)

a = 'O rato roeu a roupa do rei de Roma'
b = 'O rato roeu'
concatena_fatias(a, b)

a = 'O rato roeu a roupa do rei de Roma'
b = 'O doce perguntou para o doce qual o doce mais doce'
concatena_fatias(a, b)

#Questão 4
def muda_palavra(s,x,i):
    if i < 0 or i > len(s):
        return 'Posição inválida'
    ns = s.replace(s[i], x)
    return ns


#Aplicação
muda_palavra('Janeo', 'i', 3)
s = 'Vaxco'
i = s.index('x')
muda_palavra(s, 's', i)

#Questão 5
def meio(s):
    m = int(len(s)/2)
    ns = s[:m] + s + s[m:]
    return ns


#Aplicação
meio('teste')
meio('abcd')
meio('abcde')

#Questão 6
def hashtag(s):
    m = int(len(s)/2)
    ns = '#'+s[:m] + '#' + s[m:] + '#'
    return ns

#Aplicação
hashtag('Vasco')
hashtag('abcd')
hashtag('abcde')


#Funções da aula 03 - Slide 14
#====================================================
#Questão 1
def intercala(tp1, tp2):
    ls = []
    for i in range(len(tp1)):
        ls.append(tp1[i])
        ls.append(tp2[i])
        
    tp3 = tuple(ls)
    return tp3


#Aplicação
a = (1,2,3)
b = ('a','b','c')
intercala(a,b)

#Questão 2
def opera(tp):
    if tp[0] == 'SOMA':
        res = tp[1]+tp[2]
    elif tp[0] == 'MULT':
        res = tp[1]*tp[2]
    elif tp[0] == 'DIV':
        res = tp[1]/tp[2]
    elif tp[0] == 'SUB':
        res = tp[1]-tp[2]
    else:
        return None
    return res


#Aplicação
op = ('SOMA', 2, 3)
opera(op)
opera(('TESTE', 2, 3))
opera(('MULT', 2, 3))
opera(('DIV', 2, 3))
opera(('SUB', 2, 3))


#Funções da aula 03 - Slide 26 a 27
#====================================================
#Questão 1
def conta_palavras(frase):
    l = frase.split()
    return len(l)


#Aplicação
s = 'O rato roeu a roupa do rei de Roma'
conta_palavras(s)
s = ' O rato roeu a roupa do rei de Roma'
conta_palavras(s)
conta_palavras('Programação em Python')

#Questão 2
def muda_frase(frase, palavra, p1, p2):
    pass
    
    
#Aplicação

#Questão 3
def sub_branco(frase):
    ls = frase.split()
    texto = '#'.join([p for p in ls])
    return texto


#Aplicação
s = ' O rato roeu a roupa do rei de Roma'
sub_branco(s)

#Questão 4
def frase_fatia(s, c):
    idx = s.index(c)
    return s[idx:]


#Aplicação
frase_fatia('Janio','i')
frase_fatia('Quem mexeu no meu queijo', 'n')

#Questão 5
def elementos(tp):
    pass


#Aplicação

#Questão 6
def intercala_ls(ls1, ls2):
    ls3 = []
    for i in range(len(ls1)):
        ls3.append(ls1[i])
        ls3.append(ls2[i])
        
    return ls3


#Aplicação
a = (1,2,3)
b = ('a','b','c')
intercala_ls(a,b)
intercala_ls([1,3,5], [2,4,6])


#Funções da aula 03 - Slide 58 a 60
#====================================================
#Questão 1
def inverte_frase(frase):
    nf = frase.split()
    nf.reverse()
    nf = ' '.join(p for p in nf)
    return nf


#Aplicação
f = 'eu gosto de chocolate'
inverte_frase(f)

#Questão 2
def ordena_frase(frase):
    nf = frase.split()
    nf.sort()
    nf = ' '.join(p for p in nf)
    return nf


#Aplicação
f = 'eu gosto de chocolate'
ordena_frase(f)

f = 'eu gosto de doce'
ordena_frase(f)

#Questão 3
def frase_i(frase):
    nf = frase
    for v in 'aeou':
        nf = nf.replace(v, 'i')
    return nf

    
#Aplicação
f = 'Leveu meu cachorro para passear'
frase_i(f)

#Questão 4
def palavra_frase(frase, palavra, pos):
    frase = frase.split()
    if palavra in frase:
        pos = frase.index(palavra)
        frase[pos] = palavra.upper()
    else:
        frase.insert(pos, palavra)
    
    frase = ' '.join(p for p in frase)
    return frase


#Aplicação
f = 'Meu nome é ana'
p = 'ana'
palavra_frase(f, p, 0)

p = 'primeiro'
palavra_frase(f, p, 1)

#Questão 5
def faltas(jogos):
    f = []
    for jogo in jogos:
        f.append(sum(jogo[2]))
    return sum(f)


#Aplicação
js = [['Brasil','Itália', [10,9]],['Brasil','Espanha', [5,7]]]
faltas(js)

#Funções da aula 04 - Slides 24 a 25
#====================================================
#Questão 1
def prime_div(num):
    div = 2
    while (num%div != 0):
        div += 1
    return div


#Aplicação
prime_div(4)
prime_div(5)
prime_div(8)
prime_div(9)
prime_div(7)

#Questão 2
def soma_n_imp(n):
    soma = 0
    for i in range(1,n+1,2):        
        soma += i
        print(i, soma)
    return soma
    

#Aplicação
soma_n_imp(7)
soma_n_imp(3)
soma_n_imp(13)

#Questão 3
def fatorial(num):
    fatorial = 1
    for i in range(num,0,-1):
        fatorial *= i
    return fatorial


def soma_fatorial():
    soma_fat = 0
    for i in range(1,11):
        print(i, '->', fatorial(i))
        soma_fat += fatorial(i)
    return soma_fat


#Aplicação
soma_fatorial()

#Questão 4
#Questão 5

#Questão 6
def cont_div(num):
    cont = 0
    for i in range(num,0,-1):        
        if (num % i == 0):
            cont += 1    
    return cont


#Aplicação
cont_div(10)
cont_div(7)
cont_div(8)
cont_div(5)
cont_div(1)

#Questão 7
def cont_letra(frase, letra):
    cont = 0
    for l in frase:
        if l == letra:
            cont += 1
    return cont


#Aplicação
cont_letra('casa', 'a')
cont_letra('janio', 'o')
cont_letra('a casa de janio', 'a')
cont_letra('a casa de janio', 'j')
