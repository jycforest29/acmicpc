## 코드 참고 여부
# 혼자품

## 문제 풀이 방식
 
## 슈도 코드

## 배운점 

## 걸린 시간

import sys
from collections import deque

n = int(sys.stdin.readline())
deq = deque([i+1 for i in range(n)])

while True:
    if len(deq) <= 1:
        break
    deq.popleft()
    tmp = deq.popleft()
    deq.append(tmp)
print(deq.pop())