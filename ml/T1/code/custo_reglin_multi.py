import numpy as np


def custo_reglin_multi(X, y, theta):
    # Quantidade de exemplos
    m = len(y)

    # Computa a funcao de custo J
    J = (np.sum((X.dot(theta)- y)**2)) / (2 * m)

    return J
