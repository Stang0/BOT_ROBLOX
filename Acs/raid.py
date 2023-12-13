from pyautogui import *
import cv2 as cv
import numpy as np
import pyautogui
import random
import time as timepy
import pydirectinput
from time import time
from windowcapture import WindowCapture
from vision import find
from multiprocessing import Process
import os


fream = cv.imread('./assets/fream.png',cv.IMREAD_UNCHANGED)
house = cv.imread('./assets/House.png',cv.IMREAD_UNCHANGED)


start = './assets/Start.png'
Start = pyautogui.locateOnScreen(start,confidence=0.7, grayscale=True)



Lraid = './assets/LogoRaid.jpg'
LRaid = pyautogui.locateOnScreen(Lraid)

raid = './assets/Ninga.png'
Raid = pyautogui.locateOnScreen(raid)

MAP = './assets/Map.png'
Maping = pyautogui.locateOnScreen(MAP)

tel = './assets/Tel.png'
Tel = pyautogui.locateOnScreen(tel)



def clickMap():
    pyautogui.click(1200,1080)
    timepy.sleep(2)
    pyautogui.doubleClick(Maping)
    timepy.sleep(1)

def Goraid():   
    pyautogui.click(1200,1080)
    timepy.sleep(1)
    pyautogui.doubleClick(869,866)    
    pyautogui.click(1200,1080)
    timepy.sleep(1)
    pyautogui.doubleClick(902,639)
    timepy.sleep(2)
    pydirectinput.keyDown('left')
    timepy.sleep(0.5)
    pydirectinput.keyUp('left') 
    pydirectinput.keyDown('w')
    timepy.sleep(5)
    pydirectinput.keyUp('w') 
    timepy.sleep(1)
    pydirectinput.keyDown('right')
    timepy.sleep(0.87)
    pydirectinput.keyUp('right') 
    timepy.sleep(2)
    pydirectinput.keyDown('w')
    timepy.sleep(1.2)
    pydirectinput.keyUp('w')
    timepy.sleep(1)
    pydirectinput.keyDown('right')
    timepy.sleep(0.3)
    pydirectinput.keyUp('right') 
    timepy.sleep(1)
    pydirectinput.keyDown('w')
    timepy.sleep(0.5)
    pydirectinput.keyUp('w')
    timepy.sleep(5)

    
   
    pyautogui.scroll(-3000, x=813, y=428)
    timepy.sleep(1)
    pyautogui.scroll(-3000, x=813, y=428)
    timepy.sleep(1)
    pyautogui.scroll(-3000, x=813, y=428)
    timepy.sleep(1)
    pyautogui.scroll(-3000, x=813, y=428)

    pyautogui.click(1200,1080)
    timepy.sleep(1)
    pyautogui.doubleClick(711,709)
    timepy.sleep(1)
    pyautogui.click(1200,1080)
    timepy.sleep(1)
    pyautogui.doubleClick(675,707)
    timepy.sleep(1)
    pyautogui.click(1200,1080)
    timepy.sleep(1)
    pyautogui.doubleClick(1285,798)


def checkRaid():
    print("checkRaid",LRaid)
    if LRaid == None:
        clickMap()
        Goraid()

def Battle():
    pyautogui.click(1200,1080)
    timepy.sleep(1)
    pyautogui.doubleClick(826,465)
    pyautogui.scroll(-3000, x=813, y=428)
    timepy.sleep(0.5)
    pyautogui.scroll(-3000, x=813, y=428)
    timepy.sleep(0.50)
    pyautogui.scroll(-3000, x=813, y=428)
    timepy.sleep(0.50)
    pyautogui.scroll(-3000, x=813, y=428)
    timepy.sleep(0.50)
    pyautogui.scroll(-3000, x=813, y=428)
    timepy.sleep(0.50)
    pyautogui.scroll(-3000, x=813, y=428)
    timepy.sleep(0.50)
    pyautogui.scroll(-3000, x=813, y=428)
    timepy.sleep(0.50)
    pyautogui.scroll(-3000, x=813, y=428)

    os.chdir(os.path.dirname(os.path.abspath(__file__)))


    wincap = WindowCapture('Roblox')

    loop_time = time()

    while(True):

       
        screenshot = wincap.get_screenshot()

        result , max_val = find('F.jpg', screenshot, 0.5, 'rectangles')
        
        
     
        loop_time = time()

       

        
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break
        
        if max_val >= 0.9:
                pyautogui.click(1200,1080)
                pyautogui.doubleClick(63,681)
                pyautogui.click(1200,1080)
                pyautogui.doubleClick(1392,607)
                pyautogui.click(1200,1080)
                pyautogui.doubleClick(1392,607)
                pyautogui.click(1200,1080)
                pyautogui.doubleClick(1430,264)
                pyautogui.click(1200,1080)
                timepy.sleep(1)
                pyautogui.doubleClick(885,950)
                pydirectinput.keyDown('left')
                timepy.sleep(0.08)
                pydirectinput.keyUp('left')
                pydirectinput.keyDown('w')
                timepy.sleep(2)
                pydirectinput.keyUp('w')
                timepy.sleep(10)
                pydirectinput.keyDown('left')
                timepy.sleep(0.45)
                pydirectinput.keyUp('left')
                pydirectinput.keyDown('w')
                timepy.sleep(1.5)
                pydirectinput.keyUp('w')
                timepy.sleep(6)
                pydirectinput.keyDown('w')
                timepy.sleep(2.5)
                pydirectinput.keyUp('w')
                timepy.sleep(5)
                pydirectinput.keyDown('right')
                timepy.sleep(0.7)
                pydirectinput.keyUp('right')
                pydirectinput.keyDown('w')
                timepy.sleep(0.8)
                pydirectinput.keyUp('w')
                timepy.sleep(8)
                pydirectinput.keyDown('left')
                timepy.sleep(0.7)
                pydirectinput.keyUp('left')
                pydirectinput.keyDown('w')
                timepy.sleep(2.6)
                pydirectinput.keyUp('w')
                timepy.sleep(6)
                pydirectinput.keyDown('left')
                timepy.sleep(0.65)
                pydirectinput.keyUp('left')
                pydirectinput.keyDown('w')
                timepy.sleep(3)
                pydirectinput.keyUp('w')
                pydirectinput.keyDown('right')
                timepy.sleep(1.4)
                pydirectinput.keyUp('right')
                timepy.sleep(8)
                pydirectinput.keyDown('w')
                timepy.sleep(1.3)
                pydirectinput.keyUp('w')
                pydirectinput.keyDown('left')
                timepy.sleep(0.65)
                pydirectinput.keyUp('left')
                timepy.sleep(1)
                pydirectinput.keyDown('w')
                timepy.sleep(2)
                pydirectinput.keyUp('w')
                timepy.sleep(7)
                pydirectinput.keyDown('right')
                timepy.sleep(0.7)
                pydirectinput.keyUp('right')
                pydirectinput.keyDown('w')
                timepy.sleep(0.5)
                pydirectinput.keyUp('w')
                pydirectinput.keyDown('left')
                timepy.sleep(0.7)
                pydirectinput.keyUp('left')
                pydirectinput.keyDown('w')
                timepy.sleep(4)
                pydirectinput.keyUp('w')
                timepy.sleep(10)
                pydirectinput.keyDown('right')
                timepy.sleep(0.7)
                pydirectinput.keyUp('right')
                pydirectinput.keyDown('w')
                timepy.sleep(2)
                pydirectinput.keyUp('w')
                timepy.sleep(5)
                pydirectinput.keyDown('left')
                timepy.sleep(0.7)
                pydirectinput.keyUp('left')
                pydirectinput.keyDown('w')
                timepy.sleep(0.5)
                pydirectinput.keyUp('w')
                break
        else:
                pydirectinput.press('esc')
                pydirectinput.press('r')
                pydirectinput.press('enter')
                timepy.sleep(7)
                continue
       
        
    print('Done.')
    

   

if Maping:
    # clickMap()
    # Goraid()
    Battle()
   