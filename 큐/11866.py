## 코드 참고 여부
# 혼자품

## 문제 풀이 방식
# 2 3 4 | 5 | [1]
# 2 3 4 2 3 4

## 슈도 코드

## 배운점 

## 걸린 시간

import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
deq = deque([i+1 for i in range(n)])
res = []
count = n-1
index = k-1

while deq:
    res.append(deq.pop(index))
    if count == 0:
        break
    index = (index+k-1)%count
    count -= 1

print('<', end = '')
print(*res, sep = ', ', end = '')
print('>', end = '')
