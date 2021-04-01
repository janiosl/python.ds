import numpy as np

def custo_reglin_uni(X, y, theta):

    # Quantidade de exemplos de treinamento
    m = len(y)

    # Computar a funcao do custo J
    J = (np.sum((X.dot(theta) - y)**2)) / (2 * m)

    return J

