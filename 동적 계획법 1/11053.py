# 탐색 범위 지정이 어려웠음.
# 질문글의 풀이 참고함.
import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

dp = [1]*n
for i in range(n):
    for j in range(0, i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j]+1) # 이 부분이 핵심

print(max(dp))
