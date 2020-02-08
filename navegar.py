"""
* Programa navega em opções em uma página web,
mas poderia ser adaptado para uma aplicação.
* Após chegar em um formulário digita um termo
para busca e pressiona a tecla enter.
* Em seguida acessa o primeiro resultado da busca
e copia a primeira palavra do título.
* O resultado da cópia é gravado em uma variável e
exibido na tela
"""
import os, pyautogui
from time import sleep
from pyperclip import paste

#Posições
home = (1135, 426)
link_documentos = (1373, 578)
procura = (1090, 199)
resultado = (1508, 404)
primeira_palavra = (1417, 243)

diretorio = r'C:\Users\janio\Desktop'
os.chdir(diretorio)

#Clica na opção home
pyautogui.moveTo(home, duration=0.5)
pyautogui.click()
sleep(2)

#Clica no link da documentação de pyautogui
pyautogui.moveTo(link_documentos, duration=0.5)
pyautogui.click()
sleep(2)

#Clica no campo do formulário de busca
pyautogui.click(procura)
sleep(1)

#Digita e confirma a busca pelo termo desejado
termo = 'mouse'
pyautogui.typewrite(termo, interval=0.5)
sleep(0.5)
pyautogui.press('enter')
sleep(3)

#Clica no primeiro resultado da busca
pyautogui.click(resultado)
sleep(2)

#Copia a primeira palavra do título
pyautogui.moveTo(primeira_palavra, duration=0.25)
pyautogui.doubleClick(logScreenshot=True)
sleep(1)

#Copia o texto e cola em uma variável
pyautogui.hotkey('ctrl', 'c')
subtitle = paste()
print(subtitle)
