import pandas as pd
import numpy as np

def read_dataset(filepath):
    data = pd.read_csv(filepath, header=None)

    X = data.iloc[:, 0:-1].values
    y = data.iloc[:, -1:].values

    # X --> matriz de dados, y --> vetor de resposta
    return X, y