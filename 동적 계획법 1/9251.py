# 최장 공통 부분 수열과 최장 공통 문자열은 다름
import sys

arr1 = sys.stdin.readline().strip()
arr2 = sys.stdin.readline().strip()

dp = [[0 for i in range(len(arr1))] for i in range(len(arr2))]
for i in range(len(arr2)):
    for j in range(len(arr1)):
        if arr2[i] == arr1[j]:
            dp[i][j] = dp[i-1][j-1]+1
            if i == 0 or j == 0:
                dp[i][j] = 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

# print(dp)
print(dp[-1][-1])