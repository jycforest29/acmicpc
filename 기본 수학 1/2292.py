## 코드 참고 여부
# https://velog.io/@cco2416/%EB%B0%B1%EC%A4%80-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%ED%8C%8C%EC%9D%B4%EC%8D%AC2292%EB%B2%88-%EA%B7%B8%EB%A3%B9-%EB%8B%A8%EC%96%B4-%EC%B2%B4%EC%BB%A4
# 8일전에 참고해서 풀고 안보고 다시 풀어봄

## 문제 풀이 방식
# 벌집번호 1 1+6*1 1+6*1+6*2
# 방 수    1 2     3

## 슈도 코드
# 벌집번호 입력받음
# count = 1
# 벌집번호값이 1이 될때까지
#     벌집번호 -= 6*count
#     count += 1
# count값 출력

import sys
 
n = int(sys.stdin.readline())
count = 1
while n > 1:
    n -= 6*count
    count += 1
print(count)