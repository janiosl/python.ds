import os
import numpy as np
import matplotlib.pyplot as plt

#Usado para plotar 3d em fig.gca
from mpl_toolkits.mplot3d import Axes3D


def plot(J):
    # Valores de theta0 e theta1 informados no enunciado do trabalho
    theta0 = np.arange(-10, 10, 0.01)
    theta1 = np.arange(-1, 4, 0.01)

    # Comandos necessarios para o matplotlib plotar em 3D
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    # Plotando o grafico de superficie
    theta0, theta1 = np.meshgrid(theta0, theta1)
    surf = ax.plot_surface(theta0, theta1, J)
    plt.xlabel('theta_0')
    plt.ylabel('theta_1')
    plt.show()

    filename = 'target/plot1.3.2.png'
    if not os.path.exists(os.path.dirname(filename)):
        os.makedirs(os.path.dirname(filename))

    plt.savefig(filename)

    return surf
