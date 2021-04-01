import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def importarDados(filepath):
    path = os.getcwd() + filepath  
    data = pd.read_csv(path, header=None)

    X = data.iloc[:, 0:-1].values
    y = data.iloc[:, -1:].values

    return X, y
