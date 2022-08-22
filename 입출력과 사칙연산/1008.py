## 배운점 
# 10*-9이하의 오차를 허용한다 -> 파이썬은 상관 없음. 
# c++의 경우 float과 %f대신 double과 %lf 사용해야

import sys

n, m = map(int, sys.stdin.readline().split())
print(n/m)