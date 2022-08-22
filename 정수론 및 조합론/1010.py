## 코드 참고 여부
# 혼자품 -> dp 함수를 다른 사람 풀이로 바꿔봄
    # 
## 문제 풀이 방식
# mCn을 구하는 문제. 일단 구하면 알아서 순서대로 할당됨
 
## 슈도 코드
# t 입력받음
# t 동안
    # n, m 입력받음
    # 파스칼 삼각형을 통한 이항계수 구하기로 mCn 구함

## 배운점

## 걸린 시간

import sys

def dp(n, k):
    table = [[1]*(i) for i in range(1, n+2)] #[1, n+1] 총 n+1개의 서브리스트
    for i in range(2, n+1):#[2, n]
        for j in range(1, n-1): #[1, n-1]
            table[i][j] = table[i-1][j]+table[i-1][j+1]
    
    return table[n][k]

n, k = map(int,sys.stdin.readline().split())

t = int(sys.stdin.readline())
result = []
for i in range(t):
    n, m = map(int,sys.stdin.readline().split())
    result.append(dp(m, n))

for i in result:
    print(i)
