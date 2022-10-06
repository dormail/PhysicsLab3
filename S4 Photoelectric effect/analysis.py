# script to plot data we took on our own which showed some error

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from uncertainties import ufloat
from scipy.optimize import curve_fit

# matplotlib setup
mpl.use('pgf')

# data import
data = pd.read_csv('data/data.csv')
U = data['U']
current = data.to_numpy()[:,1:]
current_average = np.nanmean(current, axis=1)
current_std = np.nanstd(current, axis=1)
current_rel_std = current_std / current_average


# output as tex table
# data frame with all new data and output as tex table
data.insert(len(data.columns), 'average', current_average)
data.insert(len(data.columns), 'std', current_std)
data.insert(len(data.columns), 'rel_std', current_rel_std*100)

# modified line_terminator to include a percentage symbol
data.to_csv('build/our_data.tex',
            sep='&',
            float_format="%.2f",
            header=False,
            index=False,
            decimal='.',
            line_terminator='\% \\\\\n')

# linear fit for U<0
def linear(x, m, b):
    return m*x + b

current_average_red = current_average[:31]
U_red = U[:31]

popt, pcov = curve_fit(linear, U_red, current_average_red,
          p0=(3,300))
m, b = popt
m_err, b_err = np.sqrt(np.diag(pcov))

m_u = ufloat(m, m_err)
b_u = ufloat(b, b_err)

print(f'm = {m_u}')
print(f'b = {b_u}')

# import ta data
data = pd.read_csv('data/data_ta.csv')
data['current (nA)'] *= 1000 # conversion to pA
data_np = data.to_numpy()
U_ta = data_np[:,0]
A_ta = data_np[:,1] 

# output as tex table 
data.to_csv('build/ta_data.tex',
            sep='&',
            float_format="%.2f",
            header=False,
            index=False,
            decimal='.',
            line_terminator=' \\\\\n')

# plotting
plt.clf()
plt.errorbar(U, current_average, xerr=np.ones_like(U)*.5, yerr=current_std, 
            ls='None',
            label='Our measurement data',
             color='k')

plt.plot(U_red, linear(U_red, m, b),
         c='r',
         alpha=1,
         label=r'linear curve fit for $U_\text{C}<0$')

plt.scatter(U_ta,A_ta,
           marker='+',
            label='TA data')

plt.ylabel('Photo current / pA')
plt.xlabel(r'Accelerating voltage $U_\text{C}/$ V')
plt.tight_layout()
plt.legend()
plt.savefig('build/photocurrent.pdf')
