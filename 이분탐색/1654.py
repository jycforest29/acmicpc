## 배운점 
# 파라메트릭 서치는 최적화 문제(기준에 따라 최적의 값 구하는 문제. 예: f(i) = 1이 되는 i의 최솟값 구해라)
# -> 결정 문제(예: 어떤 i에서 f(i) = 1인가?에 대해 예, 아니오 가능)로 바꿀 수 있음
    # 특정 조건이 전제되어야 적용 가능

import sys

def f(start, end, kList, n):
    # start 유일함
    if end - start <= 1:
        return start
    mid = (start+end) // 2
    count = 0
    for i in kList:
        count += i // mid
    # count가 n개에 가장 근접했을 때 return
    if count >= n:
        return f(mid, end, kList, n)
    elif count < n:
        return f(start, mid-1, kList, n)

k, n = map(int, sys.stdin.readline().split())
kList = []
for _ in range(k):
    kList.append(int(sys.stdin.readline()))

print(f(1, max(kList), kList, n)) # start, end를 포함, 비포함으로 범위 설정하면 사소한 확인을 안 해도 됨.