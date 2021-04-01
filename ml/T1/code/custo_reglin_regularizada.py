import numpy as np

def custo_reglin_regularizada(theta, X, y, _lambda):
    # Quantidade de exemplos
    m = len(X)
    theta = np.matrix(theta)

    # não considera theta0 para o cálculo
    theta_j = theta[:,1:]
    regularizacao = (_lambda /(2 * m)) * np.sum(theta_j.dot(theta_j.T))    

    erro = X.dot(theta.T) - y

    # Computa a função de custo J
    J = (np.sum(np.power(erro, 2)))/ (2 * m) 
    
    return J + regularizacao