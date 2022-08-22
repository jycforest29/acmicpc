import sys
import heapq

n = int(sys.stdin.readline())
res = []
for i in range(n):
    m = int(sys.stdin.readline())
    if m == 0:
        if len(res) == 0:
            print(0)
        else:
            # 가장  값 출력 후 제거 
            print(heapq.heappop(res))
    else:
        heapq.heappush(res, m)