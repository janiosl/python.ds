"""
Programa para agendar desligamento do computador.

Desenvolvido por Janio de Souza Lima
Mais projetos e tutoriais em:
http:www.pythonds.com.br
Instagram: @python.ds
"""
import os
from time import sleep
import pyautogui
from datetime import datetime


def desligar(tempo=0):
    """
    Função para desligamento do computador
    
    Parâmetros:
    int tempo: número inteiro de minutos para agendamento do programa
    Padrão: tempo = 0 minutos (desligamento imediato após contagem
    regressiva)

    Retorno: Não há retorno de valor nesta função.
    """
    if tempo > 0:
        agora = datetime.now()
        agora = agora.strftime('%H:%M')
        print(f'Hora de início: {agora}')
        
        if tempo == 1:
            print(f'Desligamento agendado para {tempo} minuto')
        else:
            print(f'Desligamento agendado para {tempo} minutos')
            
        sleep(tempo * 60)

    print(f'O processo de desligamento do computador iniciará em {10} segundos...')
    print('Pressione [CTRL] + [C] antes do final da contagem para cancelar.')

    try:
        contagem = 10
        for k in range(contagem, 0, -1):
            print(k, end='')
            print('.' * (k), end=' ')
            sleep(1)

        os.system('shutdown -s')

    except (KeyboardInterrupt):
        print('\nATENÇÃO: Procedimento abortado pelo usuário.')


def agendador():
    """
    Função cria interface com usuário para agendamento
    do desligamento do computador.
    
    Parâmetros:
    Não há parâmetros para esta função.

    Retorno:
    int tempo: Quantidade de minutos para agendamento
    """
    tempo = pyautogui.prompt('Digte a quantidade de minutos para agendar o desligamento',
                             title='Agendador de desligamento',
                             default='Digite um número inteiro')
    
    if tempo != None:
        if tempo.isnumeric():
            return int(tempo)
    else:
        return None
    

def main():
    tempo = agendador()
    if tempo != None:
        desligar(tempo)
    else:
        print('Programa cancelado.')


main()
