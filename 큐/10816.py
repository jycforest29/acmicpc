## 코드 참고 여부
# 혼자품

## 문제 풀이 방식
 
## 슈도 코드

## 배운점 

## 걸린 시간

import sys
from collections import deque

n = int(sys.stdin.readline())
nQueue = deque(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
mQueue = deque(list(map(int, sys.stdin.readline().split())))
counts = []
for i in mQueue:
    counts.append(nQueue.count(i))
print(*counts)