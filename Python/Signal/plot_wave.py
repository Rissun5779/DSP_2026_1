#%%
import numpy as np
import scipy.signal as signal 
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']  
plt.rcParams['axes.unicode_minus'] = False

fs        = 1000
duration  = 0.35
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
    signal.square(2*np.pi*f*t, duty=0.2),
    signal.chirp(t, f0=5, f1=50, t1=1)
]
f1= 20
f2= 200
x = np.cos(2*np.pi*f1*t)*np.cos(2*np.pi*f2*t)
evelop1 = np.cos(2*np.pi*f1*t)
evelop2 = -np.cos(2*np.pi*f1*t)
x = x+evelop1+evelop2
names = ["正弦波", "方波", "三角波",
         "鋸齒波", "PWM波", "Chirp"]

# %%
plt.figure(figsize=(15, 10))
for k in range(1):
    plt.subplot(3, 2, k+1)
    plt.plot(t, x)
    plt.title(names[k])
    plt.xlabel("時間 (s)")
    plt.ylabel("振幅")
    plt.grid()



plt.grid(True)
plt.tight_layout()
plt.show()
# %%
