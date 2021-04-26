"""
Bloco de Notas Simples
Desenvolvido por Janio de Souza Lima
Adaptado de @papa_programmer
"""
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfile, asksaveasfilename

win = Tk()
win.title('noteJan v0.01 - Desenvolvido com Python')

#Funções do menu
def open_file():
    """Função abre um arquivo de texto"""
    blank.delete('1.0', END)
    file = askopenfile(title='noteJan: Abrir arquivo',
                       mode='r',
                      filetypes=[('Arquivos de texto', '*.txt')])

    if file is not None:
        text = file.read()
        blank.insert('1.0', text)


def save_file():
    """Função salva o arquivo de texto em uso"""
    notepad_text = blank.get('1.0', 'end-1c')
    file = asksaveasfilename(title='noteJan: Salvar arquivo',
                             filetypes=[('Arquivos de texto', '*.txt')])

    with open(file, 'w') as data:
        data.write(notepad_text)


#Criação dos menus
menubar = Menu(win)
win.config(menu=menubar)
filemenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label='Arquivo', menu=filemenu)
filemenu.add_command(label='Abrir', command=open_file)
filemenu.add_command(label='Salvar', command=save_file)

menubar.add_command(label='Sair', command=win.destroy)

blank = Text(win, font=('arial', 11))
blank.pack()

win.mainloop()
