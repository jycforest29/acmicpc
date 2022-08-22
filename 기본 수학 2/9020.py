## 코드 참고 여부
# 혼자품

## 문제 풀이 방식
# 합이 n이 되는 두 수의 모든 경우를 찾아야 함. 이때 대칭성이용.
#   짝수 - (2, n-2) /,,,/ (n/2, n/2)
# 각 경우에 대해 모두 소수인지를 체크하고 두 수 모두 소수면 소수인 것들끼리 모아 차이가 최소인 것을 출력해야
 
## 슈도 코드
# t 입력받음
# t의 범위동안
    # 새로운 리스트 생성 후 (2, n-2) /,,,/ (n/2, n/2)까지 모든 경우의 수를 리스트에 담기
    # 리스트 원소의 쌍이 모두 소수인지 확인
        # 모두 소수일 경우 절댓값을 통해 차이가 가장 작은 수 출력

## 어려웠던 부분
# check.sort(key = lambda x: abs(x[0] - x[1]))[0]로 할 경우 None이 반환됨.

## 걸린 시간
# 26분

import sys

def f(num):
    if num == 1:
        return True
    for i in range(2, int(num**(1/2))+1):
        if num % i == 0:
            return True
    return False

inputList = []
table = []
for i in range(4, 10001):
    if f(i) == False:
        table.append(i)

t = int(sys.stdin.readline())

for i in range(t):
    inputList.append(int(sys.stdin.readline()))

for i in inputList:
    tmp = []
    check = []
    for j in range(2, i // 2+1):
        tmp.append([j, i - j])
    for n, m in tmp:
        if n in table and m in table:
            check.append([n, m])
    result = sorted(check, key = lambda x: abs(x[0] - x[1]))[0]
    print('{0} {1}'.format(result[0], result[1]))