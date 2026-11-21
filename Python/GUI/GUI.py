import tkinter as tk     # from tkinter import *

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

top1= tk.LabelFrame(pw1,text="即時影像", font=("Microsoft JhengHei", 14, "bold"),bg="white", fg='steelblue', bd=2, padx=5,pady=5)
top2= tk.LabelFrame(pw2,text="控制面板", font=("Microsoft JhengHei", 14, "bold"),bg="white", fg='steelblue', bd=2, padx=5,pady=5)
top3= tk.LabelFrame(pw3,text="模組選單", font=("Microsoft JhengHei", 14, "bold"),bg="white", fg='steelblue', bd=2, padx=5,pady=5)
top4= tk.LabelFrame(pw4,text="數據資料", font=("Microsoft JhengHei", 14, "bold"),bg="white", fg='steelblue', bd=2, padx=5,pady=5)
top5= tk.LabelFrame(pw5,text="擷取原圖", font=("Microsoft JhengHei", 14, "bold"),bg="white", fg='steelblue', bd=2, padx=5,pady=5)
top6= tk.LabelFrame(pw6,text="實驗結果", font=("Microsoft JhengHei", 14, "bold"), bg="white", fg='steelblue', bd=2, padx=5,pady=5)
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

window.mainloop()

# import tkinter as tk

# window = tk.Tk()

# # 1. 初始大小設定（這裡設定開視窗自動最大化，你也可以維持指定尺寸）
# window.state('zoomed') 
# window.title('Dobot UI')
# window.configure(bg="cornflowerblue", bd=5)

# # ==========================================
# # 2. 核心：設定大視窗的「網格等比例權重」
# # ==========================================
# # 我們把視窗橫向切成 3 欄 (欄 0, 欄 1 比例為 725，欄 2 比例為 460)
# window.columnconfigure(0, weight=725)
# window.columnconfigure(1, weight=725)
# window.columnconfigure(2, weight=460)

# # 我們把視窗縱向切成 3 列 (列 0 比例 500, 列 1 比例 100, 列 2 比例 300)
# # 這樣安排是為了配合你右邊三格 (300, 300, 300) 與左邊兩格 (500, 400) 的交錯高度
# window.rowconfigure(0, weight=300)
# window.rowconfigure(1, weight=200)
# window.rowconfigure(2, weight=400)

# # ==========================================
# # 3. 建立 7 個白色 LabelFrame 面板
# # ==========================================
# # 注意：這裡不需要再另外宣告 PanedWindow，直接把主視窗當作容器，程式碼更乾淨
# top1 = tk.LabelFrame(window, text="即時影像", font=("Microsoft JhengHei", 14, "bold"), bg="white", fg='steelblue', bd=2, padx=5, pady=5)
# top2 = tk.LabelFrame(window, text="控制面板", font=("Microsoft JhengHei", 14, "bold"), bg="white", fg='steelblue', bd=2, padx=5, pady=5)
# top3 = tk.LabelFrame(window, text="模組選單", font=("Microsoft JhengHei", 14, "bold"), bg="white", fg='steelblue', bd=2, padx=5, pady=5)
# top4 = tk.LabelFrame(window, text="數據資料", font=("Microsoft JhengHei", 14, "bold"), bg="white", fg='steelblue', bd=2, padx=5, pady=5)
# top5 = tk.LabelFrame(window, text="擷取原圖", font=("Microsoft JhengHei", 14, "bold"), bg="white", fg='steelblue', bd=2, padx=5, pady=5)
# top6 = tk.LabelFrame(window, text="實驗結果", font=("Microsoft JhengHei", 14, "bold"), bg="white", fg='steelblue', bd=2, padx=5, pady=5)
# top7 = tk.LabelFrame(window, text="入庫資訊", font=("Microsoft JhengHei", 14, "bold"), bg="white", fg='steelblue', bd=2, padx=5, pady=5)

# # ==========================================
# # 4. 用 grid() 把面板填入網格，並用 sticky="nsew" 讓它填滿
# # ==========================================
# # sticky="nsew" 代表上下左右自動拉伸填滿格子

# # 左邊第一欄（欄 0）
# top1.grid(row=0, column=0, rowspan=2, sticky="nsew", padx=2, pady=2) # 佔用列0~1 (高500比例)
# top2.grid(row=2, column=0, sticky="nsew", padx=2, pady=2)            # 佔用列2   (高400比例)

# # 中間第二欄（欄 1）
# top3.grid(row=0, column=1, rowspan=2, sticky="nsew", padx=2, pady=2) # 佔用列0~1 (高500比例)
# top4.grid(row=2, column=1, sticky="nsew", padx=2, pady=2)            # 佔用列2   (高400比例)

# # 右邊第三欄（欄 2）：三格高度均分
# top5.grid(row=0, column=2, sticky="nsew", padx=2, pady=2)            # 佔用列0 (高300比例)
# top6.grid(row=1, column=2, sticky="nsew", padx=2, pady=2)            # 佔用列1 (高300比例)
# top7.grid(row=2, column=2, sticky="nsew", padx=2, pady=2)            # 佔用列2 (高300比例)

# window.mainloop()