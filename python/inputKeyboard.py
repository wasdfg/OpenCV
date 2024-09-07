import numpy as np
import cv2 as cv

img = cv.imread("dog.bmp")

if img is None:
    print("no img")
    exit()

cv.namedWindow("img")
cv.imshow("img",img)

while True:
    keycode = cv.waitKey() #키를 입력받음
    
    if keycode == ord('i') or keycode == ord('I'): #받은 키가 대소문자 i일때 ord는 유니코드 반환
        img = ~img #색반전
        cv.imshow("img",img)
    elif keycode == 27 or keycode == ord('q') or keycode == ord('Q'):
        break
cv.destroyAllWindows()