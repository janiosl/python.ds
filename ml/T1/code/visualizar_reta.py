import os
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt


def plot(filepath, theta):
    path = os.getcwd() + filepath
    dataset = pd.read_csv(path, header=None)
    X = dataset.iloc[:, 0:-1].values
    y = dataset.iloc[:, -1:].values

    t = np.arange(0, 25, 1)
    plt.scatter(X, y, color='red', marker='x', label='Training Data')
    plt.plot(t, theta[0] + (theta[1]*t), color='blue', label='Linear Regression')
    plt.axis([4, 25, -5, 25])
    plt.title('Populacao da cidade x Lucro da filial')
    plt.xlabel('Populacao da cidade (10k)')
    plt.ylabel('Lucro (10k)')
    plt.legend()
    plt.show()

    filename = 'target/plot1.2.png'
    if not os.path.exists(os.path.dirname(filename)):
        os.makedirs(os.path.dirname(filename))

    plt.savefig(filename)
