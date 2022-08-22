## 코드 참고 여부
# 혼자품

## 문제 풀이 방식
# 결국 생각나는 모든 경우의 수 고려함
 
## 슈도 코드
# 생략

## 배운점 

## 걸린 시간

import sys

n = int(sys.stdin.readline())
table = [[n]]
count = 0
while 1 not in table[-1]:
    tmp = []
    for i in table[-1]:
        if i % 3 == 0:
            tmp.append(i // 3)
        if i % 2 == 0:
            tmp.append(i // 2)
        tmp.append(i-1)
    table.append(tmp)
    count += 1
print(count)