## 코드 참고 여부
# 예전에 봤던 풀이 참고 외에
# https://velog.io/@jihun333/%EB%B0%B1%EC%A4%802477-%EC%B0%B8%EC%99%B8%EB%B0%AD-%EC%9E%90%EB%B0%94
# https://velog.io/@holawan/%EB%B0%B1%EC%A4%80-2477%EC%B0%B8%EC%99%B8%EB%B0%AD-python

## 문제 풀이 방식
# 가장 긴 가로 양 옆의 세로 2개의 차이가 뺄 직사각형의 세로
# [50, 30, 20]
# 가장 긴 세로 양 옆의 가로 2개의 차이가 뺄 직사각형의 가로
# [160, 60, 100]
# [50, 160, 30, 60, 20, 100]
 
## 슈도 코드

## 배운점

## 걸린 시간

import sys

k = int(sys.stdin.readline())
row = []
col = []
all = []
for i in range(6):
    a, b = map(int, sys.stdin.readline().split())
    if a == 3 or a == 4:
        col.append(b)
    else:
        row.append(b)
    all.append(b)
colMax = max(col)
rowMax = max(row)

max_ = colMax*rowMax
colIndex = all.index(colMax)
rowIndex = all.index(rowMax)

colSub = all[colIndex-1]
if all[colIndex+1]:
    colSub_ = all[colIndex+1]
else:
    colSub_ = all[colIndex-5]
rowSub = all[rowIndex-1]
if all[rowIndex+1]:
    rowSub_ = all[rowIndex+1]
else:
    rowSub_ = all[rowIndex-5]
min_ = abs(colSub-colSub_)*abs(rowSub-rowSub_)
print(k*(max_-min_))