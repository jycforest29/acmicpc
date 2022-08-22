## 코드 참고 여부
# 혼자품

## 문제 풀이 방식
# 생략
 
## 슈도 코드
# 생략

## 배운점 

## 걸린 시간

import sys

t = int(sys.stdin.readline())
for i in range(t):
    input_ = sys.stdin.readline().strip()
    stack = [input_[0]]
    for i in range(1, len(input_)):
        if len(stack) == 1 and stack[0] == ')':
            break
        if input_[i] == ')':
            if len(stack) == 0:
                stack.append(input_[i])
            else:
                del stack[-1]
        else:
            stack.append(input_[i])
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')
