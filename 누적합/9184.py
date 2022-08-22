import sys

def dp(a, b, c):
    if min(a, b, c) <= 0:
        return 1
    if max(a, b, c) > 20:
        return dp(20, 20, 20)
    if table[a][b][c] == -9999999:
        if a < b and b < c:
            table[a][b][c] = dp(a, b, c-1)+dp(a, b-1, c-1)-dp(a, b-1, c)
            return table[a][b][c]
        table[a][b][c] = dp(a-1, b, c)+dp(a-1, b-1, c)+dp(a-1, b, c-1)-dp(a-1, b-1, c-1)
    return table[a][b][c]

a, b, c = map(int, sys.stdin.readline().split(' '))

# 3차원 리스트
table = [[[-9999999 for i in range(21) ]for j in range(21)] for k in range(21)]
inputs = []
while a != -1 or b!= -1 or c != -1:
    inputs.append([a, b, c])
    # table 리스트에 a, b, c값 저장
    a, b, c = map(int, sys.stdin.readline().split(' '))

for i in inputs:
    print('w({}, {}, {}) = {}'.format(i[0], i[1], i[2], dp(i[0], i[1], i[2])))