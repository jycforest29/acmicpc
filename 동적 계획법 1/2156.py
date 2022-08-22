## 코드 참고 여부
# 점화식 모르겠어서 참고함
    # https://velog.io/@yanghl98/%EB%B0%B1%EC%A4%80-2156-%ED%8F%AC%EB%8F%84%EC%A3%BC-%EC%8B%9C%EC%8B%9D

## 문제 풀이 방식
# 3개에 대해서만 생각
# oox -> table[i-1]
# oxo -> table[i-2]+arr[i]
# xoo -> table[i-3]+arr[i-1]+arr[i]

## 슈도 코드
# 위에서 작성

## 배운점 
# 단위를 쪼개 모든 경우의 수 정확하게 따지는 방법

## 걸린 시간

import sys

n = int(sys.stdin.readline())
arr = [0]
for i in range(n):
    arr.append(int(sys.stdin.readline()))

if n <= 2:
    print(sum(arr))
else:
    table = [0, arr[1], arr[1]+arr[2]]
    for i in range(3, n+1):
        table.append(max(table[i-1], table[i-2]+arr[i], table[i-3]+arr[i-1]+arr[i]))

    print(table[n])