## 코드 참고 여부
# 잘 모르겠어서 참고함
# https://velog.io/@learningssik/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B0%B1%EC%A4%80-10986-%ED%8C%8C%EC%9D%B4%EC%8D%AC 참고

## 문제 풀이 방식
# 가능한 나머지의 종류는 0부터 m-1까지만 나올 수 있음. 
# 따라서 각 나머지의 종류를 구해서 각 몇번 나오는지 확인하면 됨.
 
## 슈도 코드
# n, m 입력받음
# An개 입력받음
# 인덱스로 나머지 종류를 저장할 리스트 생성(이하 mList)
# 0부터 n-1까지
    # 누적합 % m를 인덱스로 갖는 mList값을 찾아 + 1
# 0부터 n-1까지 
    # 각 나머지의 종류가 몇번 나오는지 

## 배운점 
# mList[0] = 1 왜 나누어 떨어질때는 1로 넣고 시작하지? 
# 순서쌍 만족?
# for i in mList:
    # count += i*(i-1) // 2
# m <= 1000

## 걸린 시간

import sys
n,m = map(int, sys.stdin.readline().split())
aList = list(map(int, sys.stdin.readline().split()))

mList = [0 for i in range(m)]
sum = 0
mList[0] = 1

for i in range(n):
    sum += aList[i]
    # 누적합의 나머지 종류별 개수 구하기
    mList[sum % m] += 1

count = 0
for i in mList:
    count += i*(i-1) // 2
print(count)
# -------------------------이 부분 왜 안됐는지 확인------------------------
# import sys

# n,m = map(int, sys.stdin.readline().split())
# aList = list(map(int, sys.stdin.readline().split()))
# tmp = [[0 for j in range(n-i)] for i in range(n)]
# tmp[0][0] = aList[0]

# for i in range(n):
#     sum = 0
#     for j in range(n-i):
#         sum += aList[j]
#         if (j+1) % (i+1) == 0:
#             tmp[i][j] = sum

#     print(tmp)