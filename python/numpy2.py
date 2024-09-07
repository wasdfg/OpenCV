import numpy as np

arr = [[1,2,3],[4,5,6],[7,8,9]]

arr4 = [1,2,3,4,5]

arr2 = ['123',4.0,5]

arr1 = np.array(arr2,dtype='double') #dtype을 통해 자료형을 명시할 수 있다.
arr3 = np.array(arr4)
arr5 = np.array(arr)
print(type(arr))
print(arr)
print(type(arr1)) #np는 변수의 형식을 가장 높은 타입으로 일치시킨다. 문자와 숫자 혼합일 경우 문자로 취급 #np는 컴마가 사라진다 
#np로 바꿀 때 배열의 요소가 모두 같아야한다. 다차원이라면 차원 내부의 형식도 일치해야한다.

print(arr1)

print(arr3.ndim) #ndim은 몇 차원 배열인지
print(arr3.shape) #shape는 각 차원의 크기를 오름차순으로
print(len(arr3.shape)) #ndim이랑 같은말

print(arr3[:]) #전체 배열 출력
print(arr3[-1:-1]) #뒤는 항상 -1번째까지 계산 -1은 맨 뒤부터 계산하는 것이다. 맨 뒤부터 맨 뒤의 다음것까지 출력이지만 거꾸로 이므로 빈 값
print(arr3[:-2])

print(arr5) 
'''[[1 2 3] 
    [4 5 6] 
    [7 8 9]]'''
print(arr5.ndim) #2
print(arr5.shape) #(3,3)
print(len(arr5.shape)) #2
print(arr5.size) #9

nums = np.array([[1,4,2],[7,5,3]])

print(nums[1,1])
print(nums[1][0:2])
print(nums[:,-1:])
print(nums[:,:2])

#배열의 슬라이싱은 기존 배열 값이 변경되면 따라서 변경되므로 기존 배열을 쓰고 싶으면 copy()함수를 사용해라

print(np.identity(3)) #3x3행렬의 단위행렬을 출력
print(np.eye(3)) #3x3행렬의 단위 행렬을 출력
print(np.eye(3,k=1)) #k값이 양수라면 배열이 북동쪽으로 올라가고 올라가서 빈 부분은 0으로 출력 음수라면 남서쪽으로 내려간다.
print(np.eye(3,k=-2))

print(np.random.random((2,2))) #nxn형태의 배열로 랜덤 값을 넣음 0~1까지의 소수
print(np.linspace(0,1,num= 5,endpoint=True,retstep=True)) #0부터 1까지 5개로 이루어진 등차수열을 출력 endpoint 끝값 포함 retstep 등차값
print(np.arange(1,5,1)) #1부터 5미만까지 등차가 1인 배열을 출력 dtype으로 형 지정 가능 숫자 1개만 입력하면 0부터 n-1까지 1차원 배열로 채운다

month = np.array(["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"])

month2d = month.reshape(3,4)
print(month2d) #reshape으로 배열을 다른 형태로 배치 가능 하지만 총 크기는 원본과 동일해야한다.

print(month2d.T) #nxm 형태의 배열을 mxn으로 변경 전치 
print(month2d.swapaxes(0,1)) #축을 서로 바꿈 다차원 행렬에서 사용

x = np.array([[1,2,3],[4,5,6]])
y = np.array([[7,8,9],[10,11,12]])

a = np.concatenate([x,y],axis=1) #x와y를 이어붙인다 axis가 1이면 가로 0이면 세로 행렬의 형태가 같을때만 적용
b = np.concatenate([x,y],axis=0)
print(a)
print(b)

h = np.array([[0],[0]])
i = np.array([[1,2,3],[4,5,6]])
j = np.array([7,8,9])

k = np.vstack([i,j]) #i와 j를 가로로 이어붙임 행렬의 형태가 붙는 쪽의 크기가 같기만 하면 됨 
l = np.hstack([h,i]) #h와 i를 세로로 이어붙임 행렬의 형태가 붙는 쪽의 크기가 같기만 하면 됨 
print(k)
print(l)

a = np.array([1,2,3,4,5,6,7,8,9,10])

x1,x2,x3,x4 = np.split(a,[3,5,7])#a라는 배열의 3,5,7번째를 기준으로 자른다

print(x1,x2,x3,x4)

arr = [100,80,70,90,110]

for i in range(len(arr)):
    print((i-32)*5/9)
    
narr = np.array(arr)

print((narr-32)*5/9) #np array는 배열 전체 값으로 계산 할 수 있다

a = np.array([1,2,3,4]) #np array는 배열의 형태가 같고 크키가 같으면 사칙연산이 가능하다
b = np.array([5,6,7,8])
print(a+b)

n = np.eye(4) + np.ones(4,) #4x4의 단위행렬과 1x4의 1로 이루어진 행렬의 계산
print(np.eye(4))            #원칙적으로는 계산이 되지 않지만 브로드 캐스팅으로 1x4의 배열이 4x4의 배열로 변하며 계산
print(np.ones(4,))          #늘어나는 배열의 값은 y축의 같은 값으로 채워지며 크기가 같아야만 계산가능
print(n)

m = np.ones((3,2))
a = np.arange(6).reshape(3,2)
print(m+a)

grid = np.array([[1,2,3],[4,6,2]])

print(np.mean(grid,axis = 0)) #평균,최대값,최소값, 합계 등등 np에서 계산 가능 axis로 가로행,세로행 계산 가능 0은 세로로 1은 가로로

print(grid > 4) #비교 연산자로 출력 가능
print(np.count_nonzero(grid > 4)) #참인것 개수도 출력 가능