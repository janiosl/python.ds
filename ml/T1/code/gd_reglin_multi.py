import numpy as np
from custo_reglin_multi import custo_reglin_multi

def gd(X, y, alpha, epochs, theta=np.array([0,0,0], ndmin = 2).T):

    m = len(y)

    cost_history = np.zeros(epochs)

    for i in range(epochs):
        h = X.dot(theta)
        loss = h - y
        gradient = X.T.dot(loss) / m
        theta = theta - (alpha * gradient)
        cost_history[i] = custo_reglin_multi(X, y, theta=theta)

    return cost_history, theta

