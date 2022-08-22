
# for i in s-2, e+3
#     if data[i] == wanted 

## 배운점
# 나무를 전체 자른 경우도 포함해야
    # ex. 1 10000000000 -> 10000000000
import sys

def f(start, end, nList, m):
    # 바닥조건
    if end-start <= 1:
        return start
    mid = (start+end) // 2
    count = 0
    for i in nList:
        if i-mid >= 0:
            count += i-mid
    # m보다 많이 잘리면
    if count >= m:
        return f(mid, end, nList, m)
    # m보다 적게 잘리면
    else:
        return f(start, mid, nList, m)
    
n, m = map(int, sys.stdin.readline().split())
nList = list(map(int, sys.stdin.readline().split()))

# 전체를 잘라야 할 때
if nList[0] == m:
    print(0)
else:
    print(f(1, max(nList)+1, nList, m))