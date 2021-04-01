import numpy as np
from custo_reglog import custo_reglog
from sigmoide import sigmoide

def costFunctionReg(theta, X, y, lambda_):
    '''
    Método que calcula e atribui os valores de theta
    '''
    m = len(y)
    
    theta_shape = theta.shape[0]
    
    # atualização de theta
    for theta_index in range(theta_shape):
        value = 0
        for line in range(m):
            z = sigmoide(theta.T.dot(X[line]))
            value += (z - y[line]) * X[line][theta_index]

            if theta_index > 0:
                value += (lambda_/m) * theta[theta_index]

        theta[theta_index] = value
    
    J = custoRegLog_Norm(theta, X, y, lambda_)

    return theta

def custoRegLog_Norm(theta, X, y, lambda_):
    '''
    Função de custo da regressão logística regularizada
    '''
    m = len(y)
    # Cálculo do custo
    cost_last_component = (lambda_ / (2*m)) * (np.sum(theta ** 2))
    J = custo_reglog(theta, X, y) +  cost_last_component
    
    return J