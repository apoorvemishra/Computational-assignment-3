import requests
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal


# Fetch data from the URL
url = "http://theory.tifr.res.in/~kulkarni/noise.txt"
response = requests.get(url)
data = response.text

# Process the data
lines = data.strip().split('\n')
noise = []
for line in lines:
    noise.append(float(line))


# Plotting the noise data
plt.figure(figsize=(12, 6))
# Original data plot
plt.subplot(2, 2, 1)
plt.plot(noise, color='blue')
plt.title('Noise Data')
plt.xlabel('Time')
plt.ylabel('Noise')
plt.grid(True)

# Compute FFT
fft_vals = np.fft.fft(noise, norm = 'ortho')
freqs = np.fft.fftfreq(len(noise), d=1)
plt.subplot(2, 2, 2)
plt.plot(freqs, np.abs(fft_vals), color='green')
plt.title('FFT of Noise Data')
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.grid(True)


f, P = signal.periodogram(noise)

plt.subplot(2, 2, 3)
plt.plot(f, P, color='red')
plt.title('Periodogram')
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.grid(True)



plt.subplot(2, 2, 4)
plt.hist(P, 10)
plt.title('Bined power spectrum')
plt.xlabel('Bin')
plt.ylabel('Power')
plt.grid(True)



plt.tight_layout()
plt.show()


