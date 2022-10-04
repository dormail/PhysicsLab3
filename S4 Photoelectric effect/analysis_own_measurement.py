# script to plot data we took on our own which showed some error

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# matplotlib setup
mpl.use('pgf')

data = pd.read_csv('data/data.csv')
U = data['U']
current = data.to_numpy()[:,1:]
current_average = np.nanmean(current, axis=1)
current_std = np.nanstd(current, axis=1)

# plotting
plt.clf()
plt.errorbar(U, current_average, xerr=np.ones_like(U)*.5, yerr=current_std, 
            ls='None',
            label='Photo current')

plt.ylabel('Photo current / pA')
plt.xlabel(r'Accelerating voltage / V')
plt.tight_layout()
plt.savefig('build/photocurrent_incorrect.pdf')