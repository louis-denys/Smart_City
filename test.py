import ctypes
 
usr32 = ctypes.windll.user32
print("width =", usr32.GetSystemMetrics(0))
print("height =", usr32.GetSystemMetrics(1))
