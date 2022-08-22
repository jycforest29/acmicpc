## 코드 참고 여부
# 혼자품

## 문제 풀이 방식
 
## 슈도 코드

## 배운점 
 
## 걸린 시간

import sys

def f(left, right, a, i):
    mid = (left+right) // 2
    if a[mid] == i:
        return 1
    else:
        if left > right and a[mid] != i:
            return 0
        elif a[mid] > i:
            return f(left, mid-1, a, i)
        else:
            return f(mid+1, right, a, i)

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
a.sort()
m = int(sys.stdin.readline())
mList = list(map(int, sys.stdin.readline().split()))
for i in mList:
    print(f(0, n-1, a, i))


