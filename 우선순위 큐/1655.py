import sys
import heapq

n = int(sys.stdin.readline())
# 특정 값보다 작은 값들을 모아놓은 최대힙
maxres = []
# 특정 값보다 큰 값들을 모아놓은 최소힙
minres = []

heapq.heappush(maxres, -int(sys.stdin.readline()))

for i in range(n-1):
    # 특정값은 최대힙에서 pop한 값으로 생각해야
    tmp = -heapq.heappop(maxres)
    input = int(sys.stdin.readline())
    if tmp < input:
        heapq.heappush(minres, input)
    else:
        heapq.heappush(maxres, -input)
    heapq.heappush(maxres, -tmp)

    # 항상 최대힙의 개수가 1개 많거나 같게
    if len(maxres)<len(minres): # 반복적으로 계속 확인하므로 이 조건을 만족할 경우는 +1뿐. -> 같게 만들어줌
        heapq.heappush(maxres, -heapq.heappop(minres))
    elif len(maxres)>len(minres)+1: # maxres가 minres보다 2개 이상 많을 경우임. 이 역시 반복적으로 계속 확인하므로 이 조건을 만족할 경우는 +1뿐. -> 1개 많게 만들어줌.
        heapq.heappush(minres, -heapq.heappop(maxres))

    # 항상 최대힙에서 pop한 수가 정답임
    res=heapq.heappop(maxres)
    print(-res)
    heapq.heappush(maxres, res)
    