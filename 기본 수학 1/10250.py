## 코드 참고 여부
# 반례참고
    # 10 76 90
    # 2 31 18

## 문제 풀이 방식
# 걷는 거리가 같을 때에는 아래층 선호 -> 엘리베이터로부터 떨어진 수평거리가 같을 경우 아래층부터 선택
# 층 수는 1<= <=h 이므로 n % h를 할 경우 자동적으로 위의 조건 만족
# 호수는 1<= <=w 이므로 n//h에 기본적으로 01호부터 시작하므로 1을 더하면 구할 수 있음 
# w를 층과 호수구할때 쓰지 않는 이유는 n <= w*h이므로 h로부터 n을 구할 경우 무조건 w 이하이기 때문

## 슈도 코드
# h, w, n 입력받음
# n % h가 0일 경우(가장 고층)
    # 층 수는 최대 높이인 h 출력
    # 호수는 n // h
        # 호수+1
# n % h가 0이 아닐 경우
    # 층 수는 n % h
    # 호수는 n // h + 1

## 어려웠던 부분
# 층 수와 호수 사이에 0을 넣을지 말지 체크하는 부분
# %로 층수를 계산할 경우 마지막 층수는 항상 0이 된다는 사실 빠뜨림
# if n % h == 0:
    # if n // h + 1 <= 10:
    # 일 때 n // h가 9일수도 있다는 사실 간과

## 걸린 시간
# 11분?

import sys

t = int(sys.stdin.readline())
result = []
for i in range(t):
    h, w, n = map(int, sys.stdin.readline().split())
    if n % h == 0:
        if n // h + 1 <= 10:
            result.append('{0}0{1}'.format(str(h), str(n // h )))
        else:
            result.append('{0}{1}'.format(str(h), str(n // h )))
    else:
        if n // h + 1 < 10:
            result.append('{0}0{1}'.format(str(n % h), str(n // h + 1)))
        else:
            result.append('{0}{1}'.format(str(n % h), str(n // h + 1)))
            
for i in result:
    print(i)