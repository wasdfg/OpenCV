import numpy as np
import cv2 as cv

def over(num):
    if num > 255:
        num = 255
    elif num < 0:
        num =  0
    
    return num

img = cv.imread("rose.bmp",cv.IMREAD_GRAYSCALE) #기본적으로 uint8로 열림 0~255범위

if img is None:
    print("img load failed")
    exit()

img1 = cv.add(img,100) #포화연산이 구현되어있음

dst = np.empty(img.shape,dtype=img.dtype)

def update(pos):
    dst = cv.add(img,pos)
    cv.imshow("dst",dst)

for y in range(img.shape[0]): #포화연산이 적용되어 있지 않아 0~255값을 벗어날수 있음 직접 구현해줘야함
    for x in range(img.shape[1]):
        dst[y,x] = over(img[y,x]+100)

cv.namedWindow("dst")
cv.createTrackbar('Brightness',"dst",0,100,update)
update(0)
cv.waitKey()

