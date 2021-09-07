"""
Programa simula um RPA para automação de um
sistema web.

Formulário usado como exemplo: https://forms.gle/FA2Bxst6VaAJGbvMA

Tutorial com utilização disponível no Canal Python DS:
https://www.youtube.com/channel/UCdpQJDGrM3Xj58ZFF-2UNBA
"""
#IMPORTAÇÃO DE BIBLIOTECAS USADAS NO CÓDIGO
import pyautogui, os
import pandas as pd
from time import sleep

"""
Configurações iniciais:
- Diretório
- Imagem do botão enviar
- Nome da base de dados
"""
#Substituir pelo seu diretório
caminho = r'C:\Users\janio\OneDrive\Área de Trabalho\pythonDS'
os.chdir(caminho)
botao = 'botao_ENVIAR.PNG'
arquivo = 'base.xlsx'
dados = pd.read_excel(arquivo)

"""
Conferência dos dados da planilha
- Após conferência e desenvolvimento do RPA
o trecho abaixo deve ser apago ou desativado para
uso apenas em testes.

for i in range(0, len(dados.NOME)):
    print('Nome: ', dados.iloc[i]['NOME'])
    print('Opção: ', dados.iloc[i]['ESCOLHA'])
    print('Texto: ', dados.iloc[i]['TEXTO'])
    print('Avaliação: ', dados.iloc[i]['AVALIAÇÃO'])
    print('-'*30)
"""

"""
Captura de posições dos campos:
- Captura no shell das posições da tela
usando .position()
"""
cmp_nome = (178, 392)
cmp_escolha1 = (184, 540)
cmp_escolha2 = (182, 576)
cmp_texto = (181, 805)
cmp_aval4 = (562, 967)
cmp_aval5 = (644, 965)
cmp_proximo = (261, 271)

"""
Preenchimento dos campos
"""
for i in range(0, len(dados.NOME)):
    #Nome
    #Aguardar
    sleep(1)

    #Mover para posição e clicar
    pyautogui.moveTo(cmp_nome, duration=0.5)
    pyautogui.click()

    #Aguardar e digitar o conteúdo da planilha
    sleep(1)
    pyautogui.typewrite(dados.iloc[i]['NOME'],
                        interval=0.10)

    #Opção
    #Aguardar
    sleep(1)

    if dados.iloc[i]['ESCOLHA'] == 1:
        #Mover para posição opção 1
        pyautogui.moveTo(cmp_escolha1, duration=0.5)
    else:
        #Mover para posição opção 2
        pyautogui.moveTo(cmp_escolha2, duration=0.5)

    #Clicar
    pyautogui.click()

    #Avaliação
    if dados.iloc[i]['AVALIAÇÃO'] == 4:
        pyautogui.moveTo(cmp_aval4, duration=0.5)
    elif dados.iloc[i]['AVALIAÇÃO'] == 5:
        pyautogui.moveTo(cmp_aval5, duration=0.5)
    else:
        #Observar no programa defintiva todas as opções
        print('Opção inválida')

    #Clicar
    pyautogui.click()

    #Texto
    pyautogui.moveTo(cmp_texto, duration=0.5)
    pyautogui.click()
    sleep(0.5)
    pyautogui.typewrite(dados.iloc[i]['TEXTO'],
                        interval=0.10)

    """
    Envio do formulário
    """
    pyautogui.scroll(-200)
    sleep(1)
    #Reconhecimento de imagem
    enviar = pyautogui.locateCenterOnScreen(botao)
    pyautogui.moveTo(enviar, duration=0.5)
    pyautogui.click()

    #PRÓXIMO
    sleep(1)
    pyautogui.moveTo(cmp_proximo, duration=0.5)
    pyautogui.click()
    sleep(2)
    
