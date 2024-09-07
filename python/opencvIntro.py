import cv2 as cv
import sys

img = cv.imread("lenna.bmp",flags=1) #경로에 있는 bmp 이미지 파일을 읽어온다 flag값이 0이면 흑백 1이면 컬러 기본값은 rgb컬러 값
img1 = cv.imread("lenna.bmp",cv.IMREAD_GRAYSCALE) #cv.색지정 으로도 설정 가능

if img is None:
    print('no images')
    sys.exit()

print(img.shape) #이미지의 해상도 세번째 값은 컬러인지 흑백인지 표시
print(type(img)) #img의 이루어진 값

cv.namedWindow('test')  #이미지를 여는 창 이름
cv.imshow('test',img)  #여는 이미지의 이름 및 여는 값
cv.moveWindow('test',0,0) #왼쪽 상단의 값을 기준으로 위치를 조정
cv.resizeWindow('test',512,512) #결과창의 크기를 조절 (이름,가로,세로)
cv.waitKey()    #키보드 값을 입력받기 전까지 유지
cv.destroyAllWindows()  #입력받으면 종료