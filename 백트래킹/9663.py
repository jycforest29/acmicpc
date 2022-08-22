import sys

def f(inputs, n, i):
    count = 0

    for i in range(n):
        for j in range(n):
            inputs[i]
    return count

n = int(sys.stdin.readline())
inputs = [[1 for i in range(n)] for i in range(n)]
count = []

for i in range(n):
    count.append(f(inputs, n, i))

print(max(count))