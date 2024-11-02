# -*- coding: utf-8 -*-
"""
Time series generator
@author: janio
"""
import random
import numpy as np
from matplotlib import pyplot as plt

#random.seed(31)

#Class for time series generation
class GeraTS:
    """Time series generator"""
    def __init__(self, serie=[]):
        self.serie = serie
        self.cp = []
        self.chg = []
        
    def gera_aleatoria(self, tamanho):
        """Generate a random time series with a normal distribution"""
        self.serie = np.random.randn(tamanho)
        
    def gera_cp(self, tamanho, lim, chg_size, positive=False):
        """Generate a random time series with values between lim[0] and lim[1]"""
        #Define parâmetros da série
        if tamanho > 30:
            start = 7
        elif tamanho > 100:
            start = 30
        else:
            start = 0
        cp = random.randrange(start, tamanho)
        dw = lim[0]
        up = lim[1]
        if positive == True:
            chg = (100 + random.randrange(chg_size[0],chg_size[1]))/100
        else:
            chg = (100 - random.randrange(chg_size[0],chg_size[1]))/100
        dw_cp = int(dw * chg)
        up_cp = int(up * chg)
        
        #Gera série
        before = [random.randrange(dw,up) for t in range(0,cp)]
        after = [random.randrange(dw_cp,up_cp) for t in range(cp,tamanho)]
        
        #Atributos
        self.serie = before + after
        self.cp.append(cp)
        self.chg.append(chg)
        
    def add_cp(self, chg_size, new_points, positive=False):
        """Add synthetic change points to the time series"""
        if positive == True:
            chg = (100 + random.randrange(chg_size[0],chg_size[1]))/100
        else:
            chg = (100 - random.randrange(chg_size[0],chg_size[1]))/100
        
        mu = np.mean(self.serie) * chg
        sigma = np.std(self.serie)  * chg
        
        add_points = int(len(self.serie) * new_points)
        
        before = self.serie
        after = np.random.normal(mu, sigma, add_points)
        
        self.serie = before + list(after)
        self.cp.append(len(before))
        self.chg.append(chg)
    
    def grafico(self):
        """Generates a time series line plot"""
        plt.plot(self.serie)
        for c in self.cp:
            plt.axvline(x=c, ymin=0, ymax=1, c = 'gray', ls = '--')
        
        plt.ylabel('Values')
        plt.xlabel('Time')
        
        #plt.close()
        
    def head(self, rows=5):
        """Displays the first rows of the time series"""
        print(self.serie[:rows])
    
    def tail(self, rows=5):
        """Displays the last rows of the time series"""
        print(self.serie[-rows:])
        
    def __repr__(self):
        return f'Time series: {self.serie}'