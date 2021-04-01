import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def importarDados(filepath, names):
    path = os.getcwd() + filepath  
    data = pd.read_csv(path, header=None, names=names)

    X = data.iloc[:, 0:-1].values
    y = data.iloc[:, -1:].values

    return X, y


def plot():
    X, y = importarDados(filepath="/data/ex1data1.txt", names=["Population","Profit"])

    plt.scatter(X.T, y, color='red', marker='x')
    plt.title('Populacao da cidade x Lucro da filial')
    plt.xlabel('Populacao da cidade (10k)')
    plt.ylabel('Lucro (10k)')

    filename = 'target/plot1.1.png'
    if not os.path.exists(os.path.dirname(filename)):
      os.makedirs(os.path.dirname(filename))

    plt.savefig(filename)
    plt.show()