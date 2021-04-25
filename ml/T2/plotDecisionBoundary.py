import numpy as np
import matplotlib.pyplot as plt 
from mapFeature import mapFeature

def plotDecisionBoundary(theta, X, y):
 
    theta = np.array(theta)

    if X.shape[1] <= 3:
        plot_x = np.array([np.min(X[:, 1]) - 2, np.max(X[:, 1]) + 2])

        #calcular fronteira de decisão
        plot_y = (-1. / theta[2]) * (theta[1] * plot_x + theta[0])

        #ajuste 
        plt.plot(plot_x, plot_y)

        #legendas
        plt.legend(['Admitido', 'Não admitido', 'Fronteira de decisão'])
        plt.xlim([30, 100])
        plt.ylim([30, 100])
    else:
        #alcance do grid
        u = np.linspace(-1, 1.5, 50)
        v = np.linspace(-0.8, 1.2, 50)

        z = np.zeros((u.size, v.size))
        
        for i, ui in enumerate(u):
            for j, vj in enumerate(v):
                z[i, j] = np.dot(mapFeature(ui, vj), theta)

        z = z.T  
        
        plt.contour(u, v, z, levels=[0], linewidths=2, colors='g')
        plt.contourf(u, v, z, levels=[np.min(z), 0, np.max(z)], cmap='Greens', alpha=0.4)