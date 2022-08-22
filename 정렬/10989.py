## 코드 참고 여부
# 딕셔너리 정렬하는 법 찾아봄
    # https://codechacha.com/ko/python-sorting-dict/

## 문제 풀이 방식
# 중복되는 수가 있으므로 딕셔너리 사용해 value로 해당 수의 개수를 저장하면 더 빠르게 정렬 가능할 듯
 
## 슈도 코드
# n 입력받음
# 딕셔너리에 n개의 수 입력받음
# 딕셔너리 key 기준으로 sort 후 출력

## 배운점
# 딕셔너리 정렬
    # sorted(딕셔너리명.items()) return Tuple pair로 이루어진 리스트
    # sorted의 인자로 key lambda x: x[0]을 설정하면 key 기준으로 정렬됨
    # sorted의 인자로 key lambda x: x[1]을 설정하면 value 기준으로 정렬됨

## 걸린 시간
# 11분

import sys

n = int(sys.stdin.readline())
toSort = dict()
for i in range(n):
    tmp = int(sys.stdin.readline())
    if tmp in toSort:
        toSort[tmp] += 1
        continue
    toSort[tmp] = 1
    
result = sorted(toSort.items())
for i in result:
    for j in range(i[1]):
        print(i[0])