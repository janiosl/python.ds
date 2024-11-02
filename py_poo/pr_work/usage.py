# -*- coding: utf-8 -*-
"""
DeoST AD usage
@author: janio
"""

from deost_ad import Evento, GeraTS

import pandas as pd
from matplotlib import pyplot as plt

#Loading data
entrada = 'gecco.csv'
gecco = pd.read_csv(entrada)

#Data analysis
gecco.head()
gecco.describe()

#Subset
series = gecco.ph
reference = gecco.event
plt.plot(series)


#DeoST detector
#Create DeoST object with series
ph = GeraTS(serie=series)

#Model
deost = Evento(s=ph)

#Detection
deost.detect()
print(deost)

#Detection visualization
deost.det_graf()
