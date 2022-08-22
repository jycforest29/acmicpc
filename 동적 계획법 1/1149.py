## 코드 참고 여부
# 틀려서 참고함
    # https://velog.io/@wjdtmdgml/%EB%B0%B1%EC%A4%80RGB%EA%B1%B0%EB%A6%AC1149%EB%B2%88Python%ED%8C%8C%EC%9D%B4%EC%8D%ACDP

## 문제 풀이 방식
# 모든 줄에 대해 그 줄의 0번째를 칠했을 때, 1번째를 칠했을 때, 2번째를 칠했을 때
# 최소합을 각각 구해야
 
## 슈도 코드
# [1, n-1]
    # 입력리스트[i][0] = i-1번째에 1이나 2번째 색 선택했을 때 최소+i번째에 0번째 선택한 값

## 배운점 
# 가장 첫번째 줄이 최소일 때 정답이라는 보장 없음. 따라서 이렇게 때려맞추지 말고
# 논리적으로 풀어야 함
# 따라서 아래 풀이에서는 모든 줄에 대해
# 0, 1, 2번째를 기준으로 잡았을 때 최소합을 각각 구해 거기서 또 최소를 구함

## 걸린 시간

import sys

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, n):
    arr[i][0] = arr[i][0]+min(arr[i-1][1], arr[i-1][2])
    arr[i][1] = arr[i][1]+min(arr[i-1][0], arr[i-1][2])
    arr[i][2] = arr[i][2]+min(arr[i-1][0], arr[i-1][1])

print(min(arr[i]))