"""
Programa simples para geração de um arquivo csv a partir dos dados 
"""
import csv, os

os.chdir(r'D:\Python\pySelfDS')

titulos = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']
dados = [1000, 1050, 750, 1150, 900, 1550]

outputFile = open('dados.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)

#outputWriter.writerow([2015, 2016, 2017, 2018, 2019, 2020])
#outputWriter.writerow([1000, 1050, 1100, 1150, 1200, 1250])
outputWriter.writerow(titulos)
outputWriter.writerow(dados)

outputFile.close()
