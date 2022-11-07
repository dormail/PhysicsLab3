# plot_a.py
# makes the plots

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import ufloat

# n dotted
print("--- n dotted start ---")
a_3A_r1_n = pd.read_csv('data/a_3A_r1_n.txt', sep='\t', skiprows=4)
a_4A_r1_n = pd.read_csv('data/a_4A_r1_n.txt', sep='\t', skiprows=4)
a_5A_r1_n = pd.read_csv('data/a_5A_r1_n.txt', sep='\t', skiprows=4)

# curve fit
def linear(x,m,b):
    return m*x + b

popt, pcov = curve_fit(linear, a_3A_r1_n['Current I_A1 / A'], a_3A_r1_n['Voltage U_B1 / V'])
m_3A, b_3A = popt
m_err, b_err = np.sqrt(np.diag(pcov))
print('3A')
m = ufloat(m_3A, m_err)
b = ufloat(b_3A, b_err)
print(f'm = {m}')
print(f'b=  {b}')

popt, pcov = curve_fit(linear, a_4A_r1_n['Current I_A1 / A'], a_4A_r1_n['Voltage U_B1 / V'])
m_4A, b_4A = popt
print('4A')
m = ufloat(m_4A, m_err)
b = ufloat(b_4A, b_err)
print(f'm = {m}')
print(f'b=  {b}')

popt, pcov = curve_fit(linear, a_5A_r1_n['Current I_A1 / A'], a_5A_r1_n['Voltage U_B1 / V'])
m_5A, b_5A = popt
print('5A')
m = ufloat(m_5A, m_err)
b = ufloat(b_5A, b_err)
print(f'm = {m}')
print(f'b=  {b}')


I = np.linspace(np.min(a_3A_r1_n['Current I_A1 / A']), np.max(a_3A_r1_n['Current I_A1 / A']))

plt.scatter(a_3A_r1_n['Current I_A1 / A'], a_3A_r1_n['Voltage U_B1 / V'], marker='.', alpha=0.3,
           label='3A')
plt.plot(I, linear(I, m_3A, b_3A))


plt.scatter(a_4A_r1_n['Current I_A1 / A'], a_4A_r1_n['Voltage U_B1 / V'], marker='.', alpha=0.3,
           label='4A')
plt.plot(I, linear(I, m_4A, b_4A))

plt.scatter(a_5A_r1_n['Current I_A1 / A'], a_5A_r1_n['Voltage U_B1 / V'], marker='.', alpha=0.3,
            label='5A')
plt.plot(I, linear(I, m_5A, b_5A))

plt.legend()
plt.xlabel('Current / A')
plt.ylabel('Hall Voltage / V')
plt.tight_layout()

plt.savefig('build/V-A-n.pdf')
print("--- n dotted end ---")

# p dotted
plt.clf()
print("--- p dotted start ---")
a_3A_r1_n = pd.read_csv('data/a_3A_r1_p.txt', sep='\t', skiprows=4)
a_4A_r1_n = pd.read_csv('data/a_4A_r1_p.txt', sep='\t', skiprows=4)
a_5A_r1_n = pd.read_csv('data/a_5A_r1_p.txt', sep='\t', skiprows=4)

# curve fit
def linear(x,m,b):
    return m*x + b

popt, pcov = curve_fit(linear, a_3A_r1_n['Current I_A1 / A'], a_3A_r1_n['Voltage U_B1 / V'])
m_3A, b_3A = popt
m_err, b_err = np.sqrt(np.diag(pcov))
print('3A')
m = ufloat(m_3A, m_err)
b = ufloat(b_3A, b_err)
print(f'm = {m}')
print(f'b=  {b}')

popt, pcov = curve_fit(linear, a_4A_r1_n['Current I_A1 / A'], a_4A_r1_n['Voltage U_B1 / V'])
m_4A, b_4A = popt
print('4A')
m = ufloat(m_4A, m_err)
b = ufloat(b_4A, b_err)
print(f'm = {m}')
print(f'b=  {b}')

popt, pcov = curve_fit(linear, a_5A_r1_n['Current I_A1 / A'], a_5A_r1_n['Voltage U_B1 / V'])
m_5A, b_5A = popt
print('5A')
m = ufloat(m_5A, m_err)
b = ufloat(b_5A, b_err)
print(f'm = {m}')
print(f'b=  {b}')


I = np.linspace(np.min(a_3A_r1_n['Current I_A1 / A']), np.max(a_3A_r1_n['Current I_A1 / A']))

plt.scatter(a_3A_r1_n['Current I_A1 / A'], a_3A_r1_n['Voltage U_B1 / V'], marker='.', alpha=0.3,
           label='3A')
plt.plot(I, linear(I, m_3A, b_3A))


plt.scatter(a_4A_r1_n['Current I_A1 / A'], a_4A_r1_n['Voltage U_B1 / V'], marker='.', alpha=0.3,
           label='4A')
plt.plot(I, linear(I, m_4A, b_4A))

plt.scatter(a_5A_r1_n['Current I_A1 / A'], a_5A_r1_n['Voltage U_B1 / V'], marker='.', alpha=0.3,
            label='5A')
plt.plot(I, linear(I, m_5A, b_5A))

plt.legend()
plt.xlabel('Current / A')
plt.ylabel('Hall Voltage / V')
plt.tight_layout()

plt.savefig('build/V-A-p.pdf')
print("--- p dotted end ---")

# e dotted
plt.clf()
print("--- non dotted start ---")
a_3A_r1_n = pd.read_csv('data/a_3A_r1_e.txt', sep='\t', skiprows=4)
a_4A_r1_n = pd.read_csv('data/a_4A_r1_e.txt', sep='\t', skiprows=4)
a_5A_r1_n = pd.read_csv('data/a_5A_r1_e.txt', sep='\t', skiprows=4)

# curve fit
def linear(x,m,b):
    return m*x + b

popt, pcov = curve_fit(linear, a_3A_r1_n['Current I_A1 / A'], a_3A_r1_n['Voltage U_B1 / V'])
m_3A, b_3A = popt
m_err, b_err = np.sqrt(np.diag(pcov))
print('3A')
m = ufloat(m_3A, m_err)
b = ufloat(b_3A, b_err)
print(f'm = {m}')
print(f'b=  {b}')

popt, pcov = curve_fit(linear, a_4A_r1_n['Current I_A1 / A'], a_4A_r1_n['Voltage U_B1 / V'])
m_4A, b_4A = popt
print('4A')
m = ufloat(m_4A, m_err)
b = ufloat(b_4A, b_err)
print(f'm = {m}')
print(f'b=  {b}')

popt, pcov = curve_fit(linear, a_5A_r1_n['Current I_A1 / A'], a_5A_r1_n['Voltage U_B1 / V'])
m_5A, b_5A = popt
print('5A')
m = ufloat(m_5A, m_err)
b = ufloat(b_5A, b_err)
print(f'm = {m}')
print(f'b=  {b}')


I = np.linspace(np.min(a_3A_r1_n['Current I_A1 / A']), np.max(a_3A_r1_n['Current I_A1 / A']))

plt.scatter(a_3A_r1_n['Current I_A1 / A'], a_3A_r1_n['Voltage U_B1 / V'], marker='.', alpha=0.3,
           label='3A')
plt.plot(I, linear(I, m_3A, b_3A))


plt.scatter(a_4A_r1_n['Current I_A1 / A'], a_4A_r1_n['Voltage U_B1 / V'], marker='.', alpha=0.3,
           label='4A')
plt.plot(I, linear(I, m_4A, b_4A))

plt.scatter(a_5A_r1_n['Current I_A1 / A'], a_5A_r1_n['Voltage U_B1 / V'], marker='.', alpha=0.3,
            label='5A')
plt.plot(I, linear(I, m_5A, b_5A))

plt.legend()
plt.xlabel('Current / A')
plt.ylabel('Hall Voltage / V')
plt.tight_layout()

plt.savefig('build/V-A-e.pdf')
print("--- non dotted end ---")
