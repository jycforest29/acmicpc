import sys

def f(n, m, count, res):
    if count == 1:
        pass

input = sys.stdin.readline()
n, m = map(int, input.split())

# 중복 없이 m개
res = [] # 재귀적으로 도출한 결과를 담을 배열
count = 0 # 
f(n, m, count, res)