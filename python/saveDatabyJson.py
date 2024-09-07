import numpy as np
import cv2 as cv

filename = "mydata.json" #파일 형태 선언

def writeData():
    name = "Jane"
    age = 10
    pt1 = (100,200)
    scores = (80,90,50)
    mat1 = np.array([[1.0,1.5],[2.0,3.2]],dtype=np.float32) #저장할 내용
    
    fs = cv.FileStorage(filename,cv.FILE_STORAGE_WRITE) #파일을 쓰기 형식으로 열기
    
    if not fs.isOpened: #안열리면
        print("file open failed")
        return
    
    fs.write("name",name) #내용 쓰기
    fs.write("age",age)
    fs.write("point",pt1)
    fs.write("scores",scores)
    fs.write("data",mat1)
    
    fs.release() #파일저장
    
writeData()

def readData():
    fs = cv.FileStorage(filename, cv.FileStorage_READ) #파일을 읽어들임
    
    if not fs.isOpened():
        print("file open failed")
        return
    
    name = fs.getNode('name').string() #읽은 파일에 있는 변수를 읽어온다
    age = int(fs.getNode('age').real())
    pt1 = tuple(fs.getNode('point').mat().astype(np.int32).flatten().tolist())
    scores = tuple(fs.getNode('scores').mat().flatten().tolist())
    mat1 = fs.getNode('data').mat()
    
    fs.release()
    
    print('name:',name)
    print('age:',age)
    print('point:',pt1)
    print('scores:',scores)
    print('data:')
    print(mat1)

readData()