# arr is rvs -> False
import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
rvs = arr[::-1]

s = [1]*n
e = [1]*n

for i in range(0, n):
    for j in range(0, i):
        if arr[j] < arr[i]:
           s[i] = max(s[i], s[j]+1)
        if rvs[j] < rvs[i]:
           e[i] = max(e[i], e[j]+1)

res = [0]*n
for i in range(n):
    res[i] = s[i]+e[n-1-i]-1

print(max(res))
