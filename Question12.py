import numpy as np
import matplotlib.pyplot as plt

def g(x):
    return np.exp(-x*x)
def h(x):
    return np.exp(-4*x*x)
def conv(x):
    return np.exp(-4*x*x/5)*np.sqrt(np.pi/5)


n = 20
x = np.linspace(-n/2, n/2, 1000)
y_g = g(x)
y_h = h(x)
y_fft = np.fft.fft(y_g, norm = 'ortho')*np.fft.fft(y_h, norm = 'ortho')
y_num = np.fft.fft(y_fft, norm='ortho')
y_dft = np.fft.fftshift(y_num)
y_dft = y_dft*np.sqrt(n*(x[1]-x[0]))
y = conv(x)




plt.plot(x, y, label ='analytical convolution')
plt.plot(x, np.abs(y_dft), label = 'Convolution using DFT')
plt.title('Convolved Function')
plt.xlabel('x')
plt.ylabel('[g*h](x)')


plt.tight_layout()
plt.legend()
plt.show()
