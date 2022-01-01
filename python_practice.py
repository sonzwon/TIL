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
# aBcda = "3"
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

