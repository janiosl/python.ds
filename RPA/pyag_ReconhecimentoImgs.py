"""
#Mapear Tela por Reconhecimento de imagem
#Python DS
Tutorial para uso do código: https://youtu.be/JafE-mSCiWA
"""

#Bibliotecas usadas
from time import sleep
import pyautogui
from pyautogui import click, moveTo, typewrite

##===============================
#Preparação do ambiente
#Coordenadas da aplicação
##===============================
videoDesejado = (253, 670)

#Nome do arquivo com a imagem a ser reconhecida
botao_curtir = 'like.PNG'
termo = 'INSCREVA-SE NO CANAL Python DS'


##===============================
#RPA
##===============================
#Passo 1: Acessar vídeo
moveTo(videoDesejado, duration=1)
sleep(0.5) #Aguardar meio segundo
click()

#Passo 2: Reconhecer imagem
sleep(2) #Aguardar a próxima página carregar

#Função realiza reconhecimento da imagem desejada
curtir = pyautogui.locateCenterOnScreen(botao_curtir)


#Passo 3: Acessar resultado
sleep(1)
#Move para o centro da imagem reconhecida
moveTo(curtir)
sleep(0.5)
click()

#Passo 4 (PRINCIPAL): INSCRIÇÃO NO CANAL Python DS
moveTo(246, 107)
click()
sleep(0.5)
typewrite(termo)
