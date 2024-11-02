# -*- coding: utf-8 -*-
"""
Time series online event detector
@author: janio
"""
import random
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from gerats import GeraTS

#Class for time series event detection
class Evento:
    """Time series event detector"""
    def __init__(self, s=GeraTS()):
        self.serie = s.serie
        self.cp = s.cp
        self.ev = None
        self.sens = None
        self.type_sens = False
        self.pr = [None, None]
        self.lim = [None, None]
        
    def det_param(self, pointer=30):
        """Calculates mean and standard deviation detection parameters"""
        mu_base = np.mean(self.serie[:pointer])
        std_base = np.std(self.serie[:pointer])
        
        param = [mu_base, std_base]
        self.param = param
        
        return mu_base, std_base
    
    def lim_calc(self, pr, sensitivity=0.2, type_sens = False):
        """Calculates the upper and lower limits of the detection threshold"""
        if type_sens == True:
            self.sens = sensitivity
            lim = (pr[0] * (1+(1-sensitivity)), pr[0] * sensitivity)
        else:
            lim = (pr[0] + 1.5*pr[1], pr[0] - 1.5*pr[1])
        
        return lim
    
    def detect(self, type_sens = False, w=30, sensitivity=0.2, adaptive=False):
        if type_sens == True:
            if sensitivity < 0 or sensitivity > 1:
                return '*** Sensitivity invalid. It must be between 0 and 1 ***'
        
        """Detect events in the time series"""
        self.type_sens = type_sens
        serie = self.serie
        #Step 1 - Initialize event vector
        ev = []
        
        #Step 2 - Set initial parameters
        #    Step 2.1 - Calc mean and standard deviation
        if adaptive == False:
            mu_base = np.mean(serie)
            std_base = np.std(serie)
        else:
            mu_base = np.mean(serie[:w])
            std_base = np.std(serie[:w])
        
        pr = (mu_base, std_base)
        
        #    Step 2.2 - Calc threshold
        lim = self.lim_calc(pr=pr, sensitivity=sensitivity, type_sens = type_sens)
        
        #Step 3 - Slide througout the series
        pointer = w + 1
        batch = 0
        #print(f'Current batch={batch}')
        #print('Walking through the series...', end='')
        #    Step 3.1 - Compare each new observation with threshold
        #    Step 3.2 - Append events position in the event vector
        
        while pointer < len(serie):
            if serie[pointer] > lim[0]:
                ev.append(pointer)
            elif serie[pointer] < lim[1]:
                ev.append(pointer)
            #print('.', end='')
            pointer += 1
            if pointer % w == 0:
                batch += 1
                #print(f'\n    Batch changed. Current batch={batch}')
                if adaptive == True:
                    #    Step 3.3 - Check new batches and update parameters                    
                    pr = self.det_param(pointer)
                    lim = self.lim_calc(pr, sensitivity, type_sens)
                    #print(f'New threshold: {lim}')
                    
                #print('Walking through the series...', end='')
        #print('\nEnd of time series.')
        
        self.ev = ev
        self.pr = pr
        self.lim = lim
            
        return ev, pr, lim

    def det_graf(self, cp_lines=True):
        """Generates a graph with the detection result"""
        if self.ev == None: return 'There are no events detected yet.'
        
        ev_value = [self.serie[i] for i in self.ev]
        ev_dic = dict(zip(self.ev, ev_value))

        print('Events detected:', len(self.ev))
        print(f'Initial parameters: mu={self.pr[0]}, sigma={self.pr[1]}')
        print('Threshold', self.lim)

        plt.plot(self.serie, label = 'Values')
        plt.ylabel('Time')
        plt.xlabel('Values')
        plt.axhline(y=self.pr[0], c = 'red', ls = '--', label='Mean')
        plt.axhline(y=self.lim[0], c = 'gray', label = 'Threshold')
        plt.axhline(y=self.lim[1], c = 'gray')
        for k,v in ev_dic.items():
            plt.plot(k, v, marker='o', c = 'green')
        plt.legend(loc='best')
        if self.type_sens == True:
            plt.title('Sensitivity-based detection')
            plt.annotate(f'Sensitiviry={self.sens}', xy=(150,50))
        else:
            plt.title('IQR statistics-based detection of outliers')
            plt.annotate(f'Sigma={round(self.pr[1], 2)}', xy=(150,50))
        if cp_lines == True:
            for c in self.cp:
                plt.axvline(x=c, ymin=0, ymax=1, c = 'gray', ls = '--')
    
    def metricas(self, reference):
        """Under construction"""
        m = []
        return m
    
    def __repr__(self):
        content = f'Series with {len(self.serie)} observations.\n'
        p = f'Parameters: mu={self.pr[0]}, sigma={self.pr[1]}\n'
        l = f'Threshold: {self.lim}\n'
        if self.type_sens == True:
            p = f'Parameters: sensitivity={self.sens}, mu={self.pr[0]}, sigma={self.pr[1]}\n'
            t = 'Detection based on sensitivity - '
        else:
            t = 'Detection based on IQR - '
        if self.ev == None: 
            e = 'There are no events detected yet.'
        else:
            e = t+f'Events detected: {len(self.ev)}'
        return content+p+l+e
