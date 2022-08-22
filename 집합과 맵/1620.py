## 코드 참고 여부
# 혼자품

## 문제 풀이 방식
# 포켓몬 도감이므로 딕셔너리로 풀 수 있음
# 포켓몬 도감 입력받을 때 대문자가 끝에있을 경우만 맨앞에 대문자, 끝에 소문자가 오도록 바꿔서 저장하면 될듯
 
## 슈도 코드
# n, m 입력
# 딕셔너리 생성
# 반대 딕셔너리 생성(위의 딕셔너리에 대해 key와 value를 각각 value와 key로 저장) - 이 문제에서는 key와 value가 1:1이기 때문에 가능
# index = 1
# n 동안
    # 딕셔너리의 키로 입력 문자열 저장
    # 딕셔너리의 값으로 index 저장
    # index += 1
# m 동안
    # key에 존재할 경우
        # 딕셔너리[입력값] 출력
    # 존재하지 않을 경우
        # 반대딕셔너리[입력값] 출력

## 배운점
# 일부 포켓몬은 마지막 문자만 대문자일 수 있다는걸 어떻게 처리해야할지?
# 딕셔너리에서 value를 알때 key 출력(key와 value는 1:1)
# sys.stdin.readline().split()은 항상 list 따라서 문자열 입력시에는 개행문자 제거를 위해 .rstrip()

## 걸린 시간

import sys

n, m = map(int, sys.stdin.readline().split())
inputList = dict()
inputReverse = dict()
result = []
index = 1
for i in range(n):
    tmp = sys.stdin.readline().rstrip()
    inputList[tmp] = index
    inputReverse[index] = tmp
    index += 1
    
for i in range(m):
    tmp = sys.stdin.readline().rstrip()
    if tmp in inputList.keys():
        result.append(inputList[tmp])
        continue
    result.append(inputReverse[int(tmp)])

for i in result:
    print(i)
    

