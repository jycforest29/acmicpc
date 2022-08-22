## 코드 참고 여부
# 재귀 세우는게 감이 안잡힘
    # https://velog.io/@real_jun9u/%EB%B0%B1%EC%A4%80%ED%8C%8C%EC%9D%B4%EC%8D%AC-11729%EB%B2%88-%ED%95%98%EB%85%B8%EC%9D%B4-%ED%83%91-%EC%9D%B4%EB%8F%99-%EC%88%9C%EC%84%9C

## 문제 풀이 방식
# hanoi(남은 원판 개수, 시작, 경유, 끝)
# 우선 n-1개를 b번 원판에 갖다놓고
# a번에 있는 원판 1개를 c번에 갖다 놓은 다음
# b번의 n-1개를 c번에 갖다 놓으면 됨

## 슈도 코드
# 하노이 함수(남은 원판 개수, 시작, 경유, 끝)
    # 만약 남은 원판 개수 1일 경우
        # 시작, 끝 출력
    # 아닐 경우
        # 하노이 함수(남은 원판 개수-1, 시작, 끝, 경유)
        # 시작 위치에 남은 원판 하나 옮김
        # 하노이 함수(남은 원판 개수-1, 경유, 시작, 끝)
# n 입력받음
# 2**n - 1로 횟수 출력
# 하노이 함수(n, 1, 2, 3)

## 어려웠던 부분

## 걸린 시간

import sys

def hanoi(n, a, b, c):
    if n == 1:
        print(a, c)
    else:
        hanoi(n-1, a, c, b)
        print(a, c)
        hanoi(n-1, b, a, c)

n = int(sys.stdin.readline())
print(2**n - 1)
hanoi(n, 1, 2, 3)