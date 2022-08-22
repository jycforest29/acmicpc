import sys

def dp(a, b, c):
    if min(a, b, c) <= 0:
        return 1
    else:
        if a < b and b < c:
            # return dp(aList[i], bList[i], cList[i-1])+dp(aList[i], bList[i-1], cList[i-1]) - dp(aList[i], bList[i-1], cList[i])
            return dp(a, b, c-1)+dp(a, b-1, c-1)-dp(a, b-1, c)
        else:
            # return dp(aList[i-1], bList[i], cList[i])+dp(aList[i-1], bList[i-1], cList[i])+dp(aList[i-1], bList[i], cList[i-1])-dp(aList[i-1], bList[i-1], cList[i-1])
            return dp(a-1, b, c)+dp(a-1, b-1, c)+dp(a-1, b, c-1)-dp(a-1, b-1, c-1)

a, b, c = map(int, sys.stdin.readline().split(' '))
inputs = []
while a != -1 or b!= -1 or c != -1:
    inputs.append([a, b, c])
    a, b, c = map(int, sys.stdin.readline().split(' '))

for i in inputs:
    if max(i[0], i[1], i[2]) > 20:
        print(f'w({a}, {b}, {c}) = '.format(20, 20, 20), dp(20, 20, 20))
    else:
        print(f'w({a}, {b}, {c}) ='.format(i[0], i[1], i[2]), dp(i[0], i[1], i[2]))
