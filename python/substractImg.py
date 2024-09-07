import cv2 as cv

def func1():
    img1 = cv.imread("lenna.bmp",cv.IMREAD_GRAYSCALE)
    
    img2 = img1[200:400,200:400]
    img3 = img1[200:400,200:400].copy()

    img4 = 255-img2
    img2-=img2
    img2+=img4

    cv.imshow("img1",img1)
    cv.imshow("img2",img2) #얕은 복사로 인해 원본 그림이 변경 
    cv.imshow("img3",img3)
    cv.waitKey()

func1()