## 코드 참고 여부
# 반례 참고

## 문제 풀이 방식
# 입력 타입: 최빈값에서 딕셔너리 필요하므로 딕셔너리 형태로 입력받음, 중앙값에서 딕셔너리 말고 리스트가 필요하므로 입력리스트로도 입력받음
# 산술평균: round(key의 합, 1)
# 중앙값: 입력리스트 정렬 후 index = (총개수-1)//2
# 최빈값: value 기준으로 reverse 정렬. index = 0
# 범위: 중앙값 정렬의 index = -1과 index = 0 차이
 
## 슈도 코드
# n 입력받음
# 딕셔너리, 입력리스트 생성
# n개의 입력 딕셔너리, 입력리스트에 저장
# 입력리스트 정렬

# round(sum(딕셔너리.keys), 1): 산술평균
# 입력리스트 [len(딕셔너리)-1 // 2]: 중앙값
# sorted(딕셔너리, value 기준, reverse=True)[0]: 최빈값
# sorted(딕셔너리, key 기준)[-1] - sorted(딕셔너리, key 기준)[0]

## 배운점
# toSort.keys()) / len(toSort)로 산술평균을 구하면 안됨

## 걸린 시간

import sys

n = int(sys.stdin.readline())
toSort = dict()
inputList = []
for i in range(n):
    tmp = int(sys.stdin.readline())
    inputList.append(tmp)
    if tmp in toSort:
        toSort[tmp] += 1
        continue
    toSort[tmp] = 1

inputList = sorted(inputList)
sortedByKey = sorted(toSort.keys())
sortedByValue = sorted(toSort.items(), key = lambda x: (-x[1], x[0]))

print(round(sum(inputList) / n))
print(inputList[(n-1) // 2])
if len(sortedByValue) > 1 and sortedByValue[0][1] == sortedByValue[1][1]:
    print(sortedByValue[1][0])
else:
    print(sortedByValue[0][0])
print(sortedByKey[-1] - sortedByKey[0])
