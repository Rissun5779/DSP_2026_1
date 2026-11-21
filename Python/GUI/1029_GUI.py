import serial
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']  
plt.rcParams['axes.unicode_minus'] = False

PORT = "COM4"
BAUD = 9600

index_array  = []
sensor_array = [] 

ser = serial.Serial(PORT, BAUD, timeout=2)
print("Waiting for ESP32 data...")

while True:
    line = ser.readline().decode("utf-8", errors="ignore").strip()

    if line == "START":
        print("Start receiving data...")
        break

while True:
    line = ser.readline().decode("utf-8", errors="ignore").strip()

    if not line:
        continue

    if line == "END":
        print("Receive END")
        break

    try:
        parts = line.split(",")

        index = int(parts[0])
        value = float(parts[1])

        index_array.append(index)
        sensor_array.append(value)

        print("index =", index, "value =", value)

    except Exception as e:
        print("Invalid data:", line)
        print("error:", e)

ser.close()
print("Total samples received:", len(sensor_array))
print("First 10 data:", sensor_array[:10])
# while True:
#   line = ser
# 1005
sample_interval = 0.01
time_array = [i*sample_interval for i in index_array]

plt.figure()
plt.plot(time_array, sensor_array)
plt.xlabel("秒(s)")
plt.ylabel("感測值")
plt.title("ESP32 感測資料圖形 GUI")
plt.grid(True)
plt.show()
