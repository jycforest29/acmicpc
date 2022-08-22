## 코드 참고 여부
# 잘 모르겠어서 참고함
# https://velog.io/@hrzo1617/%EB%B0%B1%EC%A4%80-2447-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%B3%84-%EC%B0%8D%EA%B8%B0-10

## 문제 풀이 방식
# f(27) -> 27칸 비어있음
# f(9)*9 -> 9칸 비어있음
# f(3)*9*9 -> 1칸 비어있음

## 배운점 
# 한 줄씩 생각해야함

## 걸린 시간

## 슈도 코드
# 재귀함수 
    # 별을 담을 빈 리스트 생성
    # 늘어나는 줄 수*len(star)동안(이하 i)
        # 만약 i를 len(star)로 나눴을 때 1이면
            # 빈 리스트의 3, 4, 5범위에는 ' '이 들어감
        # 아닐 경우
            # star[특정값]*3
    # 리스트 리턴

# 바닥조건 리스트 생성 ['***', '* *', '***'](이하 star)
# n 입력받음
# n이 3이 될 때까지 // 3하는 count 변수 생성 구하기(이하 count)

# count 동안
    # star = 재귀함수(star)

# star를 한 줄씩 출력

import sys

def f(star):
    tmp = []
    # i는 열임
    for i in range(3*len(star)):
        # tmp에 append 되는 값은 행임
        if i // len(star) == 1: # 항상 3, 4, 5번째 줄
            tmp.append(star[i % len(star)]+len(star)*' '+star[i % len(star)])
        else:
            tmp.append(3*star[i % len(star)])
    return tmp

# 바닥조건을 n == 3일때로 설정
star = ['***', '* *', '***']
n = int(sys.stdin.readline())
count = 0

while n > 3:
    n //= 3
    count += 1

for i in range(count):
    star = f(star)

for i in star:
    print(i)
