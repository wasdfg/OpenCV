import cv2 as cv
import sys

img = cv.imread(r"./python/lenna.bmp") #경로에 있는 bmp 이미지 파일을 읽어온다

if img is None:
    print('no images')
    sys.exit()


cv.namedWindow('test')  #이미지를 여는 창 이름
cv.imshow('test',img)  #여는 이미지의 이름 및 여는 값
cv.waitKey()    #키보드 값을 입력받기 전까지 유지
cv.destroyAllWindows()  #입력받으면 종료