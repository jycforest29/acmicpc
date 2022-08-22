## 코드 참고 여부
# 혼자품

## 문제 풀이 방식
# 특정 지점에서 0이 나왔을 때 얼마나 0이 지속되느냐가 핵심
 
## 슈도 코드
# n 입력받음
# n! 구한 후 리스트에 역순으로 저장
# count = 0
# 만약 역순 리스트에 '0'이 존재할 경우
    # count + 1
    # ['0'이 처음 등장하는 위치+1, 역순 리스트의 길이-1]
        # '0'이 아니면
            # break
        # '0'이면
            # count + 1
# 존재하지 않을 경우
    # count(즉 0) 출력

## 배운점

## 걸린 시간

import sys
from math import factorial

def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1)

n = int(sys.stdin.readline())
tmp = list(str(factorial(n)))[::-1]
count = 0
if '0' in tmp:
    count += 1
    start = tmp.index('0')
    for i in range(start+1, len(tmp)):
        if tmp[i] != '0':
            break
        count += 1
print(count)