import sys

n = int(sys.stdin.readline()) 

# 빼는 풀이(https://velog.io/@cco2416/%EB%B0%B1%EC%A4%80-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%ED%8C%8C%EC%9D%B4%EC%8D%AC2292%EB%B2%88-%EA%B7%B8%EB%A3%B9-%EB%8B%A8%EC%96%B4-%EC%B2%B4%EC%BB%A4)
c = 1
# n > 1인 이유는 식이 1+6*~로 전개되기 때문
while n > 1:
    n-=(6*c)
    c +=1
print(c)
# ----------------------------------------------
# 더하는 풀이(https://velog.io/@cco2416/%EB%B0%B1%EC%A4%80-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%ED%8C%8C%EC%9D%B4%EC%8D%AC2292%EB%B2%88-%EA%B7%B8%EB%A3%B9-%EB%8B%A8%EC%96%B4-%EC%B2%B4%EC%BB%A4)
c = 1
s = 1
while True:
    # ~ 까지 이므로
    if s >= n:
        break
    s +=(6*c)
    c +=1
print(c)

# 배울점
# 브루트포스인 척하는 배수 문제(시간 2초, 메모리 128, n 10억까지 만족)
# 나머지 처리를 어떻게 할 것이냐