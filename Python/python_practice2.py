# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 00:12:02 2022

@author: sby04
"""
#) 반복문
# for 변수 in 리스트(또는 튜플, 문자열):
#     수행할 문장1
#     수행할 문장2
#     ...
    
#1)
    test_list = ['one', 'two', 'three'] 
    for i in test_list: 
        print(i)
    # one
    # two
    # three

#2)
    a = [(1,2),(3,4),(5,6)]
    for i in a:
        print(i)
    # (1, 2)
    # (3, 4)
    # (5, 6)
    for (i,j) in a:
        print(i+j)
    # 3
    # 7
    # 11

#3)
    marks = [90, 25, 67, 45, 80]
    student = 0           # 학생들에게 번호를 붙여주기 위해
    for mark in marks: 
        student += 1      # student = student +1
        if mark >= 60: 
            print("%d번 학생은 합격입니다." % student)
        else: 
            print("%d번 학생은 불합격입니다." % student)
    # 1번 학생은 합격입니다.
    # 2번 학생은 불합격입니다.
    # 3번 학생은 합격입니다.
    # 4번 학생은 불합격입니다.
    # 5번 학생은 합격입니다.
    student = 0 
    for mark in marks: 
        student += 1 
        if mark < 60:
            continue       # continue : 반복문의 처음으로 돌아감
        print("%d번 학생 축하합니다. 합격입니다. " % student)
    # 1번 학생 축하합니다. 합격입니다. 
    # 3번 학생 축하합니다. 합격입니다. 
    # 5번 학생 축하합니다. 합격입니다. 
    for number in range(len(marks)):  # len(marks) => 5 // range(len(marks)) => range(5) => 0,1,2,3,4
    if marks[number] < 60: 
        continue
    print("%d번 학생 축하합니다. 합격입니다." % (number+1))    


#---------------------------------------------------------------------------
#) 연습문제
l1 = [10,20,30]
for i in l1:
    print(i)
# 10
# 20
# 30

a = [1,2,3,4]
for i in a:
    print('------')
# ------
# ------
# ------
# ------
   
리스트 = [100, 200, 300]
부가세 = 10
for i in 리스트:
    print(i+부가세)
# 110
# 210
# 310

리스트 = ["김밥", "라면", "튀김"]
for i in 리스트:
    print('오늘의 메뉴: ', i)
# 오늘의 메뉴:  김밥
# 오늘의 메뉴:  라면
# 오늘의 메뉴:  튀김

리스트 = ["SK하이닉스", "삼성전자", "LG전자"]
for i in 리스트:
    print(len(i))
# 6
# 4
# 4

리스트 = ['dog', 'cat', 'parrot']
for i in 리스트:
    print(i , len(i))
# dog 3
# cat 3
# parrot 6
for i in 리스트:
    print(i[0])
# d
# c
# p

리스트 = [1, 2, 3]
for i in 리스트:
    print('3 x',i)
# 3 x 1
# 3 x 2
# 3 x 3
for i in 리스트:
    print('3 x',i,'=',3*i)
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9

리스트 = ["가", "나", "다", "라"]
for i in 리스트[1:]:
    print(i)
# 나
# 다
# 라 
for i in 리스트[::2]:
    print(i)
# 가
# 다
for i in 리스트[::-1]:
    print(i)
# 라
# 다
# 나
# 가

리스트 = [3, -20, -3, 44]
for i in 리스트:
    if i<0 :
        print(i)
# -20
# -3

리스트 = [3, 100, 23, 44]
for i in 리스트:
    if i%3==0:
        print(i)
# 3

리스트 = [13, 21, 12, 14, 30, 18]
for i in 리스트:
    if i%3==0 and i<20:
        print(i)
# 12
# 18

리스트 = ["I", "study", "python", "language", "!"]
for i in 리스트:
    if len(i) >= 3:
        print(i)
# study
# python
# language

리스트 = ["A", "b", "c", "D"]
for i in 리스트:
    if i.isupper():   # isupper() : 대문자 여부 판별
        print(i)
# A
# D
for i in 리스트:
    if i.islower():  # i.isupper()==False:  # i.isupper()!=True
        print(i)
# b
# c

리스트 = ['dog', 'cat', 'parrot']
for i in 리스트:
    print(i.capitalize())  
# for i in 리스트:
#     print(i[0].upper() + i[1:])
# Dog
# Cat
# Parrot

리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
for i in 리스트:
    a = i.split('.')
    print(a[0])
# hello
# ex01
# intro

리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in 리스트:
   a = i.split('.')
   if a[-1]=='h':
       print(i)
# intra.h
# define.h
for i in 리스트:
   a = i.split('.')
   if a[-1]=='h' or a[-1]=='c':
       print(i)
# intra.h
# intra.c
# define.h

for i in range(2002,2051,4):
    print(i)
# 월드컵개최

for i in range(1,31):
    if i%3==0:
        print(i)
# 3의 배수

for i in range(1,10):
    print(3,'x',i,'=',i*3)
# 구구단 3단

for i in range(1,10):
    if i%2==1:
        print(3,'x',i,'=',i*3)
# 구구단 3단 홀수번째

result = 0
for i in range(1,11):
    result += i
print(result)
# 55

result = 0
for i in range(1,11):   
    if i%2==1:
        result += i
# for i in range(1,11,2):
#    result += i
print(result)
# 25

result = 1
for i in range(1,11):   
    result *= i
print(result)

price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
    print(price_list(i))
# for i in price_list:
#     print(i)
# 32100
# 32150
# 32000
# 32500
for i in range(len(price_list)):
    print(len(price_list)-i, price_list(i))
# 3 32100
# 2 32150
# 1 32000
# 0 32500
for i in range(1, 4):
    print(90 + 10 * i, price_list[i])
# 100 32150
# 110 32000
# 120 32500

my_list = ["가", "나", "다", "라"]
for i in range(len(my_list)-1):
    print(my_list[i] + my_list[i+1])
# 가나
# 나다
# 다라   

my_list = ["가", "나", "다", "라", "마"]
for i in range(len(my_list)-2):
    print(my_list[i:i+3])
# ['가', '나', '다']
# ['나', '다', '라']
# ['다', '라', '마']

my_list = ["가", "나", "다", "라"]
for i in range(1,len(my_list)):
    print(my_list[-i] + my_list[-i-1])
# 라다
# 다나
# 나가

my_list = [100, 200, 400, 800]
for i in range(len(my_list)-1):
    print(my_list[i+1]-my_list[i])
# 100
# 200
# 400

my_list = [100, 200, 400, 800, 1000, 1300]
for i in range(len(my_list)-2):
    x = my_list[i:i+3]
    print(sum(x)/len(x))
# 233.33333333333334
# 466.6666666666667
# 733.3333333333334
# 1033.3333333333333

low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
volatility = []
for i in range(5):
    volatility.append(low_prices[i]-high_prices[i])
print(volatility)
# [-50, -100, -30, -80, 0]

apart = [['101호','102호'],['201호','202호'],['301호','302호']]
print(apart)

stock = [['시가',100,200,300],['종가',80,210,330]]
print(stock)

stock = {'시가' : [100,200,300], '종가': [80,210,330]}
print(stock)

stock = {'10/10' : [80,110,70,90], '10/11': [210,230,190,200]}

apart = [ [101, 102], [201, 202], [301, 302] ]
for row in apart:       # 변수 apart의 row(행)
    for col in row:     # row(행)의 원소(col)
        print(col, "호")
# 101 호
# 102 호
# 201 호
# 202 호
# 301 호
# 302 호
for row in apart[::-1]:
    for col in row[::-1]:
        print(col,'호')
# 302 호
# 301 호
# 202 호
# 201 호
# 102 호
# 101 호

data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
for row in data:
    for i in row:
        print(i+(i*0.00014))
# 2000.28
# 3050.427
# 2050.287
# 1980.2772
# 7501.05
# 2050.287
# 2050.287
# 1980.2772
# 15452.163
# 15052.107
# 15552.177
# 14902.086

result = []
for row in data:
    for i in row:
        result.append(i+(i*0.00014))
print(result)
# [2000.28, 3050.427, 2050.287, 1980.2772, 7501.05, 2050.287, 2050.287, 1980.2772, 15452.163, 15052.107, 15552.177, 14902.086]

ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for row in ohlc[1:]:
    print(row[-1])
# 100
# 190
# 310
for row in ohlc[1:]:
    if row[-1]>150:
        print(row[-1])
# 190
# 310
for row in ohlc[1:]:
    if row[-1]>=row[0]:
        print(row[-1])
# 100
# 310
volatility = []
for row in ohlc[1:]:
    volatility.append(row[1]-row[2])
print(volatility)
# [40, 30, 10]
for row in ohlc[1:]:
    if row[-1]>row[0]:
        print(row[1]-row[2])
# 10
profit = 0
for row in ohlc[1:]:
    profit += row[-1]-row[0]
print(profit)
# 0








