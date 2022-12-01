# critical_temperature.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from uncertainties import ufloat

mpl.use('pgf')


index_col = ['Time(sec)', 
             'Temperature(K)',
             'Resistance(Ohm)',
             'Current(A)',
             'TempError(K)',
             'ResError(Ohm)',
             'CurrError(A)']
cooling = pd.read_csv('data/221125_cl.dat', sep='\t', skiprows=2, header=0, names=index_col)
heating = pd.read_csv('data/221125_ht.dat', sep='\t', skiprows=2, header=0, names=index_col)

t_cool = np.array(cooling['Time(sec)'])
T_cool = np.array(cooling['Temperature(K)'])
resistance_cool = np.array(cooling['Resistance(Ohm)'])

t_heat = np.array(heating['Time(sec)'])
T_heat = np.array(heating['Temperature(K)'])
resistance_heat = np.array(heating['Resistance(Ohm)'])

from scipy.optimize import curve_fit

# define fit function
def fit_fun(x, m, b, A, s, C):
    linear = m * x + b
    critical = A * np.arctan((x - C) * s)

    return linear + critical

# fit and create plot for cooling
popt, pcov = curve_fit(fit_fun, T_cool, resistance_cool, p0=[0.0001, 0, 0.001, 100, 70])
error = np.sqrt(np.diag(pcov))
T_C_unc = error[-1]

m, b, A, s, T_C = popt

T_C_unc = ufloat(T_C, T_C_unc)

print(f'T_C during cooling process: {T_C_unc}')

T = np.linspace(50,300,1000)

plt.scatter(T_cool,resistance_cool, label='Resistance (Ohm) cooling', marker='.',
           alpha=.2)

plt.plot(T, fit_fun(T, m, b, A, s, T_C), c='k', label='Fit function')

#plt.scatter(t,T, label='Temperatur (K)')
plt.legend()
plt.xlabel(r'$T /$K') 
plt.ylabel(r'$R / \Omega$')
plt.tight_layout()
plt.savefig('build/fit_cooling.pdf')


# now do the same for heating
plt.clf()
popt, pcov = curve_fit(fit_fun, T_heat, resistance_heat, p0=[0.0001, 0, 0.001, 100, 100])
error = np.sqrt(np.diag(pcov))
T_C_unc = error[-1]

m, b, A, s, T_C = popt

T_C_unc = ufloat(T_C, T_C_unc)

print(f'T_C during heating process: {T_C_unc}')

T = np.linspace(50,300,1000)

plt.scatter(T_heat,resistance_heat, label='Resistance (Ohm) heating', marker='.',
           alpha=.2)

plt.plot(T, fit_fun(T, m, b, A, s, T_C), c='k', label='Fit function')

#plt.scatter(t,T, label='Temperatur (K)')
plt.legend()
plt.xlabel(r'$T /$K') 
plt.ylabel(r'$R / \Omega$')
plt.tight_layout()
plt.savefig('build/fit_heating.pdf')
