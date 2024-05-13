import numpy as np
import matplotlib.pyplot as plt

def sinc(x):
    return np.sinc(x/np.pi)
def rect(k):
    kq = []
    for i in k:
        if abs(i)>1/(2*np.pi): kq.append(0)
        else: kq.append(1)
    return np.array(kq)/(2*np.pi)


n = 2000
x = np.linspace(-n/2, n/2, 10000)
y = sinc(x)
d = x[1]-x[0]
X_fft = np.fft.fft(y, norm='ortho')
freq_fft = np.fft.fftfreq(len(y), d)

plt.plot(freq_fft, np.abs(X_fft), label='FFT')
plt.plot(freq_fft, rect(freq_fft), label = 'analytical')

plt.title('Magnitude of DFT')
plt.xlabel('Frequency (k)')
plt.ylabel('|X(k)|')
plt.legend()
plt.grid(True)
plt.show()
