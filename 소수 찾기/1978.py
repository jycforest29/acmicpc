def check(n):
    for i in range(3, n, 2):
        if n % i == 0:
            return True
    return False

n = int(input())
tmp = list(map(int, input().split(' ')))
count = 0

for i in range(len(tmp)):
    if tmp[i]%2 == 0:
        if tmp[i] == 2:
            count += 1
    else:
        if tmp[i] == 1:
            pass
        else:
            # 짝수도 아니고 1도 아닌 수 중 소수에 해당하는지 체크
            if check(tmp[i]) == False:
                count += 1

print(count)
# ----------------------------------------------
import math

def check(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return True
    return False

n = int(input())
tmp = list(map(int, input().split(' ')))
count = 0

for i in range(len(tmp)):
    if tmp[i] != 1:
        if check(tmp[i]) == False:
            count += 1

print(count)

# 배울점
# 분기를 최대한 줄이는 게 깔끔한 코드
# 숫자의 범위를 줄이는 게 핵심