# 백준 2525번
# 내 풀이
import datetime as dt
from dateutil.relativedelta import relativedelta
A, B = map(int, input().split())
C = int(input())
time = dt.datetime.strptime('{} {}'.format(A,B), '%H %M')
take_time = relativedelta(minutes=C)
end_time = time+take_time
print(end_time.strftime('%H %M'))

# 정답지 풀이
H, M = map(int, input().split())
timer = int(input()) 
H += timer // 60
M += timer % 60
if M >= 60:
    H += 1
    M -= 60
if H >= 24:
    H -= 24
print(H,M)



#백준 2530번
#내 풀이1
A,B,C = map(int, input().split())
D = int(input())
A += D//3600
B += (D%3600)//60
C += (D%3600)%60
if C >= 60:
    C -= 60
    B += 1
if B >= 60:
    B -= 60
    A += 1
if A >= 24:
    A -= 24
print(A,B,C)

#내 풀이2
H, M, S = map(int, input().split())
t = int(input()) 
S += t
M += S//60
H += M//60
print(H%24, M%60, S%60)



#백준 5355번
#내 풀이
n = int(input())
for _ in range(n):
    T = list(input().split())
    num = float(T[0])
    for i in range(len(T)):
        if T[i] =='@':
            num *= 3
        elif T[i] == '%':
            num += 5
        elif T[i] == '#':
            num -= 7
    print('%0.2f' %num)