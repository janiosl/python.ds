def calculateCost_linearReg(theta, X, y, lambda_):

    y_pred = X.dot(theta.T)
    m = len(y)    

    # Cálculo do custo
    cost = (1/(2*m))*np.sum(np.square(y_pred-y))
    regularization_component = (lambda_/(2*m)) * np.sum(np.square(theta[1:]))
    J = cost + regularization_component

    return J

​
def linearRegCostFunction(theta, X, y, lambda_):
  """
    Método que implementa o cálculo do custo da regressão linear regularizada e do gradiente descendente
  """

    # definição das variáveis
    theta = np.array(theta, ndmin=2)
    m = len(y)
    y = np.array(y, ndmin=2).T
    theta_size = 2
    grad = np.zeros(theta_size)

    # Cálculo do custo
    J = calculateCost_linearReg(theta, X, y, lambda_)
    print("J= {}".format(str(J)))

    # atualização de theta
    for j in range(theta_size):
        value = 0
        for i in range(m):
            value += (X[i].dot(theta.T) - y[i]) * X[i][j]

        if j > 0:
            value += (lambda_/m) * theta[:,j]

        grad[j] = (value*(1/m))

    return grad
