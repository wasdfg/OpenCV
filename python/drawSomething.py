import numpy as np
import cv2 as cv

img = np.full((480,720,3),255,np.uint8) #400x400의 색깔 배열을 생성 색은 흰색

cv.line(img,(50,50),(200,50),(0,0,255),10) #(50,50) 에서 (200,50)까지 굵기가 10인 빨간 선을 그림
cv.line(img,(250,50),(350,100),(0,0,255),1,cv.LINE_4)
cv.line(img,(250,70),(350,120),(255,0,255),1,cv.LINE_8)
cv.line(img,(250,90),(350,140),(255,0,255),1,cv.LINE_AA)

cv.rectangle(img,(10,10),(80,80),(0,0,255),-1) #좌측 위 점 우측 아래 점 2개를 입력받아 사각형을 그린다 , 값이 음수면 꽉찬 사각형 양수면 굵기가 있는 빈 사각형
cv.circle(img,(300,120),60,(255,0,0),3,cv.LINE_AA) #중심점을 값으로 받는 원을 생성 반지름이 60

cv.putText(img,"12345",(100,400),cv.FONT_HERSHEY_PLAIN,4,(0,0,0)) #12345라는 글씨를 작성

text = "hello opencv"
fontFace = cv.FONT_HERSHEY_TRIPLEX
fontScale = 2.0
thickness = 1
sizeText,_ = cv.getTextSize(text,fontFace,fontScale,thickness) #text의 배열 값을 가져온다

org = ((img.shape[1] - sizeText[0]) // 2,(img.shape[0]+sizeText[1])//2) #
cv.putText(img,text,org,fontFace,fontScale,(255,0,0),thickness)
cv.rectangle(img,org,(org[0]+sizeText[0],org[1]-sizeText[1]),(0,255,0),1)

cv.imshow("img",img)
cv.waitKey() 