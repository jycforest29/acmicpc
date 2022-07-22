# 재귀
def fact(n):
    if n <= 1:
        return 1
    return n*fact(n-1)

n = int(input())
print(fact(n))
# ----------------------------------------------
# 반복문
n = int(input())

# n <= 1이므로 tmp[0], tmp[1] 모두 1
tmp = [1, 1]
# 입력받은 값까지
for i in range(2, n+1):
    tmp.append(i*tmp[i-1])
print(tmp[-1])

# ----------------------------------------------
# 반복문 - 다른 정답 풀이(https://dojang.io/mod/page/view.php?id=1274)
# 내 풀이와 달리 외부 공간을 사용하지 않음. 따라서 메모리 측면에서 이득
n = int(input()) 
result = 1
for i in range(1, n+1):
    result *= i
print(result)

# 배울점
# 반복문 중 외부 공간을 사용하지 않는 풀이