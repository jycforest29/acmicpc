import sys

s = sys.stdin.readline().strip()
for i in range(26):
    i = chr(97+i)
    if i in s:
        print(s.index(i), end = ' ')
    else:
        print(-1, end = ' ')