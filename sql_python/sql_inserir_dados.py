# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 09:30:23 2020

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

#Inserir dados apenas com alguns campos
inserir = """
INSERT INTO CLIENTES(NOME, ESTADO)
VALUES(?, ?);"""

dados = [('Janio', 'RJ')]

#Executar e salvar (commit) a inserção
con.executemany(inserir, dados)
con.commit()

#Conferir os dados inseridos
cursor = con.execute("SELECT * FROM CLIENTES;")
cursor.fetchall()


#Inserir dados com todos campos (EXCETO CHAVE PRIMÁRIA)
inserir = """
INSERT INTO CLIENTES(NOME, ENDERECO, CIDADE, ESTADO)
VALUES(?, ?, ?, ?);"""

dados = ('Cecilia', 'Reservado', 'Jaguaribe', 'CE')

#Executar e salvar (commit) a inserção
con.execute(inserir, dados)
con.commit()

#Conferir os dados inseridos
cursor = con.execute("SELECT * FROM CLIENTES;")
cursor.fetchall()


#Inserir múltiplos registros
inserir = """
INSERT INTO CLIENTES(NOME, ENDERECO, CIDADE, ESTADO)
VALUES(?, ?, ?, ?);"""

dados = [('Tatiane', 'Copacabana Palace', 'Rio de Janeiro', 'RJ'),
         ('José Alves', 'Place Vendomê, 15', 'Paris', 'Île-de-France'),
         ('Francisca Léo', 'Place Vendomê, 15', 'Paris', 'Île-de-France'),
         ('Maria Zilda', 'S Las Vegas Blvd', 'Las Vegas', 'NV')
         ]

#Executar e salvar (commit) a inserção
con.executemany(inserir, dados)
con.commit()

#Conferir os dados inseridos
cursor = con.execute("SELECT * FROM CLIENTES;")
cursor.fetchall()

con.close()
