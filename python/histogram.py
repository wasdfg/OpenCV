import cv2 as cv
import numpy as np

#히스토그램이란 픽셀의 개수를 막대그래프 형식으로 표현
#grayscale의 경우 256개 0~255를 표현한 그래프를 사용
#히스토그램 스트레칭이란 최소값을 0으로 하고 최대값을 255로 해서 늘리는것
# dist(x,y) = (src(x,y) - min) * 255 / (max-min)

def calcGrayHist(img): #히스토그램을 배열로 전달
    channels = [0]
    histSize = [256]
    histRange = [0,256]
    
    hist = cv.calcHist([img],channels,None,histSize,histRange)
    
    return hist

def getGrayHistImage(hist):
    _,histmax,_,_ = cv.minMaxLoc(hist) #히스토그램의 최대값
    
    imghist = np.ones((100,256),np.uint8)*255
    
    for x in range(imghist.shape[1]):
        pt1 = (x,100) #최대값은 100을 기준
        pt2 = (x,100 - int(int(hist[x,0])*100/histmax))
        cv.line(imghist,pt1,pt2,0)
    
    return imghist

def histogram_stretching(): #히스토그램의 분포를 골고루 분포시켜주는 것 넓게 펴주는 역할
    src = cv.imread('hawkes.bmp',cv.IMREAD_GRAYSCALE)
    
    if src is None:
        print("no image")
        return
    
    gmin,gmax,_,_ = cv.minMaxLoc(src)
    
    dst = cv.convertScaleAbs(src,alpha=255.0/(gmax-gmin),beta=-gmin*255.0/(gmax-gmin))
    
    cv.imshow("src",src)
    cv.imshow("srcHist",getGrayHistImage(calcGrayHist(src)))
    cv.imshow("dst",dst)
    cv.waitKey()

img = cv.imread("lenna.bmp",cv.IMREAD_GRAYSCALE)

if img is None:
    print("img load failed")
    exit()
alpha = 1.0
img1 = cv.convertScaleAbs(img,alpha=alpha+1,beta=-128*alpha) #기울기를 구하는 함수

hist = getGrayHistImage(img1)

cv.imshow("img",img1)
cv.imshow("hist",hist)
cv.waitKey()

histogram_stretching()

src = cv.imread("hawkes.bmp",cv.IMREAD_GRAYSCALE)

if src is None:
    print("no image")
    exit()

dst1 = cv.equalizeHist(src) #히스토그램 평활화
                           #히스토그램 분포가 한쪽으로 치우쳐있는 부분을 넓게 펴주는 방식

cv.imshow("src",src)
cv.imshow("srcHist",getGrayHistImage(calcGrayHist(src)))
cv.imshow("dst1",dst1)
cv.imshow("dstHist",getGrayHistImage(calcGrayHist(dst1)))
cv.waitKey()