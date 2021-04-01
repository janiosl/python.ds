import scipy.optimize as opt
from custo_reglin_regularizada import custo_reglin_regularizada
from gd_reglin_regularizada import gd_reglin_regularizada

def minimizar_funcao(theta, X, y, _lambda):
    return opt.fmin_tnc(func = custo_reglin_regularizada, 
                        x0 = theta, 
                        fprime = gd_reglin_regularizada, 
                        args = (X, y, _lambda))