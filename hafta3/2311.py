import pyautogui #pip install pyautogui
import subprocess
import time
print(pyautogui.size())
x,y=pyautogui.size()
# pyautogui.moveTo(100,100,3)
# pyautogui.moveRel(-500,300,1)
# pyautogui.typewrite("elginkan")
# pyautogui.screenshot("sc.jpg")
subprocess.Popen(["mspaint.exe"])
pyautogui.moveTo(x/2,y/2)
time.sleep(2)
distance=300
while distance>0:
    pyautogui.dragRel(distance,0,1,button="left")
    distance=distance-20
    pyautogui.dragRel(0,distance,0,1,button="left")
    pyautogui.dragRel(- distance,0,1,button="left")
    distance=distance-20
    pyautogui.dragRel(0,distance,0,1,button="left")
    time.sleep(3)



