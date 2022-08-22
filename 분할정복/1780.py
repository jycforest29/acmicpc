## 코드 참고 여부
# 혼자품

## 문제 풀이 방식
 
## 슈도 코드

## 배운점 

## 걸린 시간

import sys

def f(inputs, n, counts):
    # 바닥조건
    zCheck = [[0]*n]*n
    oCheck = [[1]*n]*n
    mCheck = [[-1]*n]*n
    if inputs == mCheck:
        counts[0] += 1
    elif inputs == zCheck:
        counts[1] += 1
    elif inputs == oCheck:
        counts[2] += 1
    else:
        n //= 3
        tmp = [[i[:n] for i in inputs[:n]], [i[n:2*n] for i in inputs[:n]], [i[2*n:3*n] for i in inputs[:n]], 
        [i[:n] for i in inputs[n:2*n]], [i[n:2*n] for i in inputs[n:2*n]], [i[2*n:3*n] for i in inputs[n:2*n]],
        [i[:n] for i in inputs[2*n:3*n]], [i[n:2*n] for i in inputs[2*n:3*n]], [i[2*n:3*n] for i in inputs[2*n:3*n]]]
        for i in tmp:
            counts = f(i, n, counts)
    return counts
        
n = int(sys.stdin.readline())
inputs = []
for i in range(n):
    inputs.append(list(map(int, sys.stdin.readline().strip().split())))

print(*f(inputs, n, [0, 0, 0]), sep = '\n')
