## 코드 참고 여부
# 혼자품

## 문제 풀이 방식
# (), [] 페어로 비교
# )나 ]만 stack에 있을 때는 무조건 break
 
## 슈도 코드
# 생략

## 배운점 
# 괄호 안 문자열 대칭을 어떻게 구현해야 할지 모르겠음

## 걸린 시간

import sys

input_ = sys.stdin.readline().rstrip()
res = []

while input_ != '.':
    stack = []
    for i in input_:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')' or i == ']':
            if len(stack) == 0:
                stack.append(i)
                break
            else:
                if i == ')' and stack[-1] == '(':
                    del stack[-1]
                elif i == ']' and stack[-1] == '[':
                    del stack[-1]
                else:
                    stack.append(i)
    if len(stack) == 0:
        res.append('yes')
    else:
        res.append('no')
    input_ = sys.stdin.readline().rstrip()

print(*res, sep = '\n')