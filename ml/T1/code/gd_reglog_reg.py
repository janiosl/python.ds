import numpy as np
from util.sigmoide import sigmoide

def gd_reglog_reg(theta, X, y, _lambda):
    m = len(X)
    theta = np.matrix(theta)
    X = np.matrix(X)
    y = np.matrix(y)

    parametros = int(theta.ravel().shape[1])
    grad = np.zeros(parametros)

    erro = sigmoide(X * theta.T) - y

    for i in range(parametros):
        term = np.multiply(erro, X[:,i])
        if (i != 0):
            regularizacao = ((_lambda / m) * theta[:,i])
            grad[i] = (np.sum(term) / m) + regularizacao
        else:
            grad[i] = np.sum(term) / m 

    return grad