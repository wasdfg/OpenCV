import numpy as np
import cv2 as cv

def saturated(value):
    if value > 255:
        value = 255
    elif value < 0:
        value = 0
    
    return value

def on_level_change(pos):
    img[:] = saturated(pos*16)
    cv.imshow("img",img)
    
img = np.zeros((480,720),np.uint8)

cv.namedWindow("img")
cv.createTrackbar('level','img',0,16,on_level_change) #img라는 윈도우 창에 트랙바를 만드는데 16등분짜리로 만듦
cv.imshow("img",img)
cv.waitKey()