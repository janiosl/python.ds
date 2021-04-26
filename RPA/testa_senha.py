"""
Programa simples para demonstrar aplicação das
opções de caixa de diálogo da biblioteca Py AutoGUI
"""
import pyautogui

k = 0
while True:
    #Senha original digitada diretamente no código como exemplo.
    senha = 'Code Game'
    digitado = pyautogui.password(text='Digite sua senha:', title='Testa senha: Senha')

    #Lógica simples para confirmar se a senha digitada é correta
    if senha == digitado:
        pyautogui.alert(text='Senha correta', title='Testa senha: Acesso concedido')
        mensagem = pyautogui.prompt(text='Digite uma mensagem para o robô', title='Testa senha: Mensagem')
        confirma = pyautogui.confirm(text=f'Confirma a mensagem digitada?\n{mensagem}',
                                     buttons=('Sim', 'Não'), title='Testa senha: Confirmação')
        if confirma == 'Sim':
            print(f'A mensagem digitada foi: "{mensagem}".')
            break
    else:
        pyautogui.alert(text='Senha incorreta.\nTente novamente', title='Testa senha: Acesso negado')
        k += 1

    if k >= 3:
        pyautogui.alert(text='ATENÇÃO: Acesso negado.\nNúmero de tentativas excedido!', title='Testa senha: Acesso negado')
        print('Não houve mensagem digitada')
        break

if k >= 1:
    print(f'Ocorreram {k} tentativas erradas de digitação da senha')
