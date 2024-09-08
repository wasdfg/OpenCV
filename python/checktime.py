import cv2 as cv
import numpy as np

img = cv.imread("lenna.bmp")

if img is None:
    print("img load failed")
    exit()
 
dst = np.empty(img.shape,dtype=img.dtype) #이미지 파일의 크기만큼의 빈 numpy를 생성
dst1 = np.empty(img.shape,dtype=img.dtype)

tm = cv.TickMeter()
tm.start()
dst = ~img #색반전
tm.stop()
print(tm.getTimeMilli()/1000)

tm.start()
for y in range(img.shape[0]): #색반전을 np를 사용하지 않고 for문으로 
    for x in range(img.shape[1]):
        dst1[y,x] = 255 - img[y,x]
tm.stop()
print(tm.getTimeMilli()/1000)

cv.imshow("dst",dst)
cv.imshow("dst1",dst1)
cv.waitKey()