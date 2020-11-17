# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 09:07:31 2020

@author: Janio Lima
Canal Python DS:
https://www.youtube.com/channel/UCdpQJDGrM3Xj58ZFF-2UNBA?view_as=subscriber

Referências:
MCKINNEY, Wes. Python para análise de dados. São Paulo: Novatec, 2018.
NIELD, Thomas. Introdução à linguagem SQL. São Paulo: Novatec, 2016.
"""
#Biblioteca para trabalho com banco de dados sqlite3
import sqlite3

estrutura_db = """
CREATE TABLE CLIENTES (
    ID_CLIENTE    INTEGER    PRIMARY KEY    AUTOINCREMENT    NOT NULL,
    NOME          TEXT       NOT NULL,
    ENDERECO      TEXT,
    CIDADE        TEXT,
    ESTADO        TEXT
);
"""

#Se o arquivo não existir, ele é criado com o código a seguir
con = sqlite3.connect('dados_vendas.db')

con.execute(estrutura_db)
con.commit()

con.close()
