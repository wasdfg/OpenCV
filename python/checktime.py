import cv2 as cv
import numpy as np

img = cv.imread("lenna.bmp")

if img is None:
    print("img load failed")
    exit()
 
dst = np.empty(img.shape,dtype=img.dtype)
dst1 = np.empty(img.shape,dtype=img.dtype)

tm = cv.TickMeter()
tm.start()
dst = ~img
tm.stop()
print(tm.getTimeMilli()/1000)

tm.start()
for y in range(img.shape[0]):
    for x in range(img.shape[1]):
        dst1[y,x] = 255 - img[y,x]
tm.stop()
print(tm.getTimeMilli()/1000)

cv.imshow("dst",dst)
cv.imshow("dst1",dst1)
cv.waitKey()