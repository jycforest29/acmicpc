## 코드 참고 여부

## 문제 풀이 방식
 
## 슈도 코드

## 배운점 

## 걸린 시간

import sys

def rec(remain, arr):
    if remain == 0:
        print(*arr, end = '\n')
        return
    for i in range(n):
        arr.append(i+1)
        rec(remain-1, arr)
        del arr[-1]

n, m = map(int, sys.stdin.readline().split())
rec(m, [])