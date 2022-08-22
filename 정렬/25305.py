## 코드 참고 여부
# 혼자품

## 문제 풀이 방식
# 점수리스트를 내림차순 정렬시 점수리스트[k-1]을 구해라
 
## 슈도 코드
# 생략

## 배운점 

## 걸린 시간

import sys

n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

arr.sort(reverse = True)
print(arr[k-1])