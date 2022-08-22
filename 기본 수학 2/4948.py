## 코드 참고 여부
# pypy - pypy로 해야한다는 답변글 참고
# python3 - https://velog.io/@iillyy/%EB%B0%B1%EC%A4%80-4948%EB%B2%88-%ED%8C%8C%EC%9D%B4%EC%8D%AC

## 문제 풀이 방식
# 제곱근을 통해 소수 구하는 코드로 품
 
## 슈도 코드
# n을 담을 리스트 생성
# 소수의 개수를 담을 리스트 생성
# n 입력받음
# n이 0이 아닐때까지
    # 리스트에 n 추가
    # n 입력받음

# n 리스트의 각 원소에 대해
    # 소수 확인하는 함수 호출

# 개수 리스트의 원소 출력 

## 어려웠던 부분
# n+1부터 2*n까지의 모든 range안에 속하는 수를 하나씩 체크하는 방식은 python3에서는 시간초과남. pypy로 제출했더니 통과함.
    # pypy는 python3보다 메모리를 더 많이 사용하는 대신 시간을 더 적게 사용함. 
    # 내 풀이는 메모리는 nList*2만큼 사용하기 때문에 최대 123456*2kb이므로 pypy로 가능했던 듯.
# python3로 풀기 위해서는 2부터 123456*2까지를 먼저 소수체크 후 리스트에 저장하고, n+1부터 2*n까지의 수가 해당 리스트에 있는지 확인하는 방식으로
# 해야 연산량을 줄일 수 있을듯.(풀이참고)

## 걸린 시간
# 대략 30분

import sys

def f(num):
    if num == 1:
        return True
    for i in range(2, int(num**(1/2))+1):
        if num % i == 0:
            return True
    return False

nList = []
countList = []
table = []
for i in range(2, 2*123456+1):
    if f(i) == False:
        table.append(i)

n = int(sys.stdin.readline())

while n != 0:
    nList.append(n)
    n = int(sys.stdin.readline())

for i in range(len(nList)):
    tmp = 0
    for j in table:
        if nList[i]+1 <= j <= 2*nList[i]:
            tmp += 1
    countList.append(tmp)

for i in countList:
    print(i)