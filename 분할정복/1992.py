## 코드 참고 여부
# 혼자품

## 문제 풀이 방식
 
## 슈도 코드

## 배운점 

## 걸린 시간

import sys

def f(inputs, n, str):
    # 바닥조건
    zCheck = ['0'*n]*n
    oCheck = ['1'*n]*n
    if inputs == zCheck:
        str += '0'
    elif inputs == oCheck:
        str += '1'
    else:
        str += '('
        n //= 2
        tmp = [[i[:n] for i in inputs[:n]], [i[n:] for i in inputs[:n]], [i[:n] for i in inputs[n:]], [i[n:] for i in inputs[n:]]]
        
        for i in tmp:
            str = f(i, n, str)
        str += ')'
    return str
        
n = int(sys.stdin.readline())
inputs = []
for i in range(n):
    inputs.append(sys.stdin.readline().strip())

print(f(inputs, n, ''))
