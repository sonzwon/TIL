# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 22:55:45 2021

@author: sby04
"""
## Series

import pandas as pd
dict_data = {'a':1,'b':2,'c':3}
sr = pd.Series(dict_data)
print(type(sr))
# <class 'pandas.core.series.Series'>
print(sr)
# a    1
# b    2
# c    3
# dtype: int64


list_data = ['2019-01-01', 3.14, 'ABC', 100, True]
sr = pd.Series(list_data)
print(sr)
# 0    2019-01-01
# 1          3.14
# 2           ABC
# 3           100
# 4          True
# dtype: object
idx = sr.index
val = sr.values
print(idx)
print(val)
# RangeIndex(start=0, stop=5, step=1)
# ['2019-01-01' 3.14 'ABC' 100 True]


tup_data = ('영인','2010-05-01','여',True)
sr = pd.Series(tup_data, index = ['이름','생년월일','성별','학생여부'])
print(sr)
# 이름              영인
# 생년월일    2010-05-01
# 성별               여
# 학생여부          True
# dtype: object
print(sr[0])
print(sr['이름'])
print(sr[[1,2]])
print(sr[['생년월일','성별']])
print(sr[1:2])
print(sr['생년월일':'성별'])



## DataFrame






























