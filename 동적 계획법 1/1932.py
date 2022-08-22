## 코드 참고 여부
# 혼자품

## 문제 풀이 방식
# 앞 문제와 비슷함. 
# 따라서 앞에서부터 더해가며 모든 경우의 수 고려. 
# 인덱스에 따른 예외처리만 제대로 해주면 될 듯.
 
## 슈도 코드
# 생략

## 배운점 
# 모든 경우의 수 처리하는 DP 설계

## 걸린 시간

import sys

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            arr[i][j] += arr[i-1][j]
        elif j == i:
            arr[i][j] += arr[i-1][j-1]
        else:
            arr[i][j] += max(arr[i-1][j], arr[i-1][j-1])
print(max(arr[n-1]))