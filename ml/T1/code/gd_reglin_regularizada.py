import numpy as np

def gd_reglin_regularizada(theta, X, y, _lambda):
    m = len(X)
    theta = np.matrix(theta)
    X = np.matrix(X)
    y = np.matrix(y)

    erro = (X.dot(theta.T)) - y
    
    gradient = X.T.dot(erro) / m

    theta_j = theta[:,1:]
    regularizacao = (_lambda / m) * theta_j
    # insere zero como termo de regularização para theta0
    regularizacao = np.insert(regularizacao, 0, 0, axis=1)

    return gradient + regularizacao.T
