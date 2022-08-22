## 코드 참고 여부
# 혼자품

## 문제 풀이 방식
 
## 슈도 코드

## 배운점 

## 걸린 시간

import sys

def f(inputs, n, w, b):
    wCheck = [[0]*n for i in range(n)]
    bCheck = [[1]*n for i in range(n)]
    if inputs == wCheck:
        w += 1
    elif inputs == bCheck:
        b += 1
    else:
        n //= 2
        tmp = [[i[:n] for i in inputs[:n]], 
        [i[n:] for i in inputs[:n]], 
        [i[n:] for i in inputs[n:]], 
        [i[:n] for i in inputs[n:]]]
        for i in tmp:
            w, b = f(i, n, w, b)
    return w, b
    
        
n = int(sys.stdin.readline())
inputs = []
for i in range(n):
    inputs.append(list(map(int, sys.stdin.readline().split())))

w, b = f(inputs, n, 0, 0)
print(w)
print(b)