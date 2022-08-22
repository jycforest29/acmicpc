## 코드 참고 여부
# 혼자품

## 문제 풀이 방식
# 생략
 
## 슈도 코드
# 생략

## 배운점 

## 걸린 시간

import sys

n = int(sys.stdin.readline())
stack = []
for i in range(n):
    command = sys.stdin.readline().split()
    if len(command) == 1:
        command = command[0]
        if command == 'pop':
            if len(stack) != 0:
                print(stack[-1])
                del stack[-1]
            else:
                print(-1)
        elif command == 'size':
            print(len(stack))
        elif command == 'empty':
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        elif command == 'top':
            if len(stack) != 0:
                print(stack[-1])
            else:
                print(-1)
    else:
        x = command[1]
        stack.append(x)
