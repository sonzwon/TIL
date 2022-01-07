# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 00:12:02 2022

@author: sby04
"""

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






