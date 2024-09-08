import cv2 as cv

src = cv.imread("lenna.bmp",cv.IMREAD_GRAYSCALE)

if src is None:
    print("img load failed")
    exit()
    
s = 2.0

dst = cv.multiply(src,s)    #명암을 기울기 2로 조정 2배를 하고 포화연산을 적용
                            #보통은 기울기를 상수값으로 사용하지 않는다
                        
                         
alpha = 1.0

img = cv.convertScaleAbs(src,alpha=1+alpha,beta=-128*alpha) #항상 (128,128)을 지나지만 기울기가 a에 변경되는 방정식을 사용한다
                                                            # dst(x,y) = src(x,y)+(src(x,y)-128)*a
                                                            #a값이 0보다 크면 명암비가 증가 되고 -1 <= a <= 0이면 명암비가 감소

a = cv.mean(img)
print(a)

cv.imshow("src",src)
cv.imshow("dst",dst)
cv.imshow("img",img)
cv.waitKey()