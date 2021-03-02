# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 11:09:42 2020

@author: Janio Lima
Canal Python DS:
https://www.youtube.com/channel/UCdpQJDGrM3Xj58ZFF-2UNBA?view_as=subscriber

Referências:
MCKINNEY, Wes. Python para análise de dados. São Paulo: Novatec, 2018.
NIELD, Thomas. Introdução à linguagem SQL. São Paulo: Novatec, 2016.
"""

import sqlite3
import pandas as pd

import os

os.chdir(r'D:\Python\PyAD')

con = sqlite3.connect('dados_vendas.db')

#Consulta simples
#Query
cursor = con.execute("SELECT * FROM CLIENTES;")

#Carregar e exibir resulado da query
resultado = cursor.fetchall()
resultado

#Carregar resultado em um DataFrame
consulta_sql = pd.DataFrame(resultado,
                            columns=[campo[0]
                                     for campo in cursor.description])


#Transformar/Tratar dados antes da carga
query = """
SELECT * FROM CLIENTES
WHERE ESTADO!=?;
"""

query2 = """
SELECT * FROM CLIENTES
WHERE ESTADO=?;
"""

parametro = [("RJ")]
cursor = con.execute(query2, parametro)

resultado = cursor.fetchall()
resultado

#Carregar resultado em um DataFrame
clientes_RJ = pd.DataFrame(resultado,
                            columns=[campo[0]
                                     for campo in cursor.description])

#Encerrar conexão com o banco de dados
con.close()
