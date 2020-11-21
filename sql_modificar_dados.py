# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 10:46:51 2020

@author: Janio Lima
Canal Python DS:
https://www.youtube.com/channel/UCdpQJDGrM3Xj58ZFF-2UNBA?view_as=subscriber

Referências:
MCKINNEY, Wes. Python para análise de dados. São Paulo: Novatec, 2018.
NIELD, Thomas. Introdução à linguagem SQL. São Paulo: Novatec, 2016.
"""


import sqlite3

"""
TABELA: CLIENTES

CAMPOS:
    ID_CLIENTE    INTEGER    PRIMARY KEY    AUTOINCREMENT    NOT NULL,
    NOME          TEXT       NOT NULL,
    ENDERECO      TEXT,
    CIDADE        TEXT,
    ESTADO        TEXT
"""

con = sqlite3.connect('dados_vendas.db')

alterar = """
UPDATE CLIENTES
SET
ENDERECO = ?,
CIDADE = ?,
ESTADO = ?
WHERE ID_CLIENTE = ?;
"""

dados = ("Lake Buena Vista",
         "Orlando",
         "FL",
         2)


#Executar alterações
con.execute(alterar, dados)
con.commit()


#Conferir os dados inseridos
cursor = con.execute("SELECT * FROM CLIENTES;")
cursor.fetchall()

con.close()
