# plot.py

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

# matplotlib setup
mpl.use('pgf')

df1 = pd.read_csv('data/Group4.txt', sep='\t')
df2 = pd.read_csv('data/Group4-2.txt', sep='\t')
df3 = pd.read_csv('data/Group4-3.txt', sep='\t')
df_filter = pd.read_csv('data/Group4-with-filter.txt', sep='\t')
df_no_filter = pd.read_csv('data/group4-without-filter.txt', sep='\t')

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