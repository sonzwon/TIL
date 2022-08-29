# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 17:36:28 2022

@author: sby04
"""

def print_coin() :
    print('비트코인')
    return
print_coin()
# 비트코인
for i in range(100):
    print_coin()
# 비트코인 100번 호출
def print_coins() :
    for i in range(100):
        print_coin()

def print_with_smile(string):
    print(string+':D')

def print_upper_price(integer):
    print(integer * 0.3)  

def print_sum(x,y):
    print(x+y)

def print_arithmetic_operation(x,y):
    print(x,'+',y,'=',x+y)
    print(x,'-',y,'=',x-y)
    print(x,'*',y,'=',x*y)
    print(x,'/',y,'=',x/y)
print_arithmetic_operation(3,4)
# 3 + 4 = 7
# 3 - 4 = -1
# 3 * 4 = 12
# 3 / 4 = 0.75

def print_max(x,y,z):
    if x>y and x>z:
        print(x)
    elif y>x and y>z:
        print(y)
    else:
        print(z)
print_max(5,9,7)
# 9

def print_reverse(string):
    print(string[::-1])
print_reverse("python")
# nohtyp

def print_score(list):
    print(sum(list)/len(list))
print_score ([1, 2, 3])
# 2.0

def print_even(list):
    for i in list:
        if i%2==0:
            print(i)
print_even ([1, 3, 2, 10, 12, 11, 15])
# 2
# 10
# 12

def print_keys(dic):
    for i in dic.keys():
        print(i)
print_keys ({"이름":"김말똥", "나이":30, "성별":0})
# 이름
# 나이
# 성별

my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}

def print_value_by_key(dic, key):
    print(dic[key])
print_value_by_key  (my_dict, "10/26")
# [100, 130, 100, 100]

def print_5xn(string):
    a = int(len(string)/5)
    for i in range(a+1):
        print(string[i*5:i*5+5])
print_5xn("아이엠어보이유알어걸")
# 아이엠어보
# 이유알어걸

def print_mxn(string,x):
    a = int(len(string)/x)
    for i in range(a+1):
        print(string[i*x:i*x+x])
print_mxn("아이엠어보이유알어걸", 3)
# 아이엠
# 어보이
# 유알어
# 걸

def calc_monthly_salary(annual_salary):
    print(int(round(annual_salary / 12 , -1)))
calc_monthly_salary(12555555)
# 1046300
# round(실수, n) : n<0(소수점자리), n>0(정수자리)

def make_url(address):
    return 'wwww.'+ address+ '.com'
print(make_url('naver'))
# wwww.naver.com

def make_list (string) :
    my_list = []
    for 변수 in string :
        my_list.append(변수)
    return my_list
# def make_list (string) :
#     return list(string)
make_list("abcd")
# ['a', 'b', 'c', 'd']

def pickup_even(list):
    l1 = []
    for i in list:
        if i%2==0:
            l1.append(i)
    return l1
pickup_even([3, 4, 5, 6, 7, 8])
# [4, 6, 8]

def convert_int(num):
    return int(num.replace(',',''))
convert_int("1,234,567")
# 1234567
    
    
    
    
    
    
    
    
    
