import numpy as np

def polyFeatures(X, p):
    
    X_poly = np.zeros((X.shape[0], p))
    for i in range(p):
        X_poly[:, i] = X[:, 0] ** (i + 1)

    return X_poly