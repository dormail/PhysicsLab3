import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.use('pgf')

def crit_cond(T, T_C):
    if T < T_C:
        return 0
    return float(T*T*T)
crit_cond = np.vectorize(crit_cond, otypes=[float])

T_C = 1
T = np.linspace(0,2.5, num=10000)
plt.plot(T, crit_cond(T,T_C))
plt.xlabel(r'$T / T_C$')
plt.ylabel(r'$\rho$')
plt.tight_layout()

plt.savefig('build/conductivity_example.pdf')


