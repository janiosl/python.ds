"""
#Caixas de diálogo para interação com usuários
#Python DS
Tutorial para uso do código: https://youtu.be/DD0rkoBl1IU
"""
from pyautogui import alert, confirm, prompt, password

#=======================================================
#Alerta: Caixas simples para mensagens rápidas
#=======================================================

mensagem = 'Inscreva-se no Python DS agora'
alert(mensagem,
      title='Python DS',
      button='Inscrição realizada')

#=======================================================
#Perguntas: Caixas para perguntas objetivas ao usuário
#=======================================================
pergunta = 'Já curtiu este vídeo?'

resposta = confirm(pergunta,
                   buttons=['Sim', 'Curtirei agora'])
print(resposta)


#Uso da resposta no código
if resposta.upper()[0] == 'S':
    print('Obrigado!')
else:
    print('O que está esperando!')


#=======================================================
#Prompt: Caixas para digitaçao pelo usuário
#=======================================================
resposta = prompt('Qual canal ensina Python toda semana?')
alert(resposta)

#=======================================================
#Senha: Caixas para receber senhas com texto oculto
#=======================================================
sucesso = password('Qual segredo do sucesso?')
alert(sucesso)

