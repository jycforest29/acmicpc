## 코드 참고 여부
# 스터디원 풀이 참고함

## 문제 풀이 방식
# +, -, 양수
# -가 0개 -> 그냥 합 출력
# -가 1개 -> 첫번째 - 이후 모두 뺌

## 슈도 코드
# 문자열 입력받은 뒤 숫자, +, - 단위로 리스트에 저장
# -가 0개이면 숫자의 합 출력
# -가 1개이상이면
    # 첫번째 -의 위치를 구함
    # 그 위치 전까지 숫자는 모두 더함
    # 그 위치 이후 숫자는 모두 뺌

## 배운점 
# 문자열을 리스트로 바로 바꾸는 메서드는 없음
# -가 1개인 경우와 2개 이상인 경우를 1개 이상인 경우로 한번에 합쳐서 풀 수 있음
# 예를들어 1+2+3-4+5-6에서 -의 모든 위치를 구할 때
    # index = tmp.index('-')
    # index_ = tmp[index+1:].index('-')
    # 이렇게 구하면 index_는 tmp에서의 index가 나오지 않고 tmp[index+1:]에서의 인덱스가 나옴
    # 따라서 index_ = index+1+tmp[index+1:].index('-') 해줘야

## 걸린 시간

import sys

inputStr = sys.stdin.readline().strip()
tmp = []
index = 0
for i in range(len(inputStr)):
    if inputStr[i] == '-':
        tmp.append(inputStr[index:i])
        tmp.append('-')
        index = i+1
    elif inputStr[i] == '+':
        tmp.append(inputStr[index:i])
        tmp.append('+')
        index = i+1
tmp.append(inputStr[index:])

count = tmp.count('-')
cal = 0
len_ = len(tmp)

if count == 0:
    for i in range(0, len_, 2):
        cal += int(tmp[i])
else:
    index = tmp.index('-')
    for i in range(0, index, 2):
        cal += int(tmp[i])
    for i in range(index+1, len_, 2):
        cal -= int(tmp[i])

print(cal)

# -------------------------이 부분 왜 안됐는지 확인------------------------
# if count == 0:
#     for i in range(0, len_, 2):
#         cal += int(tmp[i])
# elif count == 1:
#     index = tmp.index('-')
#     for i in range(0, index, 2):
#         cal += int(tmp[i])
#     for i in range(index+1, len_, 2):
#         cal -= int(tmp[i])
# else:
#     index = tmp.index('-')
#     index_ = index+1+tmp[index+1:].index('-')
#     print(index, index_)
#     while True:
#         for i in range(0, index, 2):
#             cal += int(tmp[i])
#         for i in range(index+1, index_, 2):
#             cal -= int(tmp[i])
#         index = index_
#         index_ = tmp[index+1:].index('-')
#         if index_ < index:
#             break

# print(cal)
