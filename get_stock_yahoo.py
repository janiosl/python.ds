# -*- coding: utf-8 -*-
"""
Script para carga de dados do Yahoo Finance

Vídeo com aula sobre uso deste script de forma agendada disponível
na playlist abaixo (Canal Python DS):
https://www.youtube.com/playlist?list=PL0XxTDj23A1Ftg-rb_pIaFE3pPROwWtbw

Desenvolvido por Janio de Souza Lima
"""
import os
import pandas as pd
import pandas_datareader as pdr
import datetime


def get(tickers, startdate, enddate):
  """
  Realiza downoads dos dados a partir da base do Yahoo
  Agrupa por acao e ordena por data
  
  Função apresentada no livro:
  Rodrigues, Paulo Leonardo Vieira. Python Aplicado: Bolsa de Valores
  Um guia para construção de análises e indicadores

  param:
    tickers => Lista contendo códigos das ações desejadas
    startdate => Data do início do período a ser carregado
    enddate => Data do final do período a ser carregado
  """
  def data(ticker):
    #Download dos dados
    return (pdr.get_data_yahoo(ticker,
                               start=startdate,
                               end=enddate))

  #Aplica funcao de download aos papeis desejados
  datas = map(data, tickers)

  #Retorna os dados organizados
  return (pd.concat(datas,
                    keys=tickers,
                    names=['Ticker', 'Date']))

try:
  #Configurações para rodar função
  os.chdir(r'D:\Python\PyAD')

  hoje = datetime.datetime.now()
  hoje_str = str(hoje.day) + '-' + str(hoje.month) + '-' + str(hoje.year)
  arquivo = 'yahoo_stock_' + hoje_str + '.csv'

  #Dados da carteira
  t = ['GGBR4.SA'] #Substituir pelos códigos de ações desejadas

  #Definir data de início
  s = datetime.datetime(2010, 1, 1)

  #Final considerada d - 1
  e = hoje - datetime.timedelta(1)
  #Substituir por um periodo diferente se for preciso
  #e = datetime.datetime(2020, 9, 25)

  ativo = get(t, s, e)
  #ativo.tail() #Consultar últimos dias de movimento das ações
  #ativo.head() #Consultar primeiros dias de movimento das ações

  ativo.to_csv(arquivo)

  #Conferência - Desativar comentários para conferir
  #from matplotlib import pyplot as plt
  #import seaborn as sns
  """
  dados = pd.read_csv(arquivo)

  plt.plot(dados['Close'])
  sns.despine()
  """
  print('Extração de dados concluída com sucesso')
  print(f'Arquivo gerado: {arquivo}')
except:
  print('Ocorreu um erro na extração dos dados')
