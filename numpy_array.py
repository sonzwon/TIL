# numpy_array

# 1) 1차원 배열
import numpy as np      # 배열을 사용하기 위해서는 넘파이 패키지를 임포트해야 함.
ar = np.array([0,1,2,3,4,5,6,7,8,9])
ar
# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
type(ar)
# numpy.ndarray
# 리스트 객체와 배열 객체 차이 : 리스트는 각 원소가 각기 다른 자료형이 될 수 있지만, 배열은 모든 원소가 같은 자룔형이여야 함.
data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
x = np.array(data)
x
2*x
# array([ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18])
# 리스트는 원소에 2를 곱하려면 for문을 돌려서 해야함(번거로움)
a = np.array([1,2,3])
b = np.array([10,20,30])
2*a+b
# array([12, 24, 36])
# 1차원 배열에서는 리스트로 덧셈,곱셈과 같은 연산이 가능함.(결합,반복이 아님)
a == 2 
# array([False,  True, False])




# 2) 2차원 배열
# 행렬(matrix)
# 가로줄 = 행 = row, 세로줄 = 열 = column
c = np.array([[0,1,2],[3,4,5]])
c
# array([[0, 1, 2],
       # [3, 4, 5]])
len(c)     
# 2 : 행의 갯수
len(c[0])  
# 3 : 열의 갯수



# 3) 3차원 배열
d = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]],[[13,14,15,16],[17,18,19,20],[21,22,23,24]]]) 
d   
# array([[[ 1,  2,  3,  4],
#         [ 5,  6,  7,  8],
#         [ 9, 10, 11, 12]],
#        [[13, 14, 15, 16],
#         [17, 18, 19, 20],
#         [21, 22, 23, 24]]])    2 x 3 x 4 array
len(d)
# 2 : 배열의 깊이
len(d[0])
# 3 : 행의 갯수
len(d[0][0])
# 4 : 열의 갯수



# 4) 배열의 차원과 크기
# ndim : 배열의 차원
# shape : 배열의 크기
print(a.ndim)
# 1
print(c.ndim)
# 2
print(d.ndim)
# 3
print(a.shape)
# (3,)  : 1차원 배열의 크기는 np.array([1,2,...,n])이면 (n,)으로 나온다.
print(c.shape)
# (2, 3)
print(d.shape)
# (2, 3, 4)




# 5) 배열의 인덱싱
a = np.array([0,1,2,3,4])
a[2]
# 2
a[-1]
# 4

# axis : 축
a = np.array([[0,1,2],[3,4,5]])
a
# array([[0, 1, 2],
#        [3, 4, 5]])
a[0,0]
# 0 : 첫번째 행의 첫번째 열
a[0,1]
# 1 : 첫번쨰 행의 두번째 열
a[-1,-1]
# 5 : 마지막 행의 마지막 열



# 6) 배열 슬라이싱
a = np.array([[0,1,2,3],[4,5,6,7]])
a
# array([[0, 1, 2, 3],
#        [4, 5, 6, 7]])
a[0,:]
# array([0, 1, 2, 3]) : 첫번째 행 전체
a[:,1]
# array([1, 5]) : 두번째 열 전체
a[1,1:]
# array([5, 6, 7]) : 두번째 행의 두번째 열부터 끝열까지
a[:2,:2]
# array([[0, 1],
#        [4, 5]])  : 첫번째~두번째 행, 첫번째~두번째 열
# 연습문제)
import numpy as np
m = np.array([[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14]])
m
# array([[ 0,  1,  2,  3,  4],
#        [ 5,  6,  7,  8,  9],
#        [10, 11, 12, 13, 14]])
#1. 값7 인덱싱
m[1,2]
#2. 값14 인덱싱
m[-1,-1]
#3. 배열[6,7] 슬라이싱
m[1,1:3]
#3. 배열[7,12] 슬라이싱
m[1:,2]
#4.배열 [[3,4],[8,9]] 슬라이싱
m[:2,3:]



# 7) 배열 인덱싱
a = np.array([0,1,2,3,4,5,6,7,8,9])
idx = np.array([True, False, True, False, True, False, True, False, True, False])
a[idx]
# array([0, 2, 4, 6, 8]) #참인 값에 대해 인덱싱됨
a % 2
# array([0, 1, 0, 1, 0, 1, 0, 1, 0, 1], dtype=int32) 
a % 2 == 0
# array([ True, False,  True, False,  True, False,  True, False,  True, False])
a[a % 2 == 0]
# array([0, 2, 4, 6, 8])
a =  np.array([11,22,33,44,55,66,77,88,99])
idx = np.array([0,2,4,6,8])
a[idx]
# array([11, 33, 55, 77, 99]) # 첫번째,세번째,다섯번째,일곱번째,아홈번째 원소들
a =  np.array([11,22,33,44,55,66,77,88,99])
idx = np.array([0,0,0,0,0,1,1,1,1,1,2,2,2,2,2])
a[idx]
# array([11, 11, 11, 11, 11, 22, 22, 22, 22, 22, 33, 33, 33, 33, 33]) # 첫번째,두번째,세번째 원소들
a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
a
# array([[ 1,  2,  3,  4],
#        [ 5,  6,  7,  8],
#        [ 9, 10, 11, 12]])
a[:,[True, False, False, True]]
# array([[ 1,  4],
#        [ 5,  8],
#        [ 9, 12]])
a[[2,0,1],:]
# array([[ 9, 10, 11, 12],
#        [ 1,  2,  3,  4],
#        [ 5,  6,  7,  8]])
# 연습문제)
x = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
#1. 3의 배수
x[x % 3 == 0] # array([ 3,  6,  9, 12, 15, 18])
#2. 4의 배수
x[x % 4 == 1] # array([ 1,  5,  9, 13, 17])
#3. 3의 배수 & 4의 배수
x1 = x[x % 3 == 0]
x2 = x[x % 4 == 1]
x1.append(x2)




# 8) 넘파이 자료형
# b : 불리언
# i : 정수
# u : 부호 없는 정수
# f : 실수
# U : 문자열
x = np.array([1,2,3])
x.dtype
# dtype('int32')
x = np.array([1,2,3], dtype='f') 
# dtype인수가 없으면 자료형을 스스로 유추하기 때문에, dtype을 지정해줌.
x.dtype
# dtype('float32')
x[0] + x[1]
# 3.0
x = np.array([1,2,3], dtype='U')   # U : 유니코드 문자열 
x[0] + x[1]   # 문자열 결합
# '12'

# inf : infinity(무한대)
# nan : not a number(정의할 수 없는 숫자)
np.array([0,1,-1,0]) / np.array([1,0,0,0])
# array([  0.,  inf, -inf,  nan])




# 9) 배열 생성
# zeros() : 크기가 정해져 있고 모든 값이 0인 배열(인수 : 배열의 크기)
a = np.zeros(5)   # 배열의 크기 : 5
a
# array([0., 0., 0., 0., 0.])
b = np.zeros((2,3))    # 2 X 3을 뜻하는 튜풀
b
# array([[0., 0., 0.],
#        [0., 0., 0.]])
c = np.zeros((5,2), dtype='i')
c
# array([[0, 0],
#        [0, 0],
#        [0, 0],
#        [0, 0],
#        [0, 0]], dtype=int32)
d = np.zeros(5, dtype='U4')  # U4 : 4글자 유니코드
d
# array(['', '', '', '', ''], dtype='<U4')
d[0] = 'abc'
d[1] = 'abcd'
d[2] = 'ABCDE'
d
# array(['abc', 'abcd', 'ABCD', '', ''], dtype='<U4') # 다섯번째 글자는 짤림

# ones : 0이 아닌 1로 초기화된 배열
e = np.ones((2,3,4), dtype='i8')
e
# array([[[1, 1, 1, 1],
#         [1, 1, 1, 1],
#         [1, 1, 1, 1]],
#        [[1, 1, 1, 1],
#         [1, 1, 1, 1],
#         [1, 1, 1, 1]]], dtype=int64)

# ones_likes / zeros_like : 크기를 튜플로 명시하지 않고 다른 배열과 같은 크기의 배열 
f = np.ones_like(e, dtype='f')
f
# array([[[1., 1., 1., 1.],
#         [1., 1., 1., 1.],
#         [1., 1., 1., 1.]],

#        [[1., 1., 1., 1.],
#         [1., 1., 1., 1.],
#         [1., 1., 1., 1.]]], dtype=float32)

# empty : 배열을 생성만 하고 특정한 값으로 초기화를 하지 않는 명령 (배열의 크기가 커지면 배열을 초기화하흔데도 시간이 걸림)
g = np.empty((4,3))
g
# array([[0.0078125, 0.0078125, 0.0078125],
#        [0.0078125, 0.0078125, 0.0078125],
#        [0.0078125, 0.0078125, 0.0078125],
#        [0.0078125, 0.0078125, 0.0078125]])

# arange : 특정한 규칙에 따라 증가하는 수열
np.arange(10)   # 0 ~ (n-1)
# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
np.arange(3,21,2) # (시작, 끝(포함하지 않음), 단계)
# array([ 3,  5,  7,  9, 11, 13, 15, 17, 19])  # 3부터 20까지 2씩 커짐

# linspace / logspace : 성형 구간 혹은 로그 구간 지정한 구간의 수만큼 분할
np.linspace(0, 100, 5)  # (시작, 끝(포함), 갯수)
# array([  0.,  25.,  50.,  75., 100.])  # 0부터 100까지 5구간으로 분할
np.logspace(0.1, 1, 10) # log10(0.1)부터 log10(1)까지 10구간 분할
# array([ 1.25892541,  1.58489319,  1.99526231,  2.51188643,  3.16227766,
#         3.98107171,  5.01187234,  6.30957344,  7.94328235, 10.        ])


# 10) 전치 연산
A = np.array([[1,2,3],[4,5,6]])
A
# array([[1, 2, 3],
#        [4, 5, 6]])
A.T    # 2차원 배열의 전치연산(T속성) : 행과 열을 바꿈
# array([[1, 4],
#        [2, 5],
#        [3, 6]])


# 11) 배열의 크기 변형
# reshape : 내부데이터는 보존한 채로 형태만 바꿈
a = np.arange(12)
a
# array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])
b = a.reshape(3,4)
b
# array([[ 0,  1,  2,  3],
#        [ 4,  5,  6,  7],
#        [ 8,  9, 10, 11]])
a.reshape(3,-1)  # -1 == 4 : 원소12개를 가지는 배열을 행3개인 2차원배열로 바꾸기 위해서는 -1은 4가 된다.
# array([[ 0,  1,  2,  3],
#        [ 4,  5,  6,  7],
#        [ 8,  9, 10, 11]])
a.reshape(2,2,-1)  # -1 == 3
# array([[[ 0,  1,  2],
#         [ 3,  4,  5]],
#        [[ 6,  7,  8],
#         [ 9, 10, 11]]])
a.reshape(2,-1,2)  # -1 == 3
# array([[[ 0,  1],
#         [ 2,  3],
#         [ 4,  5]],
#        [[ 6,  7],
#         [ 8,  9],
#         [10, 11]]])

# a.flatten() / a.ravel() : 다차원배열을 1차원으로
a.flatten()
a.ravel()
# array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])

x = np.arange(5)
x
# array([0, 1, 2, 3, 4])
x.reshape(1,5)
# array([[0, 1, 2, 3, 4]])
# 형태는 같아 보이지만 다른 객체
x.reshape(5,1)
# array([[0],
#        [1],
#        [2],
#        [3],
#        [4]])

# newaxis : 같은 배열에 차원만 1증가 (axis : 축)
x[:, np.newaxis]
# array([[0],
#        [1],
#        [2],
#        [3],
#        [4]])



# 11) 배열 연결
# hstack : 행의 수가 같은 두개 이상의 배열을 옆으로 연결해서 (열이 많아짐)
a1 = np.ones((2,3))
a1
# array([[1., 1., 1.],
#        [1., 1., 1.]])
a2 = np.zeros((2,2))
a2
# array([[0., 0.],
#        [0., 0.]])
np.hstack([a1,a2])
# array([[1., 1., 1., 0., 0.],
#        [1., 1., 1., 0., 0.]])

# vstack : 열의 수가 같은 두개 이상의 배열을 위아래로 연결 (행이 많아짐)
b1 = np.ones((2,3))
b1
b2 = np.zeros((3,3))
b2
np.vstack([b1,b2])
# array([[1., 1., 1.],
#        [1., 1., 1.],
#        [0., 0., 0.],
#        [0., 0., 0.],
#        [0., 0., 0.]])

# dstack : 깊이 방향으로 배열을 합침