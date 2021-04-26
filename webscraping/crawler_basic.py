"""
Programa para rastreamento básico de conteúdo
de sites usando técnicas de web scraping.
1. As primeiras funções obtém o conteúdo bruto,
os títulos e parágrafos
2. A função main organiza a execução

OBS.: Para reutilização das funções em outros programas
basta remover a execução de main() e importar as funções
para os programas desejados, integrando-as, ao código
da forma desejada.
Desenvolvimento: Janio de Souza Lima
www.pythonds.com.br
"""
import requests, re
from bs4 import BeautifulSoup

"""Criação das funções"""
def crawler(url):
    """
    Função executa a captura do conteúdo bruto
    do site e o converte para um objeto BeautifulSoup
    parâmetros:
    url = url completa do site a ser capturado
    """
    try:
        page = requests.get(url)

        #O restante do código depende do sucesso da request
        #Isto é conferido pelo status = 200
        if page.status_code != 200:
            print('O servidor não respondeu à busca')
            return None
        else:
            bs = BeautifulSoup(page.content, 'html.parser')
            return bs
    except Exception as exc:
        print(f'Houve uma falha na varredura.\nErro: {exc}')
        return None


def titulo(bs, title_tag='h1'):
    """
    Função executa a captura o(s) título(s)
    do site e o(s) converte em uma lista de strings
    parâmetros:
    url = url completa do site a ser capturado
    title_tag = tag html para identificação de títulos
    tag padrão 'h1'
    """
    titulo = bs.find_all(title_tag)
    if titulo == None:
        print('Não foi possível recuperar títulos da página')
        return None
    else:
        titulo = [titulo[k].get_text()
                  for k in range(0, len(titulo))]

        #Limpeza de quebra de linhas
        titulo = [re.sub('\n', ' ', titulo[k])
                  for k in range(0, len(titulo))]
        return titulo


def texto(bs):
    """
    Função executa a captura do texto de parágrafos
    do site e os converte em uma lista de strings
    parâmetros:
    url = url completa do site a ser capturado
    title_tag = tag html para identificação de títulos
    tag padrão 'h1'
    """
    paragrafos = bs.find_all('p')
    if paragrafos == None:
        print('Não foi possível recuperar texto da página')
        return None
    else:
        texto = [paragrafos[k].get_text()
                 for k in range(0, len(paragrafos))]
        return texto


def main():
    """
    Função principal para chamada das funções que executam o crawler
    e fazem tratamento do conteúdo.
    Esta execução acessa um site de notícias, captura o título principal
    e os parágrafos, exibindo-os em linhas separadas.
    No site do exemplo, cada parágrafo representa uma matéria/notícia.
    """
    #Substituir a url pelo site desejado
    url = 'http://www.globo.com'
    bs = crawler(url)

    title_tag = 'h1'
    title = titulo(bs, title_tag)
    
    paragrafos = texto(bs)
    
    if title != None:
        for k in range(0, len(title)):
            print(f'Titulo: {title[k]}')

    if paragrafos != None:
        print('=' * 80)
        print('Conteúdo:')
        for k in range(0, len(paragrafos)):
            print(paragrafos[k])
            print('-' * len(paragrafos[k]))


"""Execução do programa"""
#Eliminar a linha abaixo se for apenas chamar as funções em outro programa
main()
