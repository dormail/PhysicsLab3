import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.use('pgf')

data = pd.read_csv('intensity.csv')

current = data['Tube Current mA']
I = data['I'] 
I = I / np.max(I)

plt.xlabel(r'Laser current / mA')
plt.ylabel(r'Relative intensity')

plt.scatter(current, I, marker='+')
plt.savefig('build/intensity.pdf')

