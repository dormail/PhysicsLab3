# plot.py

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np


df1 = pd.read_csv('data/Group4.txt', sep='\t')
df2 = pd.read_csv('data/Group4-2.txt', sep='\t')
df3 = pd.read_csv('data/Group4-3.txt', sep='\t')
df_filter = pd.read_csv('data/Group4-with-filter.txt', sep='\t')
df_no_filter = pd.read_csv('data/group4-without-filter.txt', sep='\t')

## compare maxima
red_peak = df_filter['Wavelength(nm)'][np.argmax(df_filter['Intensity(Counts)'])]
green_peak = df3['Wavelength(nm)'][np.argmax(df3['Intensity(Counts)'])]


ratio = green_peak / red_peak
print(f'Green preak = {green_peak}')
print(f'Red preak = {red_peak}')
print(f'ratio = {ratio}')

## Plotting

# matplotlib setup
mpl.use('pgf')

plt.scatter(df_filter['Wavelength(nm)'], df_filter['Intensity(Counts)'],
           c='r',
           marker='+',
           label='Original laser')
#plt.scatter(df_no_filter['Wavelength(nm)'], df_no_filter['Intensity(Counts)'],
#           c='g')
#plt.scatter(df2['Wavelength(nm)'], df2['Intensity(Counts)'],
#           c='g')
plt.scatter(df3['Wavelength(nm)'], df3['Intensity(Counts)'],
           c='lightgreen',
           marker='+',
           label='SHG')
plt.xlabel('Wavelength / nm')
plt.ylabel('Intensity / counts')
plt.legend()
plt.tight_layout()
plt.savefig('build/spectrum.pdf')



