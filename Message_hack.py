
import pyautogui as pygui
import time


time.sleep(4)
count=0
while count<100:
    pygui.typewrite(("Hello I am Message box")+str(count))
    pygui.press("enter")
    count=count+1

