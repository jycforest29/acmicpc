## 코드 참고 여부
# 아예 감도 안와서 풀이 참고
    # https://velog.io/@ledcost/%EB%B0%B1%EC%A4%80-2981-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EA%B2%80%EB%AC%B8-%EA%B3%A8%EB%93%9C5-%EC%A0%95%EC%88%98%EB%A1%A0

## 문제 풀이 방식
# a = m*a'+r
# b = m*b'+r
# c = m*c'+r
# ----------
# b-a = m(b'-a')
# c-b = m(c'-b')
# 이므로 입력받은 모든 수(오름차순 기준)에 대해 m은 연속된 2개의 수의 차이의 공약수임
# 따라서 m은 이웃한 것들끼리 뺀 수들의 최대 공약수의 1을 제외한 모든 약수들
 
## 슈도 코드
# n 입력받음
# 리스트 생성
# n 동안
    # 입력받음
# 입력리스트 오름차순 정렬
# 이웃한 것들끼리 뺀 새로운 리스트 생성
# 위 리스트에 속한 수의 최대 공약수 구함
# 최대 공약수의 모든 약수들을 구해 1 제외하고 출력

## 배운점
# 동일한 수로 나눠 동일한 나머지를 가질때 어떻게 처리해야 하는지
# 3개 이상 수들의 최대공약수는 연속으로 최대공약수를 구하는 방법으로 가능()
# 정렬된 리스트 한번에 출력

## 걸린 시간

import sys

def gcd(n, m):
    while True:
        if n % m == 0:
            return m
        n, m = m, n % m

n = int(sys.stdin.readline())
inputs = list()

for i in range(n):
    inputs.append(int(sys.stdin.readline()))
inputs.sort()

subs = [0]*(n-1)
for i in range(1, n):
    subs[i-1] = inputs[i] - inputs[i-1]

# subs의 최대공약수 구하기
check = subs[0]
for i in range(1, len(subs)):
    check = gcd(subs[i], check)

mSet = set()
# 최종 최대공약수의 모든 약수들 구하기
for i in range(2, int(check**0.5)+1):
    if check % i == 0:
        mSet.add(i)
        mSet.add(check // i)
mSet.add(check)
print(*sorted(list(mSet)))