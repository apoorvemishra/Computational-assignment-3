import numpy as np
import matplotlib.pyplot as plt

def box(x):
    q = []
    for i in x:
        if abs(i)>1: q.append(0)
        else: q.append(1)
    return np.array(q)



n = 10
x = np.linspace(-n/2, n/2, 1000)
y_box = box(x)
y_fft = np.fft.fft(y_box, norm = 'ortho')**2
y_num = np.fft.fft(y_fft, norm='ortho')
y_dft = np.fft.fftshift(y_num)
y_dft = y_dft*np.sqrt(n*(x[1]-x[0]))




plt.plot(x, y_box, label ='analytical convolution')
plt.plot(x, np.abs(y_dft), label = 'Convolution using DFT')
plt.title('Convoltion of Box function with itself')
plt.xlabel('x')
plt.ylabel('[box*box](x)')


plt.tight_layout()
plt.legend()
plt.show()
