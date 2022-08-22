## 코드 참고 여부
# 스터디원 풀이 참고함

## 문제 풀이 방식
# 다음 도시보다 비쌀 경우
    # 딱 지나갈 만큼만 넣기
# 쌀 경우
    # 더 싼 도시가 나오기 전까지만 넣기
 
## 슈도 코드
# n 입력받음
# road 입력받음
# price 입력받음
# count = 0
# i = 0
# priceNum = price[0]
# while i<= n-1:
    # 만약 price[i]가 priceNum보다 비쌀 경우:
        # priceNum의 값 변경 없음
    # 쌀 경우:
        # priceNum를 더 싼 값(price[i])으로 바꿔주기
    # count += road[i]*price[j]
    # i += 1

## 배운점 
# 해당 문제의 원리 이해(왜 price[i]와 price[i+1]을 비교하는게 아니라 price[i]와 priceNum을 비교하는지)

## 걸린 시간

import sys

n = int(sys.stdin.readline())
road = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))

count = 0
priceNum = price[0]
for i in range(n-1): #road 기준으로 하기 때문에
    if price[i] > priceNum: 
        pass
    else:
        priceNum = price[i]
    count += road[i]*priceNum
print(count)