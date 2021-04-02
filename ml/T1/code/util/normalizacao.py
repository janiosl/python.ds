import numpy as np

# normalização Z-Score
def normalizar_caracteristica(X):
    mean_X = np.mean(X, axis=0)
    std_X = np.std(X, axis=0)
    X_norm = (X - mean_X) / std_X
    return X_norm, mean_X, std_X