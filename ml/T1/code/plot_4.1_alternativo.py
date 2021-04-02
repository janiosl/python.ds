#Outras alternativas de geração do gráfico  

def plotData(X, y, filename = 'target/plot4.1.png'):
  labels = ['Microchip Test 1', 'Microchip Test 2']
  legends = ['$y=1$: Aceito', '$y=0$: Rejeitado']

  # gerando o grafico de dispersao para analise preliminar dos dados
  positive = y == 1
  negative = y == 0

  fig, ax = plt.subplots(figsize=(12,8))
    
  ax.scatter(X[positive, 0], X[positive, 1],
               c='b', marker='+', label=legends[0],
               alpha=0.6)
    
  ax.scatter(X[negative, 0], X[negative, 1],
               c='r', marker='o', label=legends[1],
               alpha=0.6)
    
  #ax.set_yticks([-0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1, 1.2])
  #ax.set_xticks([-1, -0.5, 0, 0.5, 1, 1.5])

  ax.legend()

  ax.set_xlabel(labels[0])
  ax.set_ylabel(labels[1])

  sns.despine()
  plt.savefig(filename)
  plt.show()

def dispers(data, filename = 'target/plot4.1.png'):

    # gerando o grafico de dispersao para analise preliminar dos dados

    positivo = data[data['Resultado'].isin([1])]
    negativo = data[data['Resultado'].isin([0])]

    fig, ax = plt.subplots(figsize=(12,8))
    
    ax.scatter(positivo['Test 1'], positivo['Test 2'],
               s=50, c='b', marker='+', label='$y=1$: Aceito',
               alpha=0.6)
    ax.scatter(negativo['Test 1'], negativo['Test 2'],
               s=50, c='r', marker='o', label='$y=0$: Rejeitado',
               alpha=0.6)
    ax.set_yticks([-0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1, 1.2])
    ax.set_xticks([-1, -0.5, 0, 0.5, 1, 1.5])
    ax.legend()
    ax.set_xlabel('Microchip Test 1')
    ax.set_ylabel('Microchip Test 2')

    if not os.path.exists(os.path.dirname(filename)):
        os.makedirs(os.path.dirname(filename))

    sns.despine()
    plt.savefig(filename)
    plt.show()
