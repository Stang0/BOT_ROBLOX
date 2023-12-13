import cv2 as cv
import numpy as np 
import pyautogui
import time as time 
import os 



FPST12 = cv.imread('./assets/fream.png',cv.IMREAD_UNCHANGED)
FPS1 = cv.imread('./assets/F.png',cv.IMREAD_UNCHANGED)


result = cv.matchTemplate(FPST12, FPS1, cv.TM_CCOEFF_NORMED)

print(result)

threshold = 0.85
locations = np.where(result >= threshold)
locations = list(zip(*locations[::-1]))


print(locations)



# cv2.imshow('Result', result)
# cv2.waitKey()
# cv2.destroyAllWindows()

min_val, max_val,min_loc,max_loc = cv.minMaxLoc(result)

print(max_loc)
print(max_val)

w = FPS1.shape[1]
h = FPS1.shape[0]

total =cv.rectangle(FPST12, max_loc, (max_loc[0] + w, max_loc[1] + h) , (0,255,255),2)



cv.imshow('FPST1.2', FPST12)
cv.waitKey()
cv.destroyAllWindows()

