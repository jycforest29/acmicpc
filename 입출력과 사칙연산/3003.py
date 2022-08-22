## 배운점 
# 리스트 안 쓰고 풀 수 있음

import sys

inputs = list(map(int, sys.stdin.readline().split()))
ans = [1, 1, 2, 2, 2, 8]
print(*list(ans[i]-inputs[i] for i in range(6)), sep = ' ')