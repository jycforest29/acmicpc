# 재귀
def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)

n = int(input())
print(fibo(n))
# ----------------------------------------------
# 반복문
n = int(input())
tmp = [0, 1]
for i in range(2, n+1):
    tmp.append(tmp[i-1]+tmp[i-2])
# 이렇게 분기 안해주면 틀림
if n == 0:
    print(0)
else:
    print(tmp[-1])

# ----------------------------------------------
# 반복문 - 다른 정답 풀이(https://bohyeon-n.github.io/deploy/algorithm/fibonacci.html)
# 내 풀이와 달리 외부 공간을 사용하지 않음. 따라서 메모리 측면에서 이득
n = int(input())
prepre = 0
pre = 1
for i in range(2, n+1):
    fib = pre+prepre
    prepre = pre 
    pre = fib

if n <= 1:
    print(n)
else:
    print(fib)

# 배울점
# 반복문 중 외부 공간을 사용하지 않는 풀이