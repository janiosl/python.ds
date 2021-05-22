#Importações do PyTorch para criação da Rede Neural
import torch
import torch.nn as nn
import torch.nn.functional as F

##Criação da classe da Rede Neural
##============================================
class Net_(nn.Module):
  # Define nn
  #def __init__(self, neur):
  def __init__(self, dimX, nC, neur):
    """
    Definição da Redeu Neural
    Parametros:
    dimX int: Entradas na primeira camada (quantidade de atributos)
    nC int:  Neurônios de saída (quantidade de classes possíveis)
    neur int: Neurônios na camada oculta
    """
    super(Net_, self).__init__()

    ##Camada oculta
    ##==============
    #Recebe neurônios = quantidade de atributos
    #Entrega quantidade de neurônios da camada oculta
    self.fc1 = nn.Linear(dimX, neur)

    ##Camada de saída
    ##==============
    #Recebe neurônios da camada oculta
    #Entrega quantidade de neurônios das classes possíveis
    self.fc2 = nn.Linear(neur, nC)

    #Uso da função Sigmoid para classificação binária
    self.output = nn.Sigmoid()

  def forward(self, X):
    """
    Definição do passo forward
    """
    X = F.relu(self.fc1(X))
    X = F.relu(self.fc2(X))
    X = self.output(X)

    return X