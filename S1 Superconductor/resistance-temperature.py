# resistivity-temperature.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.use('pgf')

# data import 
index_col = ['Time(sec)', 
             'Temperature(K)',
             'Resistance(Ohm)',
             'Current(A)',
             'TempError(K)',
             'ResError(Ohm)',
             'CurrError(A)']
cooling = pd.read_csv('data/221125_cl.dat', sep='\t', skiprows=2, header=0, names=index_col)
heating = pd.read_csv('data/221125_ht.dat', sep='\t', skiprows=2, header=0, names=index_col)

# extract variables
t_cool = np.array(cooling['Time(sec)'])
T_cool = np.array(cooling['Temperature(K)'])
resistance_cool = np.array(cooling['Resistance(Ohm)'])

t_heat = np.array(heating['Time(sec)'])
T_heat = np.array(heating['Temperature(K)'])
resistance_heat = np.array(heating['Resistance(Ohm)'])

# plotting
plt.scatter(T_cool,resistance_cool, label='Resistance (Ohm) cooling', marker='.',
           alpha=.3)
plt.scatter(T_heat,resistance_heat, label='Resistance (Ohm) heating', marker='.',
           alpha=.3)
#plt.scatter(t,T, label='Temperatur (K)')
plt.legend()
plt.xlabel(r'$T /$K') 
plt.ylabel(r'$R / \Omega$')
plt.tight_layout()

plt.savefig('build/resistance-temperature.pdf')
