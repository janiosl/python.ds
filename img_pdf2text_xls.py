"""
Programa para leitura de imagens ou pdf e conversão para formatos
tratáveis por RPAs (TXT, XLSX, CSV,etc).

Desenvolvimento: Janio de Souza Lima
Citações: algumas partes foram inspiradas ou
adapatadas dos estudos do livro Web Scraping
com Python, da escritora Ryan Mitchell, ótima
leitura para aprofundar o tema e ver em prática
a junção de OCR e PDF para varredura e interpretação
de dados da web.

OBSERVAÇÃO: Além das bibliotecas abaixo é necessária
a instalação da ferramenta Google Tesseract

Documentação do projeto Google Tesseract:
https://github.com/tesseract-ocr/tesseract

Documentação do Tesseract para Python:1
https://pypi.org/project/pytesseract/
"""

import os, csv, pytesseract, time
from PIL import Image
from pytesseract import Output
from io import StringIO, open
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams

#Criação de funções
def lerPDF(pdf):
    """
    Função para leitura do pdf
    param:
    pdf: nome do arquivo pdf a ser lido
    """
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    process_pdf(rsrcmgr, device, pdf)
    device.close()

    content = retstr.getvalue()
    retstr.close()
    return content

def limpeza(filePath, newFilePath):
    """
    Função para limpeza de imagens borradas ou com fundos
    criados para dificultar leitura por bots
    param:
    filePath: arquivo original (diretorio e nome)
    newFilePath: arquivo gerado (diretorio e nome)
    """
    
    image = Image.open(filePath)

    #Define um valor de limiar para a imagem e salva
    image = image.point(lambda x: 0 if x < 143 else 255)
    image.save(newFilePath)
    return image


#####################
#Aplicação de funções
diretorio = r'C:\Users\xpto\Documents\Projetos\imagens2xls'
os.chdir(diretorio)

"""
Este trecho do programa uso o Google Tesseract para realizar a conversão
diretamente de imagens. Não estamos usando funções, mas o código
poderia ser 'encapsulado' em uma função para melhor reaproveitamento
"""

print('=' * 60)
print(f'{"Convertendo pdf (tipo imagem) em arquivo excel (tipo csv)":^60}')
print('=' * 60)
arquivo = str(input('Digite o nome do arquivo a ser convertido: '))

if arquivo != '':
    convertido_name = arquivo[:-4]+'.xls' #Ajustar extensão da saída conforme necessário
    arquivo_novo = 'texto_limpo_T.jpg'

    try:

        #Exibir o arquivo analisado
        original = Image.open(arquivo)
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

        #Limpar arquivo
        image = limpeza(arquivo, arquivo_novo)

        #Converter
        print('Resultado da conversão:')
        print('-' * 60)
        print(f'{pytesseract.image_to_string(Image.open(arquivo))}')
        
    except Exception as err:
        print(f'Não possível converter o arquivo\nErro: {err}')
        

    confirma_jpg = input('Deseja exportar o conteúdo? [S/N]').upper().strip()[0]

    if confirma_jpg == 'S':
        with open(convertido_name, 'w') as convertido:
            print(f'Leitura do texto da imagem {arquivo}:\n'+\
                  f'\n{pytesseract.image_to_string(Image.open(arquivo))}',
                  file=convertido)
            print(f'PDF convertido em CSV. Arquivo salvo: {convertido_name}')

    time.sleep(2)
    
else:
    print('Nenhum arquivo foi informado')
    print()


"""
Este trecho do programa uso a função criada no início do codigo para realizar a
conversão a partir de PDF 'puros'.
"""

print('=' * 60)
print(f'{"Convertendo pdf (comum) em arquivo texto":^60}')
print('=' * 60)

arquivo = str(input('Digite o nome do arquivo a ser convertido: '))

if arquivo != '':
    exportado = arquivo[:-4]+'.txt' #Ajustar extensão da saída conforme necessário

    try:
        print('Resultado da conversão:')
        print('-' * 60)
        pdf = open(arquivo, 'rb')

        conteudo = lerPDF(pdf)
        print(conteudo)
        pdf.close()
        
    except Exception as err:
        print(f'Não possível converter o arquivo\nErro: {err}')

    confirma = input('Deseja exportar o conteúdo? [S/N]').upper().strip()[0]
    if confirma == 'S':
        with open(exportado, 'w', newline='') as arquivo:
            print(conteudo, file=arquivo)
            print(f'Conteúdo exportado em {diretorio}\{arquivo.name}')
else:
    print('Nenhum arquivo foi informado')
    print()

print('Programa concluído')
