import numpy as np


def cofi_cost_func(params, Y, R, num_users, num_movies, num_features, Lambda):

    # Obtem as matrizes X e Theta a partir dos params
    X = np.array(params[:num_movies*num_features]).reshape(num_features, num_movies).T.copy()
    Theta = np.array(params[num_movies*num_features:]).reshape(num_features, num_users).T.copy()


    # Voce deve retornar os seguintes valores corretamente
    J = 0
    X_grad = np.zeros(X.shape)
    Theta_grad = np.zeros(Theta.shape)

    # ====================== SEU CODIGO AQUI ======================
    # Instrucoes: calcular a funcao de custo regularizada e gradiente
    # para a filtragem colaborativa. Concretamente, você deve primeiro
    # implementar a funcao de custo. Depois disso, voce deve implementar o
    # gradiente. 
    #
    # Notas: 
    # X - num_movies x num_features: matriz das caracteristicas dos filmes
    # Theta - num_users x num_features: matriz das caracteristicas dos usuarios
    # Y - num_movies x num_users: matriz de classificacoes de filmes por usuarios
    # R - num_movies x num_users: matriz, onde R (i, j) = 1 se o i-esimo filme
    #       foi avaliado pelo j-esimo usuario
    #
    # =============================================================

    # =============================================================
    #Função de custo baseada na equação da seção 2.1.1
    # =============================================================
    J = (1/2.) * np.sum((np.power(np.dot(X,Theta.T) - Y,2)) * R)

    # =======================================================================
    #Gradiente da filtragem colaborativa baseados nas equações da seção 2.1.2
    # =======================================================================

    # Gradiente para X e Theta:
    # =============================================================
    # X_grad - num_movies x num_features matrix, contendo as
    #   derivadas parciais com relacao a cada elemento de X
    X_grad = np.dot((np.dot(X, Theta.T) - Y ) * R, Theta)
    
    #Linha adicionada apenas para conferir se a matriz gerada
    #tem as dimensões corretas. DESATIVADA APÓS VALIDAÇÃO
    #RESULTADO VALIDADO: (5, 3)
    #print(X_grad, X_grad.shape)
    

    # Theta_grad - num_users x num_features: matriz, contendo as
    #   derivadas parciais com relacao a cada elemento de Theta
    Theta_grad = np.dot(((np.dot(X, Theta.T) - Y ) * R).T, X)

    #Linha adicionada apenas para conferir se a matriz gerada
    #tem as dimensões corretas. DESATIVADA APÓS VALIDAÇÃO
    #RESULTADO VALIDADO: (4, 3)
    #print(Theta_grad, Theta_grad.shape)

    # =============================================================
    #Gradiente para ambos os cojuntos em um único vetor
    # =============================================================
    grad = np.hstack((X_grad.T.flatten(),Theta_grad.T.flatten()))

    return J, grad