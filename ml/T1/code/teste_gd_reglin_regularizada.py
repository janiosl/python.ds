import scipy.optimize as opt

def encontrar_theta_otimo(theta, X, y, _lambda):
    return opt.fmin_tnc(func = custo_reglin_regularizada, 
        x0=theta, fprime=gd_reglin_regularizada, 
        args=(X, y, _lambda))

filepath = 'https://github.com/MLRG-CEFET-RJ/ml-class/blob/master/ml-t1/data/ex5data1.mat?raw=true'
r = requests.get(filepath, allow_redirects=True)
open('ex5data1.mat', 'wb').write(r.content)

data = scipy.io.loadmat('ex5data1.mat')

_X, y = data['X'], data['y'] # conjunto de treinamento

X = np.insert(_X, 0, 1, axis=1)

_lambda = 0
result = encontrar_theta_otimo(theta, X, y, _lambda)
theta = result[0]
J = custo_reglin_regularizada(theta, X, y, _lambda)

print('Vetor de parâmetros = ', theta)
print('Custo = ', J)

h = X.dot(theta.T)

plot_ex5data1(_X, y)
plt.plot(_X, h)