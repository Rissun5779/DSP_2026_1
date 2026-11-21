import numpy as np
import scipy.signal as signal 
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']  
plt.rcParams['axes.unicode_minus'] = False

fs        = 1000
duration  = 1
t         = np.linspace(0, duration, int(duration*fs), endpoint=False)
f         = 5

waves = [
    # np.sin(2*np.pi*f*t),
    # np.sin(2*np.pi*f*t+np.pi/2),
    # np.sin(2*np.pi*f*t-np.pi/2), 
    # signal.square(2*np.pi*f*t),
    # signal.sawtooth(2*np.pi*f*t, 0.5),
    # signal.sawtooth(2*np.pi*f*t),
    # signal.square(2*np.pi*f*t, duty=0.2),
    # signal.chirp(t, f0=5, f1=50, t1=duration)

    np.sin(2*np.pi*f*t),
    signal.square(2*np.pi*f*t),
    signal.sawtooth(2*np.pi*f*t, 0.5),
    signal.sawtooth(2*np.pi*f*t),
    signal.square(2*np.pi*f*t, duty=0.2)
]

names = ["Sine", "Square", "Triangle",
         "Sawtooth", "Pulse", "Chirp"]

# plt.figure(figsize=(12,8))
# for i in range(6):
#     plt.subplot(3, 2, i+1)
#     plt.plot(t, waves[i])
#     plt.title(names[i])
#     plt.xlabel("Time (s)")
#     plt.ylabel("Amplitude")
#     plt.grid(True)
plt.plot(t, waves[0])
#, t, waves[1], t, waves[2]
plt.title("正弦波")
plt.xlabel("時間 (s)")
plt.ylabel("振幅")
plt.grid(True)

plt.tight_layout()
plt.show()
