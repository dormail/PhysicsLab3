import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl

mpl.use('pgf')

data = pd.read_csv('spectroscopy/laser-tube.txt', sep='\t', skiprows=9)
background = pd.read_csv('spectroscopy/background-tube.txt', sep='\t', skiprows=9)

wavelength = data['Wavelength(nm)']
intensity = data['Intensity(Counts)']
bg = background['Intensity(Counts)']

signal = intensity - bg

signal = signal / np.max(signal)

peak = wavelength[np.argmax(signal)]
print(f'Peak at lambda = {peak} nm')

plt.plot(wavelength, signal)
#plt.plot(wavelength, bg)
plt.xlabel('Wavelength / nm')
plt.ylabel('Relative intensity')
plt.savefig('build/spectrum.pdf')

plt.clf()


plt.plot(wavelength, intensity+40000, label='Raw data + 40000')
plt.plot(wavelength, bg + 20000, label='Background + 20000')
plt.plot(wavelength, intensity - bg, label='Clean signal', alpha=.5)

plt.xlabel('Wavelength / nm')
plt.ylabel('Relative intensity')

plt.legend()
plt.savefig('build/spectrum_clean.pdf')

