## 코드 참고 여부

## 문제 풀이 방식
# n개의 수를 리스트에 저장 후 i-1부터 j-1까지 더하면 될듯
 
## 슈도 코드
# n, m 입력받음
# 리스트에 n개의 입력 담기
# m 동안
    # 리스트의 [i-1:j]까지 더하기
 
## 배운점

## 걸린 시간

import sys

n, m = map(int, sys.stdin.readline().split())
tmp = list(map(int, sys.stdin.readline().split()))
sums = [0]*n
sum = 0
stack = []

for i in range(len(tmp)):
    sum += tmp[i]
    sums[i] = sum

for i in range(m):
    i, j = map(int, sys.stdin.readline().split())
    max_ = max(i, j)-1
    min_ = min(i, j)-1
    if min_-1 < 0:
        stack.append(sums[max_])
        continue 
    stack.append(sums[max_]-sums[min_-1])

for i in stack:
    print(i)