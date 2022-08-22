## 코드 참고 여부
# 스터디원 풀이 참고함
# 추가로 https://jokerldg.github.io/algorithm/2021/03/11/meeting-room.html

## 문제 풀이 방식
# 가장 텀이 짧은걸로
 
## 슈도 코드
# n 입력받음
# # n 동안
    # 회의리스트 입력받음
# 회의리스트를 회의 끝나는 시간이 빠른 것 , 회의시작이 빠른것 기준으로 정렬
# count 변수 = 0
# -------------------------여기부터 풀이 참고해 수도코드 작성------------------------
# 회의 마지막 시간 저장할 변수 before 생성 및 0으로 초기화
# 정렬한 회의 리스트에 대해
    # 만약 회의 리스트의 회의 시작 >= before
        # count += 1
        # before = 회의 리스트의 회의 끝나는 시간

## 배운점 
# DP 문제의 종류
# before 변수 사용
# 왜 끝나는 시간이 빠른것 먼저 우선순위로 두고 정렬해야 하는지

## 걸린 시간
# 1시간 30분

import sys

n = int(sys.stdin.readline())
tmp = []
for i in range(n):
    tmp.append(list(map(int, sys.stdin.readline().split())))

tmp.sort(key = lambda x: (x[1], x[0]))
count = 0
before = 0

for i in tmp:
    if i[0] >= before:
        count += 1
        before = i[1]

print(count)

# -------------------------이 부분 왜 안됐는지 확인------------------------
# i = 0
# x = [i[0] for i in tmp]
# while True:
#     if i >= n-1:
#         print(before)
#         if before <= tmp[i][0]:
#             print(count + 1)
#         else:
#             print(count)
#         break
#     # 간격이 더 짧을 때
#     if tmp[i][1] <= tmp[i+1][1]:
#         if tmp[i][1] in x:
#             i = x.index(tmp[i][1])
#         else:
#             while tmp[i][1] not in x:
#                 tmp[i][1] += 1
#             i = x.index(tmp[i][1])
#         before = tmp[i][1]
#         count += 1
#     else:
#         i += 1

