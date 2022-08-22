## 코드 참고 여부
# 시간초과나와서 참고함
    # https://dojinkimm.github.io/problem_solving/2019/10/21/boj-1912-continuous-sum.html

## 문제 풀이 방식
# 누적합 과정 중 비교 연산 사용
 
## 슈도 코드
# 크기가 n인 배열 생성
# 위 배열의 첫번째 원소를 입력리스트의 첫번째 원소로 대입
# [1, n-1]
    # 배열[i] = 입력리스트[i]나 입력리스트[i]+배열[i-1]
# 배열 중 최대값 출력

## 배운점 
# 아예 DP로 풀어야 함

## 걸린 시간

import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
table = [0]*n
table[0] = arr[0]
for i in range(1, n):
    table[i] = max(arr[i], arr[i]+table[i-1])
print(max(table))