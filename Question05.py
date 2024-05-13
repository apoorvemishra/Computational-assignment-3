import numpy as np
import matplotlib.pyplot as plt
import time


def compute_dft(x):
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    e = np.exp(-2j * np.pi * k * n / N)
    X = np.dot(e, x)
    return X

x = np.linspace(-100, 100, 1000)
y = []
n = range(4,1000)

for i in n:
    y.append(np.random.rand(i))

t_custom = []
t_fft = []
for q in y:
    begin = time.time()
    X_custom = compute_dft(q)
    end = time.time()
    t_custom.append(end-begin)


for q in y:
    begin = time.time()
    X_fft = np.fft.fft(q)
    end = time.time()
    t_fft.append(end-begin)


plt.figure(figsize=(10, 6))

plt.plot(n, t_custom, label='Custom DFT')
plt.plot(n, t_fft, label='numpy.fft')

plt.title('Time taken by numpy.fft and custom made DFT')
plt.xlabel('n')
plt.ylabel('Computational time')
plt.legend()
plt.grid(True)

plt.show()
