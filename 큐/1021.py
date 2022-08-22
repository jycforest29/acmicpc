## 코드 참고 여부
# https://velog.io/@goplanit/Algorithm-%EB%B0%B1%EC%A4%80-1021%EB%B2%88-%ED%9A%8C%EC%A0%84%ED%95%98%EB%8A%94-%ED%81%90%ED%8C%8C%EC%9D%B4%EC%8D%AC

## 슈도 코드
# count = 0
# inputs에 대해(이하 i)
    # 무한반복
        # 만약 deq의 첫 인덱스가 i와 같다면
            # 뽑아내고 break
        # 만약 i의 deq에서의 인덱스가 deq의 길이는 반을 나눈 것보다 작으면
            # deq[0] == i일때까지
                # deq에서 뽑은 값에 대해 2번연산
                # count += 1
        # 크거나 같으면
            # deq[0] == i일때까지
                # deq에서 뽑은 값에 대해 3번연산
                # count += 1

## 문제 풀이 방식
# 순서대로 뺀다고 생각

## 배운점 
# deq[0]처럼 deque도 인덱싱 가능

## 걸린 시간

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
inputs = list(map(int, sys.stdin.readline().split()))
deq = deque([i+1 for i in range(n)])
count = 0
j = 0

while True:
    # 맨 앞의 문자가 빼야할 수일때
    if deq[0] == inputs[j]:
        if j == m-1:
            print(count)
            break
        deq.popleft()
        j += 1
    else:
        count += 1
        # appendleft
        if deq.index(inputs[j]) > len(deq) // 2: # >=로 하면 틀림
            tmp = deq.pop()
            deq.appendleft(tmp)
        # append
        else: 
            tmp = deq.popleft()
            deq.append(tmp)
