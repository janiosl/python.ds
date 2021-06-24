"""
#Consulta web com Python
#Python DS
"""

#Bibliotecas usadas
from time import sleep
from pyautogui import click, doubleClick, moveTo
from pyautogui import typewrite, press

##===============================
#Preparação do ambiente
#Coordenadas da aplicação
##===============================
icone_navegador = (247, 1062)
campo_busca = (717, 502)
botao_buscar = (878, 572)
resultado = (306, 564)
termoBusca = 'Python DS'


##===============================
#RPA
##===============================
#Passo 1: Abrir navegador
moveTo(icone_navegador, duration=1)
sleep(1)
click()

#Passo 2: Realizar busca
moveTo(campo_busca, duration=1)
sleep(0.5)
typewrite(termoBusca)
sleep(1)
press('enter')

#Passo 3: Acessar resultado
sleep(2)
moveTo(resultado)
sleep(0.5)
click()


#Passo 4 (PRINCIPAL): INSCRIÇÃO NO CANAL Python DS
