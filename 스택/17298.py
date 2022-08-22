## 코드 참고 여부
# 시간초과로 참고함
    # https://velog.io/@tks7205/%EB%B0%B1%EC%A4%80-17298-%EC%98%A4%ED%81%B0%EC%88%98-Stack%EC%9C%BC%EB%A1%9C-%ED%92%80%EA%B8%B0

## 문제 풀이 방식
# 스택에 인덱스 삽입

## 슈도 코드
# res = [-1]*n
# 빈 스택 리스트 생성

# 스택 리스트에 0 추가
# [1, n-1]
    # stack이 존재하고 입력리스트의 인접한 두 원소를 비교했을 때 < 라면
        # res[stack의 가장 위에 있는 원소] = 입력리스트의 더 큰 원소
    # 스택에 현재 인덱스 추가
# res 출력

## 배운점 
# 길이가 n인 res 리스트를 처음에 -1로 초기화
# 리스트의 인접원소 비교는 스택에 인덱스를 넣는 방식으로 하기
# 스택을 임시리스트로 처리하면 >인 부분 알아서 가장 큰 값으로

## 걸린 시간

import sys

n = int(sys.stdin.readline())
input_ = list(map(int, sys.stdin.readline().split())) 
res = [-1]*n
stack = []

stack.append(0)
for i in range(1, n):
    while stack and input_[stack[-1]] < input_[i]: # 자동 인접원소 비교
        res[stack.pop()] = input_[i]
    stack.append(i)
print(*res, sep = ' ')