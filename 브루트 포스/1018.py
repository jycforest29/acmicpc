## 코드 참고 여부
# 혼자품

## 문제 풀이 방식
# 가로방향-> 세로방향으로(반대도 가능) 번갈아가면서 나오지 않는 개수를 저장하고 그 중 최소 리턴
 
## 슈도 코드
# n, m 입력받음
# 전체 리스트 입력받음
# res = []
# [0, m-8] 이하 i
    # [0, n-8] 이하 j
        # start = 전체 리스트[i][j]
        # count = 0
        # [i, i+8]
            # [j, j+8]
                # if i == 0 and j == 0:
                    # pass
                # start가 B이고 i+j가 짝수일 때 전체 리스트[i][j] == W 라면
                    # count += 1
                # start가 B이고 i+j가 홀수일 때 전체 리스트[i][j] == B 라면
                    # count += 1
                # start가 W이고 i+j가 짝수일 때 전체 리스트[i][j] == B 라면
                    # count += 1
                # start가 W이고 i+j가 홀수일 때 전체 리스트[i][j] == W 라면
                    # count += 1
        # res.append(count)
# min(res)

## 배운점 

## 걸린 시간

import sys

n, m = map(int, sys.stdin.readline().split())
tmp = []
for i in range(n):
    tmp.append(sys.stdin.readline().strip())

startList = ['B', 'W']
res = []

for start in startList:
    for i in range(n-8+1):
        for j in range(m-8+1):
            count = 0
            for k in range(i, i+8):
                for l in range(j, j+8):
                    if k == i and l == j:
                        pass
                    if (i+j)%2 == 0:
                        if (k+l) % 2 == 0 and tmp[k][l] != start:
                            count += 1
                        if (k+l) % 2 == 1 and tmp[k][l] == start:
                            count += 1
                    else:
                        if (k+l) % 2 == 0 and tmp[k][l] == start:
                            count += 1
                        if (k+l) % 2 == 1 and tmp[k][l] !=start:
                            count += 1
            res.append(count)
print(min(res))
