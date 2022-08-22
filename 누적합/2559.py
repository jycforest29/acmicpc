## 코드 참고 여부
# 시간 초과되어 max 함수말고 다른 정렬 방법 찾아봄
    # https://velog.io/@mmy789/Algorithm-%EC%B5%9C%EC%86%8C%ED%9E%99-%EC%B5%9C%EB%8C%80%ED%9E%99

## 문제 풀이 방식
# 누적합 구해서 빼는 방식으로 품
 
## 슈도 코드
# 누적합 구하는 방식은 동일(이하 sums)
# 뺀 수를 저장할 리스트(이하 tmp)
# k-1부터 n-1까지
    # tmp.append(누적합리스트[인덱스]-누적합리스트[인덱스-k])

## 배운점
# 누적합에서는 list의 sum 메서드 쓰면 시간 초과뜸
# max, min 함수의 시간복잡도는 n
# heapq 사용법

## 걸린 시간

import sys

n, k = map(int,sys.stdin.readline().split())
inputList = list(map(int,sys.stdin.readline().split()))
sums = []

sum = 0
for i in range(len(inputList)):
    sum += inputList[i]
    sums.append(sum)

tmp = []
for i in range(k-1, n): # [k-1, n-1]
    if i == k-1:
        tmp.append(sums[i])
        continue
    tmp.append(sums[i] - sums[i - k]) # append 내부 값 범위 : [k] - [0] 부터 [n-1] - [n-1-k]

print(max(tmp))
