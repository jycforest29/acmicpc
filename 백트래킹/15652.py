## 코드 참고 여부

## 문제 풀이 방식
 
## 슈도 코드

## 배운점 

## 걸린 시간

import sys

def rec(idx, remain, arr):
    if remain == 0:
        print(*arr, end = '\n')
        return
    for i in range(idx, n):
        arr.append(i+1)
        rec(i, remain-1, arr)
        del arr[-1]

n, m = map(int, sys.stdin.readline().split())
rec(0, m, [])