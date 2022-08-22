## 배운점 
# boj 참고
    # 출력은 %1000인데 입력은 <= 1000이므로 입력에 1000이 있는데 b = 1일때 고려

import sys

def cal(a, b):
    tmp = [[0 for _ in range(len(a))] for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a)):
            sum = 0
            for t in range(len(a)):
                sum += a[i][t]*b[t][j]
            tmp[i][j] = sum % 1000
    return tmp

def f(a, b):
    if b == 1:
        return a   
    elif b == 2:
        return cal(a, a)
    elif b % 2 == 0:
        res = f(a, b//2)
        return cal(res, res)
    else:
        res = f(a, b//2)
        return cal(cal(res,res), a)

# 입력
n, b = map(int, sys.stdin.readline().split())
a = []
for i in range(n):
    a.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    for j in range(n):
        a[i][j] %= 1000

res = f(a, b)
for i in res:
    print(*i, sep = ' ')
