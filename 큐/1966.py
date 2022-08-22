## 배운점 
# 여기서 len(deq)말고 n으로 하면 안됨
# if m == 0:
#     m = len(deq)-1
# else:
#     m -= 1

from collections import deque
import sys

t = int(sys.stdin.readline())

for i in range(t):
    n, m = map(int, sys.stdin.readline().split())
    tmp = list(map(int, sys.stdin.readline().split()))
    deq = deque(tmp)
    count = 0
    
    while len(deq) > 0:
        # print(deq, m)
        maxTmp = max(deq)
        popped = deq.popleft()
        # deq의 맨 앞에 deq 중 가장 큰 수가 있으면
        if popped == maxTmp:
            count += 1
            # 1 1 9 1 1 1 같은 경우 대비
            if m == 0:
                print(count)
                break
        # 없으면 deq의 끝에 추가
        else:
            deq.append(popped)
        if m == 0:
            m = len(deq)-1
        else:
            m -= 1

