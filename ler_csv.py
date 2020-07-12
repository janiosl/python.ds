import csv

def ler_csv(filename):
    """
    Função para leitura de dados de um arquivo csv e registro em listas
    para utlização em análises.
    Argumentos:
        filename = arquivo .csv a ser analisado
        OBSERVAÇÃO: A primeira linha deve ter os dados de tempo (meses, anos,
        etc.) e a segunda deve conter os dados.

    Retorno:
        periodo = lista de strings
        dados = lista de floats com os dados
    """
    csvFile = open(filename)
    csvReader = csv.reader(csvFile)
    csvData = list(csvReader)
    periodo = csvData[0]
    dados = [float(csvData[1][k]) for k in range(0, len(csvData[1]))]
    
    csvFile.close()
    
    return periodo, dados
