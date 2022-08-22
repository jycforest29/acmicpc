import sys

def dp(n):
    tmp = [1, 1]
    for i in range(2, n):
        tmp.append(tmp[i-1]+tmp[i-2])
    return tmp[n-1]
    
n = int(sys.stdin.readline())

print(dp(n), end = ' ')
print(n-2)