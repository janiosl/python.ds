import matplotlib.pyplot as plt
import scipy.io
import requests

def plot_ex5data1(X, y):
    plt.figure(figsize=(8,5))
    plt.xlabel('Mudança no nível da água (x)')
    plt.ylabel('Água saindo da barragem (y)')
    plt.plot(X,y,'rx')
