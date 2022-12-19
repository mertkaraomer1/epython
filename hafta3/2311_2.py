import pyautogui #pip install pyautogui
import subprocess
from PIL import ImageGrab,ImageOps
import time
import numpy as np
time.sleep(5)
def renkyogunluk():
    dinazor=(236, 392)
    box=(dinazor[0]+30,dinazor[1],dinazor[0]+120,dinazor[1]+2)
    img=ImageGrab.grab(box)
    grayimg=ImageOps.grayscale(img)
    a=np.array(grayimg.getcolors())
    print(a.sum())
    return a.sum()
def press_space():
    #pyautogui.keyUp("Down")
    pyautogui.keyDown("space")
    time.sleep(0.05)
    print("jump")
    time.sleep(0.10)
    pyautogui.keyUp("space")
    #pyautogui.keyDown("Down")
    
while True:
    #print(pyautogui.position())
    # time.sleep(1)
    if (renkyogunluk()!=430):
        press_space()
        time.sleep(0.1)











