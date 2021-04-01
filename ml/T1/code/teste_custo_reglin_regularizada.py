import scipy.io
import requests
import numpy as np

filepath = 'https://github.com/MLRG-CEFET-RJ/ml-class/blob/master/ml-t1/data/ex5data1.mat?raw=true'
r = requests.get(filepath, allow_redirects=True)
open('ex5data1.mat', 'wb').write(r.content)

data = scipy.io.loadmat('ex5data1.mat')

_X, y = data['X'], data['y'] # conjunto de treinamento
_Xval, yval = data['Xval'], data['yval'] # conjunto de desenvolvimento
_Xtest, ytest = data['Xtest'], data['ytest'] # conjunto de teste

X = np.insert(_X, 0, 1, axis=1)
Xval = np.insert(_Xval , 0, 1, axis=1)
Xtest = np.insert(_Xtest, 0, 1, axis=1)

_lambda = 1
theta = np.array([[1,1]]) #inicialização
J = custo_reglin_regularizada(theta, X, y, _lambda)
print('Custo = ', J)