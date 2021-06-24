"""
#Programa simples para abrir e fechar um aplicativo
#Python DS
"""

#Bibliotecas usadas
import pyautogui as pyag
from time import sleep
from pyautogui import click, doubleClick, moveTo

#Usar código abaixo no prompt para capturar as posições
#pyag.position()

#Gravar posições capturadas nas variáveis abaixo
foto_python = (353, 452)
botao_fechar = (1891, 3)

#Abrir aplicativo
moveTo(foto_python, duration=1)
sleep(0.5)
doubleClick()

#Pausar para visualização do arquivo
sleep(2)

#Fechar aplicativo
moveTo(botao_fechar, duration=0.5)
sleep(0.5)
click()

