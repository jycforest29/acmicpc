## 코드 참고 여부
# 혼자품

## 문제 풀이 방식
# 결국 n개의 좌표에 대해 각각의 순서-1을 리턴해야
# n의 범위가 10만까지이므로 딕셔너리로 해야 빠를듯
 
## 슈도 코드
# n 입력받음
# 빈 리스트 생성
# n까지
    # 각 입력을 빈 리스트에 담음
# 리스트를 기준으로 정렬 후 각 리스트 원소를 딕셔너리의 key값, 순서를 딕셔너리의 value값으로 담음
# 입력 리스트의 원소에 대해 딕셔너리 value값 출력

## 배운점

## 걸린 시간
# 16분?

import sys

n = int(sys.stdin.readline())
toSort = list(map(int, sys.stdin.readline().split()))
tmp = sorted(list(set(toSort)))

compressed = dict()
for i in range(len(tmp)):
    compressed[tmp[i]] = i

for i in toSort:
    print(compressed[i], end = ' ')