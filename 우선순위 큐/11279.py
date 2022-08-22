import sys
import heapq

n = int(sys.stdin.readline())
res = []
res_ = []
for i in range(n):
    m = int(sys.stdin.readline())
    if m == 0:
        if len(res) == 0:
            print('0', 0)
        else:
            # 가장 작은 값 출력 후 제거 
            print('0', heapq.heappop(res))
    else:
        if m < 0:
            heapq.heappush(res_, m)
        else:
            heapq.heappush(res, m)