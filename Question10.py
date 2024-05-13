import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the Gaussian function
def gaussian(x, y):
    return np.exp(- (x**2 + y**2))

# Define the range and step size for x and y
N = 500  # Number of points
L = 200   # Range (-L/2 to L/2)
dx = L / N
dy = L / N  # Define dy similarly to dx
x = np.linspace(-L/2, L/2, N)
y = np.linspace(-L/2, L/2, N)

# Create a meshgrid
X, Y = np.meshgrid(x, y)

# Calculate the Gaussian function
f = gaussian(X, Y)

# Compute the two-dimensional Fourier transform
F = np.fft.fftshift(np.fft.fft2(f)) * dx * dy

# Compute the frequencies in the Fourier domain
kx = np.fft.fftshift(np.fft.fftfreq(N, dx))
ky = np.fft.fftshift(np.fft.fftfreq(N, dy))
Kx, Ky = np.meshgrid(kx, ky)

# Analytical Fourier Transform of the Gaussian function
analytical_F = np.exp(- (Kx**2 + Ky**2)*np.pi*np.pi)* np.pi

# Create 3D plots
fig = plt.figure(figsize=(10, 5))

# Numerical result
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(Kx, Ky, np.abs(F), alpha=0.8)
ax1.set_title('Numerical Fourier Transform')
ax1.set_xlabel('Kx')
ax1.set_ylabel('Ky')
ax1.set_zlabel('|F(Kx, Ky)|')

# Analytical result
ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(Kx, Ky, analytical_F, cmap='plasma', alpha=0.8)
ax2.set_title('Analytical Fourier Transform')
ax2.set_xlabel('Kx')
ax2.set_ylabel('Ky')
ax2.set_zlabel('|F(Kx, Ky)|')

plt.show()
