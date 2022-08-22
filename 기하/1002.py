## 코드 참고 여부
# 틀려서 참고함
    # https://velog.io/@junyp1/%EB%B0%B1%EC%A4%80-1002-Python-%ED%84%B0%EB%A0%9B

## 문제 풀이 방식
# 두 원의 중심사이의 거리와 반지름의 합 비교
 
## 슈도 코드
# x1, y1과 x2, y2의 거리 구함
# 반지름 함 구함
# 만약 각 x, y, r 모두 일치하면 -1 출력
# 내부에서 접할 때
    # 접하면:
        # 1 출력
    # 아니면:
        # 0 출력
# 외부에서 접할 때 
    # 거리 < 반지름 합:
        # 2 출력
    # 같으면
        # 1 출력
    # > 이면
        # 0 출력

## 배운점 
# 내접, 외접 상관없이 만나지 않을 때, 한 점에서 만날 때, 두 점에서 만날때로 나눠야 함
# list.remove(value) returns Bool
# dist를 정수로 바꾸면 안됨 (0 == 0.0)
    # ((x1-x2)**2+(y1-y2)**2)**(1/2) == ((x1-x2)**2+(y1-y2)**2)**(0.5)

## 걸린 시간

import sys

t = int(sys.stdin.readline())
for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())

    dist = ((x1-x2)**2+(y1-y2)**2)**(1/2)
    R = [dist, r1, r2]
    maxAll = max(R)
    R.remove(maxAll)

    if dist == 0 and r1 == r2:
        print(-1)
    # 두 원이 만나지 않는 경우
    elif maxAll > sum(R):
        print(0)
    # 두 원이 한 점에서 일치하는 경우
    # maxAll == sum(R)
    elif maxAll == sum(R):
        print(1)
    else:
        print(2) # dist < r1+r2
