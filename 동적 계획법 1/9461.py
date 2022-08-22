import sys

def dp(input_):
    tmp = [1, 1, 1]
    for i in range(3, input_):
        tmp.append(tmp[i-2]+tmp[i-3])
    return tmp[input_-1]

n = int(sys.stdin.readline())
inputList = []
for i in range(n):
    inputList.append(int(sys.stdin.readline()))
for i in range(n):
    print(dp(inputList[i]))
