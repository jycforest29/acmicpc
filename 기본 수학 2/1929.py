## 코드 참고 여부
# 혼자품

## 문제 풀이 방식
# 결국 소수인 것들을 찾아야
# 앞의 문제와 달리 시간이 1초이므로 1과 자기자신외에는 약수가 없는 소수의 특징을 이용해 제곱근으로 소수 구하기
 
## 슈도 코드 
# m, n 입력받음
# 빈 리스트 생성
# m부터 n까지
    # 순서대로 제곱근을 취함
    # 2부터 int(해당제곱근)+1까지
        # 1씩 더해가며 제곱근을 취하기 이전 수가 나누어 떨어지는지 확인
        # 나누어 떨어진다면 리스트에 추가
# 리스트 출력

## 배운점

## 걸린 시간
# 약 11분

import sys

def f(num):
    if num == 1:
        return True
    for i in range(2, int(num**(1/2))+1):
        if num % i ==0:
            return True
    return False

m, n = map(int, sys.stdin.readline().split())
tmp = list()

for i in range(m, n+1):
    if f(i) == False:
        tmp.append(i)

for i in tmp:
    print(i)