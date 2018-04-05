import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack
from scipy.io import wavfile

fs, data = wavfile.read('C:/Users/Henry/Documents/commands/pocketsphinx/recordings/16bit/sample-drone-noise.wav')

# Number of samplepoints
N = 600
# sample spacing
T = 1.0 / 800.0
x = np.linspace(0.0, N*T, N)
y = data
yf = scipy.fftpack.fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N/2)

fig, ax = plt.subplots()
ax.plot(xf, 2.0/N * np.abs(yf[:N//2]))
plt.show()