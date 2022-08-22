## 코드 참고 여부
# 혼자품

## 문제 풀이 방식
# 중복되는 수가 있으므로 딕셔너리 사용해 value로 해당 수의 개수를 저장하면 더 빠르게 정렬 가능할 듯
 
## 슈도 코드
# n 입력받음
# 딕셔너리에 n개의 수 입력받음
# 딕셔너리 key 기준으로 sort 후 출력

## 배운점
# .sort()의 시간복잡도는 O(nlogn)

## 걸린 시간
# 5분

import sys

n = int(sys.stdin.readline())
toSort = dict()
for i in range(n):
    tmp = int(sys.stdin.readline())
    if tmp in toSort:
        toSort[tmp] += 1
        continue
    toSort[tmp] = 1
    
print(toSort)