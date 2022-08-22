# 풀이 참고함
import sys

n = int(sys.stdin.readline())
inputs = [0]
for _ in range(n):
    inputs.append(int(sys.stdin.readline())) 

if n == 1:
    print(inputs[1])
else:
    dp = [0]*(n+1) # 왜 n개의 배열일까?
    dp[1] = inputs[1]
    dp[2] = inputs[1]+inputs[2]
    for i in range(3, n+1): # 왜 3부터 시작하지?
        dp[i] = max(dp[i-3]+inputs[i]+inputs[i-1], dp[i-2]+inputs[i])
    
    print(dp[n])