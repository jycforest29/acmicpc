import sys
import heapq

n = int(sys.stdin.readline())
res = []
res_ = []
for i in range(n):
    m = int(sys.stdin.readline())
    if m == 0:
        # 최소값 출력 후 제거
        if len(res_) > 0 and len(res) > 0:
            tmp = heapq.heappop(res)
            tmp_ = heapq.heappop(res_)
            # 둘 다 무조건 양수
            if tmp < tmp_:
                print(tmp)
                heapq.heappush(res_, tmp_)
            else:
                print(-tmp_)
                heapq.heappush(res, tmp)
        elif len(res_) > 0 and len(res) == 0:
            print(-heapq.heappop(res_))
        elif len(res_) == 0 and len(res) > 0:
            print(heapq.heappop(res))
        else:
            print(0)
    else:
        # 양/음수 따지기
        if m < 0:
            heapq.heappush(res_, -m)
        else:
            heapq.heappush(res, m)