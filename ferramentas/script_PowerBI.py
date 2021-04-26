# -*- coding: utf-8 -*-
"""
Template de script para carga de dados no Power BI

Desenvolvimento por Janio Lima

Vídeo com aula sobre uso deste script para carga de dados
no Power BI: https://www.youtube.com/watch?v=UqnY1JhqBEk
"""


import os, sqlite3
import pandas as pd

os.chdir(r'D:\Python\PyAD') #Substituir pelo caminho correto

#Criar conexão
con = sqlite3.connect('dados_vendas.db') #Substituir pelo nome do db

#Realizar query e armazenar em um objeto pandas
cursor = con.execute("SELECT * FROM CLIENTES;") #Usar query desejada
resultado = cursor.fetchall()

consulta_sql = pd.DataFrame(resultado,
                            columns=[campo[0]
                                     for campo in cursor.description])

#Encerrar conexão
con.close()
