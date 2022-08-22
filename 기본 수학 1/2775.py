## 코드 참고 여부
# 혼자품

## 문제 풀이 방식
# 크기가 n인 리스트 생성 후 0층부터 k층까지 무식하게 더해야
 
## 슈도 코드
# n, k 입력받음
# 크기가 n인 리스트 생성. 값은 각 인덱스+1로 초기화
# 1부터 k까지
    # 리스트의 값 재할당
# 리스트의 k-1번째 값 출력

## 어려웠던 부분
# 위의 슈도코드에서 0부터 k까지가 아닌 1부터 k까지로 하면 1층에 값이 할당 안됨
# 시간복잡도 확인 안함

## 걸린 시간
# 26분?

import sys

def f(k, n):
    tmp = [i+1 for i in range(n)]
    for i in range(k):
        tmp_ = tmp.copy()
        tmp = [sum(tmp_[:m+1]) for m in range(n)]
    return tmp[n-1]

result = []
t = int(sys.stdin.readline())
for i in range(t):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    result.append(f(k, n))

for i in result:
    print(i)

