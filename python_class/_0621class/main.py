import os

os.system("python -m pip install --upgrade pip")
os.system("pip install colorama")
os.system("cls")

import time
import colorama

colorama.init()

sec = 1

while True:
    if 0 < sec < 6:
        print(colorama.Back.RED + " ", colorama.Back.RESET)
        print(sec)
        time.sleep(1)
        os.system("cls")
        sec += 1
    elif sec == 6:
        print("  ", colorama.Back.YELLOW + " ", colorama.Back.RESET)
        print(sec)
        time.sleep(1)
        os.system("cls")
        sec += 1
    else:
        print("     ", colorama.Back.GREEN + " ", colorama.Back.RESET)
        print(sec % 10)
        time.sleep(1)
        os.system("cls")
        sec +=1
        sec = sec % 10
