import pyautogui as pag
import random
import time
import ctypes
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
[w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]


while time :
    x = random.randint(0,w)
    y = random.randint(0,h)
    pag.moveTo(x,y,0.5)
    time.sleep(3)