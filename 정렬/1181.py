## 코드 참고 여부
# 혼자품

## 문제 풀이 방식
# 길이가 짧은것 - lambda에 첫번째 비교인자?로 len 함수 쓰면 될듯
# 사전순 - 비교가 될때까지 인덱스 0부터 마지막 인덱스까지 비교
 
## 슈도 코드
# n 입력받음
# 입력값 저장할 리스트 생성
# n까지
    # 리스트에 입력받음
# 리스트 중복 제거
# sorted(리스트, key lambda x: (len, x))

## 배운점
# lambda에 원소값 전체를 넣을 경우 알아서 정렬해줌

## 걸린 시간
# 16분

import sys

n = int(sys.stdin.readline())
toSort = []
for i in range(n):
    toSort.extend(sys.stdin.readline().split())

toSort = list(set(toSort))

result = sorted(toSort, key=lambda x: (len(x), x))

for i in result:
    print(i)