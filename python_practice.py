# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 16:10:01 2022

@author: sby04
"""
### 1) 기초

print('Hello World')
# Hello World
print("Mary's cosmetics")
# Mary's cosmetics
print('신씨가 소리질렀다. "도둑이야"')
# 신씨가 소리질렀다. "도둑이야"
print("C:\Window")
# C:\Window
print("안녕하세요.\n만나서\t\t반갑습니다.") 
# 안녕하세요.
# 만나서		반갑습니다.  -> \n:줄바꿈, \t:탭
print("오늘은","일요일")
# 오늘은 일요일
print('naver','kakao','sk','samsung',sep=';')
# naver;kakao;sk;samsung
print('naver','kakao','sk','samsung',sep='/')
# naver/kakao/sk/samsung
print("first");print("second") # print("first";"second")->Error!'
# first
# second   == print("first\nsecond")
print(5/3)
# 1.6666666666666667

# ----------------------------------------------------------------------------

### 2) 변수

삼성전자 = 50000
총평가금액 = 삼성전자*10
print(총평가금액)
# 500000
시가총액 = 2980000000000
현재가 = 50000
PER = 15.79
print(시가총액, type(시가총액))
print(현재가, type(현재가))
print(PER, type(PER))
# 298조 <class 'str'>
# 50,000원 <class 'str'>
# 15.79 <class 'float'>
s = "hello"
t = "python"
print(s+'!', t)
# hello! python
2 + 2 * 3
# 8
a = "132"
print(type(a))
# <class 'str'>
num_str = "720"
int(num_str)
# 720
num = 100
str(num)
# '100'
num1 = "15.79"
float(num1)
# 15.79
year = "2020"
int(year)
print(int(year)-1)
print(int(year)-2)
print(int(year)-3)
# 2019
# 2018
# 2017
price = 48584
total = price*36
print(total)
# 1749024

# ----------------------------------------------------------------------------

### 3) 문자열

letters = 'python'
print(letters[0], letters[2])
# p t
license_plate = "24가 2210"
print(license_plate[4:])
# 2210
string = "홀짝홀짝홀짝"
print(string[::2])   # 시작인덱스:끝인덱스:오프셋(규칙)
# 홀홀홀
string = 'PYTHON'
print(string[::-1])
# NOHTYP
phone_number = "010-1111-2222"
print(phone_number.replace('-',' '))
# 010 1111 2222
print(phone_number.replace('-',''))
# 01011112222
url = "http://sharebook.kr"
domain = url.split('.')
print(domain[-1])
print(url.split('.')[-1])
# kr
lang = 'python'
lang[0] = 'P'
print(lang)
# 문자열이 할당(assignment) 메서드를 지원하지 않음
string = 'abcdfe2a354a32a'
print(string.replace('a','A'))
# 'Abcdfe2A354A32A'
string = 'abcd'
print(string.replace('b', 'B'))
# aBcd
a = "3"
b = "4"
print(a+b)
# 34
print("Hi"*3)
# HiHiHi
t1 = 'python'
t2 = 'java'
t3 = t1 + ' ' + t2 + ' '
print(t3*4)
# python java python java python java python java 
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print('이름 : %s 나이 : %d' %(name1, age1))
print('이름 : %s 나이 : %d' %(name2, age2))
print('이름 : {} 나이 : {}' .format(name1, age1))
print('이름 : {} 나이 : {}' .format(name2, age2))
print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}")
# 이름 : 김민수 나이 : 10
# 이름 : 이철희 나이 : 13
상장주식수 = "5,969,782,550"
a = 상장주식수.replace(',','')
A = int(a)
type(A)
# int
분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])
# 2020/03
data = "   삼성전자    "
print(data.strip())
# 삼성전자
ticker = "btc_krw"
print(ticker.upper())
# BTC_KRW
ticker = "BTC_KRW"
print(ticker.lower())
# btc_krw
a = 'hello'
a.capitalize()
# 'Hello'
file_name = "보고서.xlsx"
file_name.endswith("xlsx")
# True
file_name.endswith(("xlsx","xls"))
# True
file_name = "2020_보고서.xlsx"
file_name.startswith("2020")
# True
a = "hello world"
a.split()
a.split(' ')
# ['hello', 'world']
ticker = "btc_krw"
ticker.split('_')
# ['btc', 'krw']
date = "2020-05-01"
date.split('-')
# ['2020', '05', '01']
data = "039490     "
data.rstrip()
# '039490'

# ----------------------------------------------------------------------------

### 4) 리스트

movie_rank = ['닥터 스트레인지','스플릿','럭키']
movie_rank.append('베트맨')
print(movie_rank)
# ['닥터 스트레인지', '스플릿', '럭키', '베트맨']
movie_rank.insert(1,'슈퍼맨')
print(movie_rank)
# ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '베트맨']
movie_rank.remove('럭키')
del movie_rank[3]
# ['닥터 스트레인지', '슈퍼맨', '스플릿', '베트맨']
del movie_rank[1:3]
# ['닥터 스트레인지', '베트맨']
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2
print(langs)
# ['C', 'C++', 'JAVA', 'Python', 'Go', 'C#']
nums = [1, 2, 3, 4, 5, 6, 7]
max(nums)
# 7 
min(nums)
# 1
nums = [1, 2, 3, 4, 5]
sum(nums)
# 15
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두",
        "쫄면", "소시지", "라면", "팥빙수", "김치전"]
len(cook)
# 12
nums = [1, 2, 3, 4, 5]
평균 = sum(nums)/len(nums)
print(평균)
# 3.0
price = ['20180728', 100, 130, 140, 150, 160, 170]
price[1:]
# [100, 130, 140, 150, 160, 170]
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums[::2]
# [1, 3, 5, 7, 9]
nums[1::2]
# [2, 4, 6, 8, 10]
nums = [1, 2, 3, 4, 5]
nums[::-1]
# [5, 4, 3, 2, 1]
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0],interest[2])
# 삼성전자 Naver
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(" ".join(interest))
# 삼성전자 LG전자 Naver SK하이닉스 미래에셋대우
print("/".join(interest))
# 삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우
print("\n".join(interest))
# 삼성전자
# LG전자
# Naver
# SK하이닉스
# 미래에셋대우
string = "삼성전자/LG전자/Naver"
string.split('/')
# ['삼성전자', 'LG전자', 'Naver']
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
data.sort(reverse=False)
sorted(data)
# [1, 2, 3, 4, 5, 9, 10]
data.sort(reverse=True)
# [10, 9, 5, 4, 3, 2, 1]

# ----------------------------------------------------------------------------

### 5) 튜플

my_variable = ()
type(my_variable)
# tuple
movie_rank = ('닥터 스트레인지','스플릿','럭키')
a = (1)
type(a)
# int
a = (1,)
type(a)
# tuple
t = (1, 2, 3)
t[0] = 'a'
#Traceback (most recent call last):
#  File "<pyshell#46>", line 1, in <module>
#    t[0] = 'a'
#TypeError: 'tuple' object does not support item assignment
# 튜플은 원소의 값을 변경할 수 없음(리스트와의 차이)
t = 1, 2, 3, 4
type(t)
# tuple -> 투플은 괄호없이도 동작함
t = ('a', 'b', 'c')
t = ('A', 'b', 'c')
# ('A', 'b', 'c')
interest = ['삼성전자', 'LG전자', 'SK Hynix']
tuple(interest)
# ('삼성전자', 'LG전자', 'SK Hynix')
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)
# apple banana cake
tuple(range(2,100,2))

# ----------------------------------------------------------------------------

### 6) 딕셔너리

a, b, *c = (0, 1, 2, 3, 4, 5) 
a
# 0
b
# 1
c
# [2, 3, 4, 5]
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score,a,b = scores 
valid_score
# [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5]
a,b,*valid_score = scores 
# [8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a,*valid_score,b = scores 
# [8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8]
temp = {}
icecream = {'메로나':1000, '폴라포':1200, '빵빠레':1800}
# {'메로나': 1000, '폴라포': 1200, '빵빠레': 1800}
icecream['죠스바']=1200
icecream['월드콘']=1500
# {'메로나': 1000, '폴라포': 1200, '빵빠레': 1800, '죠스바': 1200, '월드콘': 1500}
print('메로나 가격 :', icecream['메로나'])
# 메로나 가격 : 1000
icecream['메로나']=1300
# {'메로나': 1300, '폴라포': 1200, '빵빠레': 1800, '죠스바': 1200, '월드콘': 1500}
del icecream['메로나']
# {'폴라포': 1200, '빵빠레': 1800, '죠스바': 1200, '월드콘': 1500}
inventory = {'메로나':[300,20],'비비빅':[400,3],'죠스바':[250,100]}
# {'메로나': [300, 20], '비비빅': [400, 3], '죠스바': [250, 100]}
print(inventory['메로나'][0],'원')
# 300 원
print(inventory['메로나'][1],'개')
# 20 개
inventory['월드콘'] = [500,7]
# {'메로나': [300, 20], '비비빅': [400, 3], '죠스바': [250, 100], '월드콘': [500, 7]}
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
ice = icecream.keys()
list(ice)
# ['탱크보이', '폴라포', '빵빠레', '월드콘', '메로나']
sum(list(icecream.values()))
# 6700
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update(new_product)
# {'탱크보이': 1200,
#  '폴라포': 1200,
#  '빵빠레': 1800,
#  '월드콘': 1500,
#  '메로나': 1000,
#  '팥빙수': 2700,
#  '아맛나': 1000}
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
result = dict(zip(keys,vals))
# {'apple': 300, 'pear': 250, 'peach': 400}
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(date, close_price))
# {'09/05': 10500,
#  '09/06': 10300,
#  '09/07': 10100,
#  '09/08': 10800,
#  '09/09': 11000}

# ----------------------------------------------------------------------------

### 6) 분기문

if True :
    print ("1")
    print ("2")
else :
    print("3")
print("4")
# 1
# 2
# 4
user = input('입력 : ')
print(user*2)
# 입력 : 안녕하세요
# 안녕하세요안녕하세요
user = input('숫자를 입력하세요 : ')
print(int(user)+10)
# 숫자를 입력하세요 : 30
# 40
user = input('')
if int(user) % 2 == 0:
    print('짝수')
else:
    print('홀수')
# 30
# 짝수
user = input('')
if int(user)+20>255 :
    print(255)
else:
    print(int(user)+20)
# 200
# > 220
# 240
# > 255
user = input('')
result = int(user)-20
if result<0:
    print(0)
elif result>255:
    print(255)
else:
    print(result)
# 15
# > 0
user = input('현재시간 : ')
time = str(user)
if time[-2:] =='00':
    print('정각입니다.')
else:
    print('정각이 아닙니다.')
# 현재시간 : 2:10
# 정각이 아닙니다.
fruit = ["사과", "포도", "홍시"]
user = input('좋아하는 과일은? ')
if user in fruit:
    print('정답입니다.')
else:
    print('오답입니다')
# 좋아하는 과일은? 사과
# 정답입니다.
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
user = input('종목명 : ')
if user in warn_investment_list:
    print('투자 경고 종목입니다.')
else:
    print('투자 경고 종목이 아닙니다.')
# 종목명 : Google
# 투자 경고 종목입니다.
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
season = list(fruit.keys())
user = input('제가 좋아하는 계절은 : ')
if user in season:
    print('정답입니다.') 
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# user = input("제가좋아하는계절은: ")
# if user in fruit:
#     print("정답입니다.")
# else:
#     print("오답입니다.")
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
user = input('제가 좋아하는 과일은 : ')
if user in fruit.values():
    print('정답입니다.')
else :
    print('오답입니다')
# 제가 좋아하는 과일은 : 한라봉
# 오답입니다
user = input('')
if user.islower()==True:
    print(user.upper())
else:
    print(user.lower())
# abcd
# ABCD
user = int(input(''))
if 81<=user<=100 :
    print('grade is A')
elif 61<=user<=80 :
    print('grade is B')
elif 41<=user<=60 :
    print('grade is C')
elif 21<=user<=40 :
    print('grade is D')
else:
    print('grade is E')
# 83
# grade is A
#*****
per = {'달러':1167,'엔':1.096,'유로':1268,'위안':171}
user = input('입력 :') # '100 달러'
money = user.split()  # 공백기준 분리 ['100','달러']
amount = money[0]
currency = money[1]  # amount, currency = money (=> user.split())
amount = float(amount)
if currency == '달러':
    print(amount*per[currency],'원')
elif currency == '엔':
    print(amount*per[currency],'원')
elif currency == '유로':
    print(amount*per[currency],'원')
else :
    print(amount*per[currency],'원')
# 입력 :50 달러
# 58350.0 원
#*****
num1 = int(input('number1 : '))
num2 = int(input('number2 : '))
num3 = int(input('number3 : '))
num_list = [num1, num2, num3]
max(num_list)
# number1 : 10
# number2 : 9
# number3 : 20
# > 20
tel = {'011':'SKT','016':'KT','019':'LGU','010':'알수없음'}
user = input('휴대전화번호 입력(-포함) : ')
vno = user.split('-')[0]
if vno == '011':
    print(tel[vno])
elif vno == '016':
    print(tel[vno])
elif vno == '019':
    print(tel[vno])
else:
    print('알수없음')
# 휴대전화번호 입력(-포함) : 011-111-2222
# SKT
우편번호 = input("우편번호: ")
우편번호 = 우편번호[:3]
if 우편번호 in ["010", "011", "012"]:
    print("강북구")
elif 우편번호 in ["014", "015", "016"]:
    print("도봉구")
else:
    print("노원구")
# 우편번호: 01156
# 강북구
user = input('주민등록번호(-포함) : ')
gender = user.split('-')[1][0]
if gender == '1' or gender == '3' :
    print('남자')
elif gender == '2' or gender == '4' :
    print('여자')
else :
    print('다시 입력해주십시오.')
# 주민등록번호(-포함) : 123456-2222222
# 여자
user = input('주민등록번호(-포함) : ')
address = user.split('-')[1][1:3]
if 0<=int(address)<=8 :
    print('서울입니다')
else :
    print('서울이 아닙니다')
# 주민등록번호(-포함) : 123456-1666666
# 서울이 아닙니다
user = input('주민등록번호(-포함) : ')
num = user.replace('-', '')
last = user.split('-')[1][-1]
계산1 = (int(num[0]) * 2 + int(num[1]) * 3 + int(num[2]) * 4 + int(num[3]) * 5 + int(num[4]) * 6 + 
        int(num[5]) * 7 + int(num[6]) * 8 + int(num[7]) * 9 + int(num[8]) * 2 + int(num[9])* 3 +
        int(num[11])* 4 + int(num[12]) * 5)
계산2 = 11 - (계산1 % 11)
계산3 = str(계산2)
if last == 계산3 :
    print('유효한 주민등록번호 입니다.')
else:
    print('유효한 주민등록번호가 아닙니다.')
# 주민등록번호(-포함) : 123456-7894561
# 유효한 주민등록번호가 아닙니다.










