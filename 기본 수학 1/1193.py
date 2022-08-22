## 코드 참고 여부
# 애매함. 예전에 본 것 같은데 따로 기억나지는 않음.

## 문제 풀이 방식
# (/방향 대각선 줄 수)의 짝/홀수 여부에 따라 분자, 분모 순서가 바뀜
    # 짝수면 분자 = 1, 분모 = /방향 대각선 줄 수. 각각 +1, -1
    # 홀수면 반대

## 슈도 코드
# 분수 번호 입력받음(이하 x)
# 위에서 입력받은 분수번호가 있는 대각선에 도달할때까지 있는 분수 번호 개수를 저장할 변수 0으로 초기화(이하 sum)
# 위에서 입력받은 분수번호가 있는 대각선이 몇번째인지 저장할 변수 1로 초기화(이하 lineNum)
# 분수 번호가 sum보다 크고 sum+lineNum 보다 작거나 같은 범위에 있을때까지
    # sum += lineNum
    # lineNum += 1
# 만약 대각선 인덱스가 짝수일 경우
    # 1+대각선내 몇번째 인덱스인지 / lineNum-대각선내 몇번째 인덱스인지 출력
# 홀수일 경우
    # lineNum-대각선내 몇번째 인덱스인지/ 1+대각선내 몇번째 인덱스인지 출력

## 어려웠던 부분
# sum, lineNum 변수 초기화 하는 부분
# 무한루프안에서 sum += lineNum, lineNum += 1 순서
# 대각선내 몇번째 인덱스인지 구하는 부분

## 걸린시간

import sys

x = int(sys.stdin.readline())

sum = 0
lineNum = 1
while True:
    if sum < x <= sum + lineNum:
        break
    sum += lineNum
    lineNum += 1

if lineNum % 2 == 0:
    print('{1}/{0}'.format(lineNum-(x-sum-1), 1+x-sum-1))
else:
    print('{0}/{1}'.format(lineNum-(x-sum-1), 1+x-sum-1))