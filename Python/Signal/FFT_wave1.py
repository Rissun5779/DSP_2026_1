import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

fs = 8*1000
duration = 1
N = int(fs*duration)

t = np.arange(N) / fs

def generate_signal(A, f, x):
    return x+A*np.sin(2*np.pi*f*t)

x1 = np.zeros(N)
x1 = generate_signal(1,1000, x1)

x2 = np.zeros(N)
x2 = generate_signal(0.5,500, x2)
x2 = generate_signal(0.2,200, x2)
x2 = generate_signal(0.8,800, x2)
x2 = generate_signal(1.0,1000, x2)

x_mix = x2 / np.max(np.abs(x2))

plt.figure()
plt.subplot(221)
plt.plot(t[:200], x1[:200])
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("1000 Hz Sine Wave")
plt.grid()

X = np.fft.fft(x1)
freq = np.fft.fftfreq(N, d=1/fs)
mag  = np.abs(X)/N

half = N//2
freq_pos = freq[:half]
mag_pos  = mag[:half]*2

plt.subplot(222)
plt.plot(freq_pos, mag_pos)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.title("Spectrum of Mixed Signal")
plt.grid()
plt.xlim(0, 1500)

plt.subplot(223)
plt.plot(t[:200], x_mix[:200])
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Mixed Signal: 200 + 500 + 800 + 1000 Hz")
plt.grid()

X = np.fft.fft(x2)
freq = np.fft.fftfreq(N, d=1/fs)
mag  = np.abs(X)/N

half = N//2
freq_pos = freq[:half]
mag_pos  = mag[:half]*2

plt.subplot(224)
plt.plot(freq_pos, mag_pos)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.title("Spectrum of Mixed Signal")
plt.tight_layout()
plt.grid()
plt.xlim(0, 1500)
plt.show()