from bisect import bisect_left
import sys

def f(res, i, inputs):
    s = 0
    e = len(inputs)
    if e - s <= 1:
        return s
    mid = (e+s) // 2
    if res[mid] == i:
        return mid
    elif res[mid] < i:
        return mid-1
    else:
        return mid+1

n = int(sys.stdin.readline())
inputs = list(map(int, sys.stdin.readline().split()))
# f(0, len(inputs), inputs, [inputs[0]])

res = [inputs[0]]
for i in inputs:
    if res[-1] < i:
        res.append(i)
    else:
        idx = f(res, i, inputs)
        res[idx] = i
    
print(res)