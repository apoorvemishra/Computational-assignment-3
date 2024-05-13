import numpy as np
import matplotlib.pyplot as plt




x = np.linspace(-10, 10, 1000)
y = np.zeros(len(x)) + 9
X_custom = np.fft.fft(y, norm='ortho')
freq_fft = np.fft.fftfreq(len(y), d=(x[1]-x[0]))


plt.plot(freq_fft, np.abs(X_custom))
plt.title('Magnitude of DFT (Custom)')
plt.xlabel('Frequency (k)')
plt.ylabel('|X(k)|')


plt.show()
