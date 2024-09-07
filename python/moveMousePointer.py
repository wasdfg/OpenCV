import cv2 as cv
import numpy as np

def on_mouse(event,x,y,flags,param):
    global oldx,oldy
    
    if event == cv.EVENT_LBUTTONDOWN: #왼쪽 버튼 누르는 경우
        oldx,oldy = x,y
        print('EVENT_LBUTTONDOWN : (%d,%d)' % (x,y))
        
    elif event == cv.EVENT_LBUTTONUP: #왼쪽 버튼 떼는 경우
        oldx,oldy = x,y
        print('EVENT_LBUTTONUP : (%d,%d)' % (x,y))
        
    elif event == cv.EVENT_MOUSEMOVE: #마우스 움직이는 경우
        if flags & cv.EVENT_FLAG_LBUTTON: #왼쪽 버튼이 눌려있는 경우
            cv.line(img,(oldx,oldy),(x,y),(0,255,255),2)
            cv.imshow("img",img)
            oldx,oldy = x,y

img = np.full((480,720),255,np.uint8)

cv.namedWindow("img")
cv.setMouseCallback("img",on_mouse) #마우스 입력, 좌측은 이름, 우측은 함수
cv.imshow("img",img)
cv.waitKey()