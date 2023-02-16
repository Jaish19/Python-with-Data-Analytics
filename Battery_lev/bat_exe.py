import psutil
import time
import ctypes  
while True:
	battery = psutil.sensors_battery()
	if battery.power_plugged:
		if int(battery.percent)>=100:
			ctypes.windll.user32.MessageBoxW(0, "Please Unplug the Charger", "Battery is full", 0)
			time.sleep(10)
