"""
pySelfDS: Programa simples para integrar análises estatísticas e
data visualization com interface gráfica do Tkinter.

Arquivos necessários:
pySelfDS.py : Programa principal
ler_csv.py : Carga dos dados de arquivo csv
gera_csv.py : Gera um arquivo csv com o padrão necessário
dados.csv : Arquivo csv com os dados para análise

OBSERVAÇÕES:
* Funções criadas de maneira simples, apenas para demonstrar
a conexão entre a interface gráfica e as análises.
* Dados usados com variáveis globais e ausência de tratamentos
de contexto devem ser ajustados em caso de interesse de uso
mais adequado da ideia de integração.

Desenvolvido por Janio de Souza Lima
Instagram: @python.ds
www.pythonds.com.br
"""
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import asksaveasfilename, askopenfile
from matplotlib import pyplot as plt
import numpy as np

#Bibliotecas personalizadas
from ler_csv import ler_csv

versão = 0.03

#Funções para aplicação nos menus
def grafico():
    """Geração do gráfico e do relatório textual"""
    title = 'Evolução dos dados ao longo dos anos'
    
    plt.plot(years, dados)
    plt.title(title)
    plt.show()


def sumario():
    """Geração do gráfico e do relatório textual"""
    title = 'Evolução dos dados ao longo dos anos'
    media = np.mean(dados)
    maximo = max(dados)
    minimo = min(dados)
    amplitude = maximo - minimo
    total = sum(dados)
    ocorrencias = len(dados)
    mediana = np.median(dados)

    cabecalho = f'Sumário dos dados:'
    linha = '\n' + ('-' * 100) + '\n'
    sumario = f'Observações: {ocorrencias}\nAmplitude: {amplitude:.2f}\nTotal: {total:.2f}'
    analise = f'Estatística descriva:\nMédia: {media:.2f}\nMediana: {mediana:.2f}'
    
    texto = title + linha + cabecalho + linha + sumario + linha + analise
    
    blank.delete('1.0', END)
    blank.insert('1.0', abertura + texto)


def completa():
    """Geração do gráfico e do relatório textual"""
    title = 'Evolução dos dados ao longo do tempo'
    media = np.mean(dados)
    maximo = max(dados)
    minimo = min(dados)
    amplitude = maximo - minimo
    total = sum(dados)
    ocorrencias = len(dados)
    mediana = np.median(dados)

    cabecalho = f'Sumário dos dados:'
    linha = '\n' + ('-' * 100) + '\n'
    sumario = f'Observações: {ocorrencias}\nAmplitude: {amplitude:.2f}\nTotal: {total:.2f}'
    analise = f'Estatística descriva:\nMédia: {media:.2f}\nMediana: {mediana:.2f}'
    
    texto = title + linha + cabecalho + linha + sumario + linha + analise
    
    blank.delete('1.0', END)
    blank.insert('1.0', abertura + texto)
    
    plt.plot(years, dados)
    plt.title(title)
    plt.show()


def save_file():
    """Função salva o arquivo de texto em uso"""
    notepad_text = blank.get('1.0', 'end-1c')
    file = asksaveasfilename(title='Python.DS: Salvar relatório',
                             filetypes=[('Arquivos de texto', '*.txt')])

    with open(file, 'w') as data:
        data.write(notepad_text)


def open_file():
    """Função abre um arquivo de texto"""
    blank.delete('1.0', END)
    file = askopenfile(title='Python.DS: Carregar relatório',
                       mode='r',
                       filetypes=[('Arquivos de texto', '*.txt')])

    if file is not None:
        text = file.read()
        blank.insert('1.0', text)
        

def limpar():
    """Função abre um arquivo de texto"""
    blank.delete('1.0', END)
    blank.insert('1.0', abertura)


#Programa principal

"""
Para utilizar dados diretamente no código, remova os comentários
das linhas abaixo e substitua pelos dados para análise
"""
#years = [2015, 2016, 2017, 2018, 2019, 2020]
#dados = [1000, 1050, 1100, 1150, 1200, 1250]

"""
Para utilizar dados carregados de um arquivo csv, matenha o código
abaixo e grave um arquivo com o nome dados.csv no mesmo diretório
do programa.
A primeira linha deve ter os anos ou meses
A segunda linha deve conter os dados

OBS.: O script gera_csv.py pode ser usado para gerar o arquivo com
o padrão adequado.
"""
#Carga dos dados de um arquivo csv
years, dados = years, dados = ler_csv('dados.csv')

obs = {years[k]: dados[k] for k in range(0, len(dados))}
abertura = 'Dados:\n'+str(obs)+'\n\n'

win = Tk()
win.title(f'Py SelfDS: Análise de dados - v{versão}')

menubar = Menu(win)
win.config(menu=menubar)
dashmenu = Menu(menubar, tearoff=0)
estatmenu = Menu(menubar, tearoff=0)
reportmenu = Menu(menubar, tearoff=0)

#Opções do menu de análise visual
menubar.add_cascade(label='Análise visual', menu=dashmenu)
dashmenu.add_command(label='Análise gráfica', command=grafico)
dashmenu.add_command(label='Análise completa', command=completa)

#Opções do menu de análise estatística
menubar.add_cascade(label='Análise estatística', menu=estatmenu)
estatmenu.add_command(label='Sumário dos dados', command=sumario)
estatmenu.add_command(label='Limpar análise', command=limpar)


#Opções do menu de tratamento de relatórios textuais
menubar.add_cascade(label='Relatório', menu=reportmenu)
reportmenu.add_command(label='Salvar relatório textual', command=save_file)
reportmenu.add_command(label='Carregar relatório textual', command=open_file)

#Opção de encerramento do programa
menubar.add_command(label='Sair', command=win.destroy)

blank = Text(win, font=('arial', 11))
blank.pack()
blank.insert('1.0', abertura)

win.mainloop()
