import psutil
import time
import ctypes

shown=False

while True:
    b=psutil.sensors_battery()
    if b and b.percent==100 and b.power_plugged and not shown:
        ctypes.windll.user32.MessageBoxW(0, "Disconnect the charger", "Battery Full", 0x40 | 0x1)
        shown=True
    if b.percent<100:
        shown=False
    time.sleep(60)
