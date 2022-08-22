## 배운점 
# ([[1, 1], [1, 0]])^n

import sys

def cal(a, b):
    tmp = [[0 for i in range(2)] for i in range(2)]
    for i in range(2):
        for j in range(2):
            sum = 0
            for t in range(2):
                sum += a[i][t]*b[t][j]
            tmp[i][j] = sum % 1000000007
    return tmp

def f(base, n, count):
    if n == 0:
        return 0
    elif n == 1:
        return base
    elif n % 2 == 0:
        res = f(base, n//2, count+1)
        return cal(res, res)
    else:
        res = f(base, n//2, count+1)
        return cal(cal(res,res), base)

n= int(sys.stdin.readline())
base = [[1, 1], [1, 0]]
print(f(base, n, 0)[0][1])