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
    print(string[:5])
    print(string)




