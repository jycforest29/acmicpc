## 코드 참고 여부
# 틀려서 참고함
    # https://velog.io/@kgpaper/%EB%B0%B1%EC%A4%80-9375%EB%B2%88-%ED%8C%A8%EC%85%98%EC%99%95-%EC%8B%A0%ED%98%9C%EB%B9%88

## 문제 풀이 방식
# 딕셔너리[종류] = 가짓수(하루에 한 종류에서는 하나만 선택 가능하므로 조합 대신 딕셔너리 value로 계산)

# 이게 원래 풀이였는데 이런식으로 하면 항상 인접한 곳끼리만 곱해짐
# keys = list(tmp.keys())
# values = list(tmp.values())
# count = 0
# for i in range(len(keys)): # [0, n-1] 몇 종류의 옷을 입을지()
#     sum = 0
#     # i+1 종류의 옷을 입을 경우(1종류, 2종류)
#     for j in range(len(keys)-i): # [0, n-1] values에서 i만큼 묶어서 곱할때 values의 시작 위치
#         mul = 1
#         for k in range(j, j+i+1): # 실제로 곱함
#             mul *= values[k]
#         sum += mul
#     count += sum
# result.append(count)
 
## 슈도 코드
# t 입력받음
# t 동안
    # 딕셔너리 생성
    # n 입력받음
    # n 동안
        # 딕셔너리[key] = value
    # mul = 1
    # 딕셔너리 key의 개수동안(이하 i)
        # mul *= (value+1)
    # 모두 선택하지 않은 1가지를 뺀 mul-1 출력
        
## 배운점

## 걸린 시간

import sys

t = int(sys.stdin.readline())
result = []

for i in range(t):
    tmp = dict()
    n = int(sys.stdin.readline())
    for i in range(n):
        key = sys.stdin.readline().split()[1]
        if key in tmp.keys():
            tmp[key] += 1
            continue
        tmp[key] = 1
    
    keys = list(tmp.keys())
    values = list(tmp.values())
    count = 1
    for i in range(len(keys)): # [0, n-1] 몇 종류의 옷을 입을지()
        count *= values[i]+1
    result.append(count-1)

for i in result:
    print(i)