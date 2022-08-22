# 오름차순 정렬
# 인덱스 1부터 시작
# 어떻게 이진탐색을 적용할지가 관건인 문제

# a[1][1] a[1][2] a[1][3] a[1][4]
# a[2][1] a[2][2] a[2][3] a[2][4]
# a[3][1] a[3][2] a[3][3] a[3][4]
# a[4][1] a[4][2] a[4][3] a[4][4]

import sys

def f(s, e, k):
    if s - e <= 1:
        return s

n = int(sys.stdin.readline())
m = int(sys.stdin.readline()) # m-1이 인덱스

f(1, n*n+1, m)