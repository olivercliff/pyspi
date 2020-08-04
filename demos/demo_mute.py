# Import our classes
from pynats.data import Data
from pynats.ptsa import ptsa

import matplotlib.pyplot as plt
import numpy as np
import statsmodels.tsa.arima_process as arma

# a) Setup time-series configuration
T = 5000
R = 1

# c) Load the data
data = Data()
data.generate_mute_data(n_samples=T, n_replications=R)

calc = ptsa()

calc.load(data)

calc.compute()

calc.prune()

calc.heatmaps(6)
calc.flatten()
calc.clustermap('all')
plt.show()