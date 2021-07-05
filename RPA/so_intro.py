"""
#RPA PYTHON – INTRODUÇÃO À INTERAÇÃO E CONTROLE DO SISTEMA OPERACIONAL
#Python DS
Tutorial para uso do código: https://youtu.be/KsXIjCl1S5g
"""
import os

#Alterar diretório de trabalho e conferir
#Substituir pelo caminho desejado
caminho = r'D:\Python'
os.chdir(caminho)
os.getcwd()


#Criar um diretório novo
os.mkdir('so')


#Conferência se um diretório existe
os.path.exists('so')

#Conferência se um caminho é um diretório
os.path.isdir('so')


#Criar um diretório verificando se ele já existe
if os.path.exists('so/subdir'):
    print('Diretório já existe')
else:
    os.mkdir('so/subdir')
    print('Diretório criado com sucesso')


#Criação de arquivos e adição de texto
with open('so/subdir/arquivo.txt', 'a') as file:
	file.write('Teste')


#Adição de texto em um arquivo existente
with open('so/subdir/arquivo.txt', 'a') as file:
	file.write('\nTeste 2\nTeste nova linha')


#Leitura de arquivo
with open('so/subdir/arquivo.txt', 'r') as file:
	content = file.read()
	print(content)


#Checagem do conteúdo de um diretório
import glob
glob.glob('*.txt')


#Leitura de um arquivo a partir da checagem
#Analisar o conteudo
arquivos = glob.glob('*.txt')

#Ler o primeiro arquivo
with open(arquivos[0], 'r') as file:
	content = file.read()
	print(content)
	
