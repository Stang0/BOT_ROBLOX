from pyautogui import *
import pyautogui
import random
import pydirectinput
import time
#ปุ่ม reconnect 
reconnect = './assets/reconnect.png'
clickReconnect = pyautogui.locateOnScreen(reconnect)
#ปุ่ม reconnect ค้าง
holdReconnect = './assets/hold_reconnect.png'
#ปุ่ม leave ตอน reconnect ค้าง
leave = './assets/Leave.png'
pointLeave = pyautogui.locateOnScreen(leave)
#ปุ่ม play  สีเขียว
play = './assets/play.png'
pointPlay = pyautogui.locateOnScreen(play, grayscale=True)
#Leave error 279 
Error279 = './assets/Error279.png'
pointError279 = pyautogui.locateOnScreen(Error279)
#Retry สีขาว
retry = './assets/Retry.png'
pointretry = pyautogui.locateOnScreen(retry)
#reyry hold 
Holdretry  = './assets/HoleRetry.png'
pointHoldretry = pyautogui.locateOnScreen(Holdretry, grayscale=True)
#cancel
Cancel = './assets/cancel.png'
pointCancel = pyautogui.locateOnScreen(Cancel)

#Logo
logo = './assets/Logo.png'
pointLogo = pyautogui.locateOnScreen(logo,grayscale=True)
#skip 
skip = './assets/skip.png'
pointSkip = pyautogui.locateOnScreen(skip)
#stop
stop = './assets/stop.png'


time.sleep(2)
pydirectinput.keyDown('a')
time.sleep(1)
pydirectinput.keyUp('a') 
pydirectinput.keyDown('w')
time.sleep(2)
pydirectinput.keyUp('w') 
pydirectinput.keyDown('d')
time.sleep(1)
pydirectinput.keyUp('d')
pydirectinput.keyDown('w')
time.sleep(19.3)
pydirectinput.keyUp('w')
pydirectinput.keyDown('d')
time.sleep(1)
pydirectinput.keyUp('d')
pydirectinput.press('q')
time.sleep(2)
while True:
    if pyautogui.locateOnScreen(reconnect):
        print("found recoonnect")
        time.sleep(3)
        pyautogui.click(x=1050, y=1065)
        pyautogui.doubleClick(pyautogui.locateOnScreen(reconnect))
        time.sleep(1)
        pyautogui.doubleClick(pyautogui.locateOnScreen(reconnect))
        time.sleep(2)
        pyautogui.doubleClick(pyautogui.locateOnScreen(reconnect))
        print("here")
        time.sleep(90)
        pydirectinput.keyDown('a')
        time.sleep(1)
        pydirectinput.keyUp('a')
        pydirectinput.keyDown('w')
        time.sleep(2) 
        pydirectinput.keyUp('w')
        pydirectinput.keyDown('d')
        time.sleep(1)
        pydirectinput.keyUp('d')
        pydirectinput.keyDown('w')
        time.sleep(19.3)
        pydirectinput.keyUp('w')
        pydirectinput.keyDown('d')
        time.sleep(1)
        pydirectinput.keyUp('d')
        pydirectinput.press('q')
        print("continue")
        continue

    
    elif pyautogui.locateOnScreen(Error279):
        print("error 279")
        time.sleep(2)
        pyautogui.click(x=1050, y=1065)
        pyautogui.doubleClick(locateOnScreen(Error279))
        time.sleep(5)
        pyautogui.moveTo(x=242, y=650)
        time.sleep(2)
        pyautogui.click(x=1238, y=1057)
        pyautogui.doubleClick(x=242, y=650)
        pyautogui.click(x=1238, y=1057)
        pyautogui.doubleClick(x=242, y=650) 
        pyautogui.click(x=1238, y=1057)
        pyautogui.doubleClick(x=242, y=650) 
        pyautogui.click(x=1238, y=1057)
        pyautogui.doubleClick(x=242, y=650) 
        time.sleep(90)
        pydirectinput.keyDown('a')
        time.sleep(1)
        pydirectinput.keyUp('a')
        pydirectinput.keyDown('w')
        time.sleep(2) 
        pydirectinput.keyUp('w')
        pydirectinput.keyDown('d')
        time.sleep(1)
        pydirectinput.keyUp('d')
        pydirectinput.keyDown('w')
        time.sleep(19.3)
        pydirectinput.keyUp('w')
        pydirectinput.keyDown('d')
        time.sleep(1)
        pydirectinput.keyUp('d')
        pydirectinput.press('q')
        time.sleep(5)
        continue
            
   
    elif  pyautogui.locateOnScreen(holdReconnect):
        time.sleep(2)
        pyautogui.click(x=1050, y=1065)     
        pyautogui.doubleClick(pointLeave)
        print("leave")
        time.sleep(5)
        pyautogui.click(x=1050, y=1065)     
        pyautogui.doubleClick(x=242, y=650)
        pyautogui.click(x=1050, y=1065)     
        pyautogui.doubleClick(x=242, y=650)
        time.sleep(2)
        pyautogui.click(x=1050, y=1065)     
        pyautogui.doubleClick(x=242, y=650)
        time.sleep(5.5)
        
        if pyautogui.locateOnScreen(skip):
            time.sleep(90)
            pydirectinput.keyDown('a')
            time.sleep(1)
            pydirectinput.keyUp('a')
            pydirectinput.keyDown('w')
            time.sleep(2) 
            pydirectinput.keyUp('w')
            pydirectinput.keyDown('d')
            time.sleep(1)
            pydirectinput.keyUp('d')
            pydirectinput.keyDown('w')
            time.sleep(19.3)
            pydirectinput.keyUp('w')
            pydirectinput.keyDown('d')    
            time.sleep(1)
            pydirectinput.keyUp('d')
            pydirectinput.press('q')
            time.sleep(5)
            continue  
        while True:
            print("new loop")
            if pyautogui.locateOnScreen(retry):  
                pyautogui.click(x=1050, y=1065)  
                print(pyautogui.locateOnScreen(retry))   
                pyautogui.doubleClick(pyautogui.locateOnScreen(retry))
                time.sleep(0.3)
                pyautogui.click(pyautogui.locateOnScreen(retry))
                time.sleep(0.3)
                print("do1")
                time.sleep(5)
                continue

            elif pyautogui.locateOnScreen(Cancel):
                print("not")
                time.sleep(2)
                pyautogui.click(x=1050, y=1065)
                print(pyautogui.locateOnScreen(Cancel))
                pyautogui.doubleClick(pyautogui.locateOnScreen(Cancel))
                time.sleep(3)
                pyautogui.click(x=1050, y=1065)
                pyautogui.click(x=242, y=650)
                time.sleep(2)
                pyautogui.doubleClick(x=242, y=650)
                pyautogui.click(x=1050, y=1065)
                pyautogui.doubleClick(x=242, y=650)
                time.sleep(5)
                continue
                
                       
               
            else:
                if pyautogui.locateOnScreen(stop):
                    break
                print("play")
                time.sleep(90)
                pydirectinput.keyDown('a')
                time.sleep(1)
                pydirectinput.keyUp('a')
                pydirectinput.keyDown('w')
                time.sleep(2) 
                pydirectinput.keyUp('w')
                pydirectinput.keyDown('d')
                time.sleep(1)
                pydirectinput.keyUp('d')
                pydirectinput.keyDown('w')
                time.sleep(19.3)
                pydirectinput.keyUp('w')
                pydirectinput.keyDown('d')
                time.sleep(1)
                pydirectinput.keyUp('d')
                pydirectinput.press('q')
                time.sleep(5)
                print("do2")
                break   
    else:
        print("here else")
        pydirectinput.press('space')
        time.sleep(0.5)
        pydirectinput.press('q')
 





