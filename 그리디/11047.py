## 코드 참고 여부
# 혼자품

## 문제 풀이 방식
# 동전의 종류가 모두 배수이므로 그리디로 풀 수 있음
 
## 슈도 코드
# n, k 입력받음
# 동전 종류 리스트 생성
# n 동안
    # 동전 종류 리스트에 동전 종류 역순으로 저장

# count = 0
# k가 0보다 클동안
    # k >= 동전 종류이면
        # count + k // 동전종류
        # k = k % 동전종류
# count 출력

## 배운점 

## 걸린 시간

import sys

n, k = map(int, sys.stdin.readline().split())
tmp = [0]*n
for i in range(n):
    tmp[n-1-i] = int(sys.stdin.readline())

count = 0
j = 0
while k > 0:
    if k >= tmp[j]:
        count += k // tmp[j]
        k %= tmp[j]
    j += 1

print(count)
