import tkinter as tk     # from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import scipy.signal as signal 


plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']  
plt.rcParams['axes.unicode_minus'] = False

window = tk.Tk()
#window.geometry("1920x910")

screen_width  = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
print(f"Screen size: {screen_width}X{screen_height}")
window_width  = int(screen_width*0.7)
window_height = int(screen_height*0.7)
window.geometry(f"{window_width}x{window_height}")
window.title('DSP UI')
window.configure(bg="cornflowerblue", bd=5)

base_width, base_height = 1920, 910

def pw_place(widget, x, y, width, height):
    widget.place(x=(x/base_width)*window_width,
                 y=(y/base_height)*window_height,
                 width=(width/base_width)*window_width,
                 height=(height/base_height)*window_height)

pw1 = tk.PanedWindow()
pw2 = tk.PanedWindow()
pw3 = tk.PanedWindow()
pw4 = tk.PanedWindow()
pw5 = tk.PanedWindow()
pw6 = tk.PanedWindow()
pw7 = tk.PanedWindow()

top1= tk.LabelFrame(pw1,text="正弦波", font=("Microsoft JhengHei", 14, "bold"),bg="white", fg='steelblue', bd=2, padx=5,pady=5)
top2= tk.LabelFrame(pw2,text="方波", font=("Microsoft JhengHei", 14, "bold"),bg="white", fg='steelblue', bd=2, padx=5,pady=5)
top3= tk.LabelFrame(pw3,text="三角波", font=("Microsoft JhengHei", 14, "bold"),bg="white", fg='steelblue', bd=2, padx=5,pady=5)
top4= tk.LabelFrame(pw4,text="鋸齒波", font=("Microsoft JhengHei", 14, "bold"),bg="white", fg='steelblue', bd=2, padx=5,pady=5)
top5= tk.LabelFrame(pw5,text="PWM波", font=("Microsoft JhengHei", 14, "bold"),bg="white", fg='steelblue', bd=2, padx=5,pady=5)
top6= tk.LabelFrame(pw6,text="Chirp", font=("Microsoft JhengHei", 14, "bold"), bg="white", fg='steelblue', bd=2, padx=5,pady=5)
top7= tk.LabelFrame(pw7,text="入庫資訊", font=("Microsoft JhengHei", 14, "bold"), bg="white", fg='steelblue', bd=2, padx=5,pady=5)

for pw, top in [(pw1, top1), (pw2, top2), (pw3, top3), (pw4, top4), (pw5, top5), (pw6, top6), (pw7, top7)]:
    pw.add(top)

pw_place(pw1,x=0,y=0,width=725,height=500)
pw_place(pw2,x=0,y=500,width=725,height=400)
pw_place(pw3,x=725,y=0,width=725,height=500)
pw_place(pw4,x=725,y=500,width=725,height=400)
pw_place(pw5,x=1450,y=0,width=460,height=300)
pw_place(pw6,x=1450,y=300,width=460,height=300)
pw_place(pw7,x=1450,y=600,width=460,height=300)

fs = 1000
f  = 5
duaration = 1
t = np.linspace(0, duaration, fs, endpoint=False)

f1= 20
f2= 200

x = np.cos(2*np.pi*f1*t)*np.cos(2*np.pi*f2*t)
evelop1 = np.cos(2*np.pi*f1*t)
evelop2 = -np.cos(2*np.pi*f1*t)
#x = x+evelop1+evelop2

waves = [
    np.sin(2*np.pi*f*t),
    signal.square(2*np.pi*f*t),
    signal.sawtooth(2*np.pi*f*t, 0.5),
    signal.sawtooth(2*np.pi*f*t),
    signal.square(2*np.pi*f*t, duty=0.2),
    signal.chirp(t, f0=5, f1=50, t1=1),
]
names = ["正弦波", "方波", "三角波",
         "鋸齒波", "PWM波", "Chirp"]

frames = [pw1, pw2, pw3, pw4, pw5, pw6]

for k in range(6):
    fig = plt.figure(figsize=(6, 3), dpi=100)
    ax = fig.add_subplot(111)

    ax.plot(t, waves[k])
    ax.set_title(names[k])
    ax.set_xlabel("時間(s)")
    ax.set_ylabel("振幅")
    ax.grid()

    fig.tight_layout()
    fig.subplots_adjust(
        left=0.14,
        right=0.95,
        bottom=0.2,
        top=0.88
    )

    canvas = FigureCanvasTkAgg(fig, master=frames[k])
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

duration  = 0.25
t         = np.linspace(0, duration, int(duration*fs), endpoint=False)

fig = plt.figure(figsize=(6,3), dpi=100)
ax  = fig.add_subplot(111)
ax.plot(t, x[:len(t)])
ax.plot(t, evelop1[:len(t)],'--',color='b')
ax.plot(t, evelop2[:len(t)],'--',color='b')
ax.set_title("包若圖")
ax.set_xlabel("時間(s)")
ax.set_ylabel("振幅")
ax.grid()

fig.tight_layout()
fig.subplots_adjust(
    left=0.14,
    right=0.95,
    bottom=0.2,
    top=0.88
)

canvas = FigureCanvasTkAgg(fig, master=pw7)
canvas.draw()
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
window.mainloop()