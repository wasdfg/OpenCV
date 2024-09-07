import numpy as np
import cv2 as cv

def func():
    img1 = cv.imread("cat.bmp")
    
    if img1 is None:
        print("no images")
    
    img2 = img1
    img3 = img1.copy()
    img1[:,:] = (255,255,0)  #B G R 값으로 선언 
    cv.imshow("img1",img1)
    cv.imshow("img2",img2)
    cv.imshow("img3",img3) #3는 copy로 했기때문에 변경 전 img1로 복사
    cv.waitKey()

func()