import numpy as np
from util.sigmoide import sigmoide

def custo_reglog_reg(theta, X, y, _lambda):
    m = len(X)
    theta = np.matrix(theta)
    X = np.matrix(X)
    y = np.matrix(y)
    
    grad0 = np.multiply(-y, np.log(sigmoide(X * theta.T)))
    grad1 = np.multiply((1 - y), np.log(1 - sigmoide(X * theta.T)))
    
    # não considera theta0 para o cálculo
    theta_j = theta[:,1:]
    regularizacao = (_lambda / (2 * m)) * np.sum(np.dot(theta_j.T,theta_j))     
    return np.sum((grad0 - grad1) / m) + regularizacao