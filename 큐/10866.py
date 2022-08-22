## 코드 참고 여부
# 혼자품

## 문제 풀이 방식
 
## 슈도 코드

## 배운점 

## 걸린 시간

import sys
from collections import deque

n = int(sys.stdin.readline())
deq = deque()
count = 0
for i in range(n):
    command = sys.stdin.readline().split()
    if len(command) > 1:
        x = command[1]
    command = command[0]

    if command == 'push_front':
        deq.appendleft(x)
    elif command == 'push_back':
        deq.append(x)
    elif command == 'pop_front':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.popleft())
    elif command == 'pop_back':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.pop())
    elif command == 'size':
        print(len(deq))
    elif command == 'empty':
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    elif command == 'front':
        if len(deq) == 0:
            print(-1)
        else:
            tmp = deq.popleft()
            print(tmp)
            deq.appendleft(tmp)
    elif command == 'back':
        if len(deq) == 0:
            print(-1)
        else:
            tmp = deq.pop()
            print(tmp)
            deq.append(tmp)
