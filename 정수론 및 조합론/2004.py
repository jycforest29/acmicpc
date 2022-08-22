## 코드 참고 여부
# 시간초과나서 참고함 -> 아예 다른 방식의 풀이로 풀어야 해결되는듯
    # https://velog.io/@ledcost/%EB%B0%B1%EC%A4%80-2004-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A1%B0%ED%95%A9-0%EC%9D%98-%EA%B0%9C%EC%88%98-%EC%8B%A4%EB%B2%842-%EC%A1%B0%ED%95%A9%EB%A1%A0

## 문제 풀이 방식
# 2, 5 쌍이 몇개인지를 구해야
# 5의 지수 = n!의 5의 지수 - (n-r)!의 5의 지수 - r!의 5의 지수
 
## 슈도 코드
# n, m 입력받음
# nCm 값의 2의 지수 구함
# nCm 값의 5의 지수 구함
# 10은 2와 5의 쌍으로 이루어지므로 둘 중 작은값 출력

## 배운점
# 5의 지수 = n!의 5의 지수 - (n-r)!의 5의 지수 - r!의 5의 지수
# 지수 구하는 법
    # while n >= check:
        # count += n // check
        # n //= check
# 12! = 12(2:2)*11*10(2:1, 5:1)*9*8(2:3)*7*6(2:1)*5(5:1)*4(2:2)*3*2(2:1)*1

## 걸린 시간

import sys

def f(n, check):
    count = 0
    while n >= check:
        count += n // check
        n //= check

    return count

n, m = map(int, sys.stdin.readline().split())
nCheck = f(n, 2) - f(n-m, 2) - f(m, 2)
mCheck = f(n, 5) - f(n-m, 5) - f(m, 5)
print(min(nCheck, mCheck))
