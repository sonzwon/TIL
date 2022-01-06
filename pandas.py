# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 22:55:45 2021

@author: sby04
"""
## Series
# 1차원배열
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
print(sr[[1,2]])  # 특정 인덱스 인덱싱 할때는 대괄호 2개 쓰는거 잊지마!!
print(sr[['생년월일','성별']])
print(sr[1:2])
print(sr['생년월일':'성별']) # 이름 인덱싱 할 때는 마지막('성별')도 포함!!



### <DataFrame>
# 2차원 배열, 2차원 벡터, 행렬(matrix)
# 행 (row index)
# 열 (column name/column label)
import pandas as pd
  
  dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}  # key값은 columns명, value값은 원소
  df = pd.DataFrame(dict_data)  # 딕셔너리 -> 데이터프레임(type변경)
  #    c0  c1  c2  c3  c4
  # 0   1   4   7  10  13
  # 1   2   5   8  11  14
  # 2   3   6   9  12  15
  print(type(df))
  # <class 'pandas.core.frame.DataFrame'>

# index/columns 설정
  df = pd.DataFrame([[15, '남', '덕영중'],[17, '여', '수리중']],
                index = ['준서','예은'],
                columns = ['나이','성별','학교']) # 인덱스명과 칼럼명을 직접 지정할 수 있음.
  #     나이 성별   학교                          # 리스트가 행으로 변환됨( 아까 딕셔너리에서는 열로 변환)
  # 준서  15  남  덕영중
  # 예은  17  여  수리중
  
# index/columns 변경
  df.index = ['학생1','학생2']         # 인덱스명 변경
  df.columns = ['연령','남녀','소속']   # 칼럼명 변경
  #      연령 남녀   소속
  # 학생1  15  남  덕영중
  # 학생2  17  여  수리중

# rename() : index 또는 columns 일부 선택변경
  df.rename(index = {'준서':'학생1', '예은':'학생2'}, inplace=True)                # 인덱스명 변경  # inplace=True : 원본객체 수정/변경
  df.rename(columns = {'나이':'연령', '성별':'남녀', '학교':'소속'},inplace=True)   # 칼럼명 변경    # inplace=False : 새로운 객체 생성, 원본객체 유지
  #     연령 남녀   소속
  # 준서  15  남  덕영중
  # 예은  17  여  수리중

# drop() : 행 삭제(axis=0) / 열 삭제(axis=1)
  exam_data = {'수학': [90,80,70], '영어':[98,89,95], '음악':[85,95,100], '체육':[100,90,90]}
  df = pd.DataFrame(exam_data, index = ['서준','우현','인아'])
  #     수학 영어 음악 체육
  # 서준  90  98   85  100
  # 우현  80  89   95   90
  # 인아  70  95  100   90
  df.drop('우현',inplace=True)  # axis=0은 default값이므로 적지않아도 됨.
  #     수학 영어 음악 체육
  # 서준  90  98   85  100
  # 인아  70  95  100   90
  df.drop(['우현','인아'], axis=0, inplace=True)  # 여러행을 한번에 삭제할땐 리스트로 묶어서
  #     수학 영어 음악 체육
  # 서준  90  98  85  100
  df.drop('수학', axis=1, inplace=True)
  #      영어 음악 체육
  # 서준  98   85  100
  # 우현  89   95   90
  # 인아  95  100   90
  df.drop(['영어','음악'], axis=1, inplace=True)
  #     수학   체육
  # 서준  90  100
  # 우현  80   90
  # 인아  70   90

# loc : 인덱스 이름 / iloc : 정수형 위치 인덱스
  df = pd.DataFrame(exam_data, index = ['서준','우현','인아'])
  label1 = df.loc['서준']
  # 수학     90
  # 영어     98
  # 음악     85
  # 체육    100
  # Name: 서준, dtype: int64
  position1 = df.iloc[0]
  # 수학     90
  # 영어     98
  # 음악     85
  # 체육    100
  # Name: 서준, dtype: int64
  label2 = df.loc[['서준','우현']]
  position2 = df.iloc[[0,1]]
  #     수학 영어 음악 체육
  # 서준  90  98  85  100
  # 우현  80  89  95   90
  label3 = df.loc['서준':'우현']
  #     수학 영어 음악 체육
  # 서준  90  98  85  100
  # 우현  80  89  95   90
  position3 = df.iloc[0:1]
  #     수학 영어 음악 체육
  # 서준  90  98  85  100
  df.iloc[::2]   # 모든행 2행간격
  df.iloc[0:3:2] # 0~2행 2행간격
  df.iloc[::-1]  # 모든행 역순

# 열 선택
  exam_data = {'이름': ['서준','우현','인아'],
               '수학': [90,80,70],
               '영어': [98,89,95],
               '음악': [85,95,100],
               '체육': [100,90,90]}
  #    이름  수학  영어   음악   체육
  # 0  서준  90  98   85  100
  # 1  우현  80  89   95   90
  # 2  인아  70  95  100   90
  df = pd.DataFrame(exam_data)
  math1 = df['수학']
  # 0    90
  # 1    80
  # 2    70
  # Name: 수학, dtype: int64
  english1 = df.영어
  # 0    98
  # 1    89
  # 2    95
  # Name: 영어, dtype: int64

# 원소선택
# set_index() : 지정 열을 새로운 행인덱스로 지정
  df.set_index('이름',inplace=True)
  #     수학 영어 음악 체육
  # 이름                  
  # 서준  90  98   85  100
  # 우현  80  89   95   90
  # 인아  70  95  100   90
  df.iloc[0,2]           # 85 : 첫번째 행,세번째 열 원소값  # 아까 지정 인덱싱은 대괄호 두개임 이건[행,열] 요런 형태
  df.loc['서준','음악']  # 85 : 서준행, 음악열 원소값'
  df.iloc[0,[1,2]]       # 첫번째 행, 두,세번째 열
  df.loc['서준',['영어','음악']]
  df.iloc[0,1:3]         # 첫번째 행, 두~세번째 열
  df.loc['서준','영어':'음악']
  # 영어    98
  # 음악    85
  # Name: 서준, dtype: int64