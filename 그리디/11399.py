## 코드 참고 여부
# 혼자품

## 문제 풀이 방식
# 정렬 후 sum(누적합리스트)
 
## 슈도 코드
# n 입력받음
# pi 리스트 입력받음
# 누적합리스트 구하기
# sum(누적합리스트)

## 배운점 

## 걸린 시간

import sys

n = int(sys.stdin.readline())
piList = list(map(int, sys.stdin.readline().split()))
piList.sort()
sums = []
sum_ = 0
for i in range(n):
    sum_ += piList[i]
    sums.append(sum_)

print(sum(sums))
