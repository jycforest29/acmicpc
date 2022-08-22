## 코드 참고 여부
# 혼자품

## 문제 풀이 방식
# [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]]
# (2, 2)부터 (3, 4) -> [1, 1]부터 [2, 3] -> [1, 1]+[1, 2]+[1, 3]+[2, 1]+[2, 2]+[2, 3]
 
## 슈도 코드
# n, m 입력받음
# n*n 리스트 생성
# n*n 리스트 입력받음
# [0, n*n-1]에 대해 누적합 구하기
# m동안
    # x, y, x_, y_ 입력받음
    # 인덱스 = (x_-1)*n+y_-1
    # x와 x_, y와 y_이 같을 경우
        # 입력리스트[인덱스] 출력
    # 다를 경우
        # 인덱스-1 <0 일 경우
            # n*n 리스트[인덱스] 출력
        # 아닐 경우
            # n*n 리스트[인덱스]-n*n 리스트[인덱스-1] 출력
            # 이중리스트이므로 추가로 사각형을 단위로 해서 빼줘야함

## 배운점
# 이중리스트일때 어떻게 대처할지

## 걸린 시간

import sys

def solve(r1, c1, r2, c2):
    
    return ps[r2][c2]-ps[r1-1][c2]-ps[r2][c1-1]+ps[r1-1][c1-1]

n, m = map(int, sys.stdin.readline().split())
data = []

for i in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))

ps = [[0 for i in range(n+1)] for j in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        ps[i][j] = ps[i][j-1]+ps[i-1][j]-ps[i-1][j-1]+data[i-1][j-1]

for i in range(m):
    r1, c1, r2, c2 = map(int, sys.stdin.readline().split())
    print(solve(r1, c1, r2, c2))


    
# sums = []

# for i in range(m):
#     x, y, x_, y_ = map(int, sys.stdin.readline().split())
#     sum_ = 0
#     if x==x_ and y == y_:
#         sum_ = inputList[x-1][y-1]
#     else:
#         if y<= 1: # y = 1 일때 -1이 나올 수 있음
#             if x == 1:
#                 sum_ = tmp[x_-1][y_-1]
#             else:
#                 sum_ = tmp[x_-1][y_-1]-tmp[x-2][y-2]
#         else:
#             sum_ = tmp[x_-1][y_-1] - tmp[x-1][y-2]
#             for j in range(x, x_):
#                 for k in range(y-1): 
#                     sum_ -= inputList[j][k]
#     sums.append(sum_)
# for i in sums:
#     print(i)