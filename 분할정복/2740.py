## 코드 참고 여부
# 혼자품

## 문제 풀이 방식
 
## 슈도 코드

## 배운점 

## 걸린 시간

import sys

n , m= map(int, sys.stdin.readline().split())
a = []
for i in range(n):
    a.append(list(map(int, sys.stdin.readline().split())))
m_ , k= map(int, sys.stdin.readline().split())
b = []
for i in range(m):
    b.append(list(map(int, sys.stdin.readline().split())))

# n m   m_ k
# 1 2 |-1 -2 0
# 3 4 | 0  0 3
# 5 6

# a[0][0]*b[0][0]+a[0][1]*b[1][0]
# a[0][0]*b[0][1]+a[0][1]*b[1][1]
# a[0][0]*b[0][2]+a[0][1]*b[1][2]
# -> a

res = [[0 for i in range(k)] for i in range(n)]
for i in range(n):
    for j in range(k):
        sum = 0
        for t in range(m):
            sum += a[i][t]*b[t][j]
        res[i][j] = sum

for i in res:
    print(*i, sep = ' ')