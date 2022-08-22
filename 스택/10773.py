## 코드 참고 여부
# 혼자품

## 문제 풀이 방식
# 생략
 
## 슈도 코드
# 생략

## 배운점 

## 걸린 시간

import sys

k = int(sys.stdin.readline())
stack = []
for i in range(k):
    input_ = int(sys.stdin.readline())
    if input_ == 0:
        del stack[-1]
    else:
        stack.append(input_)
    
print(sum(stack))
