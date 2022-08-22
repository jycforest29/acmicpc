# 연속된 2개 합치기.
import sys

t = int(sys.stdin.readline())
for i in range(t):
    k = int(sys.stdin.readline())
    kList = list(map(int, sys.stdin.readline().split()))

    dp = [0 for i in range(k)]
    for i in range(1, k): # 총 k-1개
        dp[i]