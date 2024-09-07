import cv2 as cv

cam = cv.VideoCapture(0) #웹캠코더를 켠다 #동영상 파일이라면 경로를 입력

if not cam.isOpened: #안열리면
    print("camera not opened")
    exit()

fps = cam.get(cv.CAP_PROP_FPS)
print('fps :',fps) #현재 프레임
delay = round(1000/fps) #30프레임일 경우 나오는 delay값
print(delay)
w = int(cam.get(cv.CAP_PROP_FRAME_WIDTH)) #비디오 너비
h = int(cam.get(cv.CAP_PROP_FRAME_HEIGHT)) #비디오 높이
fourcc = cv.VideoWriter_fourcc(*'DIVX')
print('frame width :',int(cam.get(cv.CAP_PROP_FRAME_WIDTH)))
print('frame height :',int(cam.get(cv.CAP_PROP_FRAME_HEIGHT)))
print('frame count: ',int(cam.get(cv.CAP_PROP_FRAME_COUNT)))

output = cv.VideoWriter('output.avi',fourcc,fps,(w,h)) #저장 형식 지정
output1 = cv.VideoWriter('output1.avi',fourcc,fps,(w,h))

while True:
    ret,frame = cam.read() #캠 값을 읽어온다 frame이 보이는 값
    
    if not ret:
        break

    inversed = ~frame #색반전
    
    cv.imshow("frame",frame) 
    cv.imshow("inversed",inversed)
    output.write(frame) #녹화
    output1.write(inversed) #반전 녹화
    
    if(cv.waitKey(10) == 27): #deply는 10ms esc를 입력받으면 종료
        break
cv.destroyAllWindows()    