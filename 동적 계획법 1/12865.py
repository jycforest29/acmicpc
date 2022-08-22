import sys

# limit이 정해져 있을 때 최대 val
# f(n, w) = max(f(n-1, w), f(n-1, w-w[n])+val[n])
# 변수 2개 -> 테이블 생성
