"""
Programa concatena todos os arquivos PDF em um diretório
em um único PDF de destino.

Uso:
    * Para preparação do uso recomenda-se criar um novo diretório e
    armazenar nele os arquivos de origem.
    * Após execução confira o arquivo criado no caminho informado
    pelo programa.

Desenvolvido por Janio de Souza Lima
Mais projetos e tutoriais em:
http:www.pythonds.com.br
Instagram: @python.ds
"""
import os
import PyPDF2 as pdf
from glob import glob


def concatenaPdf(caminho):
    """
    Função procura todos os arquivos pdf do caminho informado
    e, cria uma pasta e armazena um versão em pdf com todos
    arquivos de origem concatenados.

    Argumentos:
        str caminho: diretório dos arquivos de origem
    """
    os.chdir(caminho)

    arquivos = glob('*.pdf')
    destino = r'concatenado\concatenado.pdf'

    #Cria o diretório de resultado, caso não exista
    if not os.path.exists('concatenado'):
        os.makedirs(r'.\concatenado')
        print('Diretório de destino criado\nProsseguindo...')
    else:
        print('Diretório de destino já existente\nProsseguindo...')

    try:
        #Abertura dos arquivos
        pdfWriter = pdf.PdfFileWriter()

        #Leitura de todos os arquivos do diretório
        for j in range(0, len(arquivos)):
            pdfDoc = open(arquivos[j], 'rb')

            pdfReader = pdf.PdfFileReader(pdfDoc)

            #Adiciona todas as páginas de cada arquivo
            for k in range(0, pdfReader.numPages):
                pagina = pdfReader.getPage(k)
                pdfWriter.addPage(pagina)

            pdfResultado = open(destino, 'ab')
            pdfWriter.write(pdfResultado)
            
            pdfDoc.close()
            pdfResultado.close()
    except Exception as exc:
        print('Administrador: verificar existência de exceções')
        return str(exc)

    print(f'Arquivo gerado em:\n{os.getcwd()}\{destino}')
    return f'Arquivo gerado em:\n{os.getcwd()}\{destino}'


def main():
    """
    Função principal para para definição do caminho e
    execução da função de concatenção de arquivos PDF
    """
    #Informe o caminho desejado nesta variável
    caminho = r'D:\Python\estudos\documentos'
    response = concatenaPdf(caminho)
    """
    Uso da variável response apenas para conferir retorno da função.
    Caso não tenha esta necessidade, basta suprimir a variável,
    chamando a função diretamente.
    """

main()
