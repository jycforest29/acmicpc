## 코드 참고 여부
# 계속 시간초과나서 질문글 참고함

## 문제 풀이 방식
 
## 슈도 코드

## 배운점
# 어디서 리스트 써야하고 어디서 큐를 써야하는지 모르겠음. 아니 일단 리스트를 쓰는게 맞나?
# <list>
# len(list) O(1)
# list[i]   O(1)
# append()  O(1)
# pop()     O(1)
# pop(0)    O(N)
# del list[i] O(N)
# sort()    O(NlogN)
# -> 리스트가 큐 연산에 불리한 이유

## 걸린 시간

import sys
from collections import deque

t = int(sys.stdin.readline())
for i in range(t):
    p = deque(sys.stdin.readline().strip())
    n = int(sys.stdin.readline())
    inputs = sys.stdin.readline().strip()

    # inputs을 deque에 집어넣기
    tmp = inputs.replace('[', '')
    tmp = tmp.replace(']', '')
    tmp = tmp.split(',')
    queue = deque(tmp)

    # error인지 확인할 변수
    check = True

    if queue == deque(['']):
        queue = deque()
    reverse = False
    # O(1) * 10만
    while len(p) > 0:
        i = p.popleft()
        if i == 'R':
            reverse = not reverse
            continue
        if len(queue) > 0:
            if reverse:
                queue.pop()
            else:
                queue.popleft()
            continue
        # i가 D인데 len(queue)가 0인 경우
        check = False
        break

    # 출력
    if check == False: 
        print('error')
        continue
    if reverse == True:
        queue.reverse()
    print('[', end = '')
    print(*queue, sep = ',', end=']\n')
