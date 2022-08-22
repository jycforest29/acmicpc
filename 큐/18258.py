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

    if command == 'push':
        deq.append(x)
        count += 1
    elif command == 'pop':
        if count == 0:
            print(-1)
        else:
            print(deq.popleft())
            count -= 1
    elif command == 'size':
        print(count)
    elif command == 'empty':
        if count == 0:
            print(1)
        else:
            print(0)
    elif command == 'front':
        if count == 0:
            print(-1)
        else:
            tmp = deq.popleft()
            print(tmp)
            deq.appendleft(tmp)
    elif command == 'back':
        if count == 0:
            print(-1)
        else:
            tmp = deq.pop()
            print(tmp)
            deq.append(tmp)
