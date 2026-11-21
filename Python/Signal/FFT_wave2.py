import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

fs = 44.1*1000
duration = 1
N = int(fs*duration)

t = np.arange(N) / fs

def generate_signal(A, f, x):
    return x+A*np.sin(2*np.pi*f*t)

f  = 1000
x_sine = np.zeros(N)
x_sine = generate_signal(1,1000, x_sine)

x_square = signal.square(2*np.pi*f*t)
x_triangle = signal.sawtooth(2*np.pi*f*t, width=0.5)

# x_mix = x2 / np.max(np.abs(x2))
show_sample = int(0.005*fs)

plt.figure()
plt.subplot(321)
plt.plot(t[:show_sample], x_sine[:show_sample])
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Sine Wave")
plt.grid()

X = np.fft.fft(x_sine)
freq = np.fft.fftfreq(N, d=1/fs)
mag  = np.abs(X)/N

half = N//4
freq_pos = freq[:half]
mag_pos  = mag[:half]*2

plt.subplot(322)
plt.plot(freq_pos, mag_pos)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.title("Spectrum of Sine Signal")
plt.grid()

plt.subplot(323)
plt.plot(t[:show_sample], x_square[:show_sample])
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("square Wave")
plt.grid()

X = np.fft.fft(x_square)
freq = np.fft.fftfreq(N, d=1/fs)
mag  = np.abs(X)/N

half = N//4
freq_pos = freq[:half]
mag_pos  = mag[:half]*2

plt.subplot(324)
plt.plot(freq_pos, mag_pos)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.title("Spectrum of Square Signal")
plt.grid()

plt.subplot(325)
plt.plot(t[:show_sample], x_triangle[:show_sample])
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("triangle Wave")
plt.grid()

X = np.fft.fft(x_triangle)
freq = np.fft.fftfreq(N, d=1/fs)
mag  = np.abs(X)/N

half = N//4
freq_pos = freq[:half]
mag_pos  = mag[:half]*2

plt.subplot(326)
plt.plot(freq_pos, mag_pos)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.title("Spectrum of triangle Signal")
plt.grid()

plt.tight_layout()
plt.show()