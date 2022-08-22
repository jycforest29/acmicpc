## 코드 참고 여부
# 스터디에서 예전에 봤던 풀이로 품
# sorted 함수로 정렬시 다중 조건 설정하기
    # https://lee-jeongmin.github.io/2020/07/13/dictionary-sort-multiple.html

## 문제 풀이 방식
# x, y를 입력받아 sorted 함수를 통해 다중조건 설정 후 정렬
 
## 슈도 코드
# n 입력받음
# 빈 리스트 생성
# n개의 x, y를 리스트에 저장
# 리스트를 1번째 인덱스 기준으로 정렬하되, 정렬 기준값이 같은 것에 대해서는 0번째 인덱스 기준으로 추가 정렬

## 배운점
# sorted 함수에서 lambda 함수 사용해 다중조건 설정
# 이 문제는 x나 y가 유일하지 않기 때문에 딕셔너리로 풀 수 없음

## 걸린 시간

import sys

n = int(sys.stdin.readline())
toSort = []
for i in range(n):
    x, y = map(int, sys.stdin.readline().split(' '))
    toSort.append((x, y))

result = sorted(toSort, key = lambda x: (x[1], x[0]))

for i in result:
    print('{0} {1}'.format(i[0], i[1]))