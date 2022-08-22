import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
for i in range(3):
    print(n*((m//(10**i))%10))
print(n*m)