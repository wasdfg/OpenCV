import cv2 as cv

tm = cv.TickMeter() #시간 측정용

def mask_setTo():
    src = cv.imread("lenna.bmp")
    mask = cv.imread("mask_smile.bmp",cv.IMREAD_GRAYSCALE)
    
    if src is None or mask is None:
        print("image load failed")
        return
    
    src[mask > 0] = (0,255,255) #검은 색이 아닌 mask를 노란색으로 변경해서 src에 넣음
    
    cv.imshow("src",src)
    cv.imshow("mask",mask)
    cv.waitKey()
    
mask_setTo()



def mask_copyTo():
    src = cv.imread("airplane.bmp")
    mask = cv.imread("mask_plane.bmp",cv.IMREAD_GRAYSCALE)
    dst = cv.imread("field.bmp")
    
    if src is None or mask is None or dst is None:
        print("image load failed")
        return
    
    dst[mask > 0] = src[mask > 0] #mask_plane의 흰 부분을 누끼를 따서 field에 넣는다.
    
    cv.imshow("src",src)
    cv.imshow("mask",mask)
    cv.imshow("dst",dst)
    cv.waitKey()

tm.start()
mask_copyTo()

tm.stop()
print(tm.getTimeMilli()/1000) #단위는 ms