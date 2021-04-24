import pandas as pd
import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt
import scipy.io

def normalize_features(X):
	mu = np.mean(X,axis=0)
	sigma = np.std(X,axis=0)
	normalized_X = np.divide(X - mu,sigma)

	return (normalized_X, mu, sigma)

def pca(X):
	########################
	# SEU CODIGO AQUI :
	# Essa funcao deve retornar U e S, duas das
	# tres matrizes geradas pela decomposicao
	# da matriz de covariância de X.
	########################
	#Define m como o número de exemplos de X
	m = X.shape[0]

	#Calcula a matriz de covariância
	mc = (1/m) * np.dot(X, X.T)

	#Decomposição da matriz de covariância (SVD)
	U, S, V = np.linalg.svd(mc)

	return (U, S)

def project_data(X, U, K):
	U_reduce = U[:, 0:K]
	Z = np.zeros((len(X), K))
	for i in range(len(X)):
		x = X[i,:]
		projection_k = np.dot(x, U_reduce)
		Z[i] = projection_k
	return Z

def recover_data(Z, U, K):
	X_rec = np.zeros((len(Z), len(U)))
	for i in range(len(Z)):
		v = Z[i,:]
		for j in range(np.size(U,1)):
			recovered_j = np.dot(v.T,U[j,0:K])
			X_rec[i][j] = recovered_j
	return X_rec

def explain_variance(S):
	########################
	### SEU CÓDIGO AQUI  ###
	########################

	# implement code to print the percentages 
	# of variation for each dimension.
	pass

def main():
	raw_mat = scipy.io.loadmat("../data/ex7data1.mat")
	X = raw_mat.get("X")
	plt.cla()
	plt.plot(X[:,0], X[:,1], 'bo')
	plt.show()

	X_norm, mu, sigma = normalize_features(X)
	U, S = pca(X_norm)

	plt.cla()
	plt.axis('equal')
	plt.plot(X_norm[:,0], X_norm[:,1], 'bo')

	K = 2
	for axis, color in zip(U[:K], ["yellow","green"]):
		start, end = np.zeros(2), (mu + sigma * axis)[:K] - (mu)[:K]
		plt.annotate('', xy=end,xytext=start, arrowprops=dict(facecolor=color, width=1.0))
	plt.axis('equal')
	plt.show()

	K = 1
	Z = project_data(X_norm, U, K)
	X_rec = recover_data(Z, U, K)

	plt.cla()
	plt.plot(X_norm[:,0], X_norm[:,1], 'bo')
	plt.plot(X_rec[:,0], X_rec[:,1], 'rx')
	plt.axis('equal')
	plt.show()

	explain_variance(S)

if __name__ == "__main__":
	main()
