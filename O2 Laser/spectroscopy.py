import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl

mpl.use('pgf')

data = pd.read_csv('spectroscopy/laser-tube.txt', sep='\t', skiprows=9)

wavelength = data['Wavelength(nm)']
intensity = data['Intensity(Counts)']

intensity = intensity / np.max(intensity)

peak = wavelength[np.argmax(intensity)]
print(f'Peak at lambda = {peak} nm')

plt.plot(wavelength, intensity)
plt.xlabel('Wavelength / nm')
plt.ylabel('Relative intensity')
plt.savefig('build/spectrum.pdf')
