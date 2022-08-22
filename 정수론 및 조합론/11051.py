## 코드 참고 여부
# 파스칼의 삼각형 찾아봄
    # https://javalab.org/pascals_triangle/

## 문제 풀이 방식
# nCk는 n-1Ck-1+n-1Ck
# 전체 삼각형의 테두리를 다 1이어야 성립
 
## 슈도 코드
# n, k 입력받음
# 전체 줄들 저장할 리스트 생성
# 1부터 n까지
    # n <= 2일때
        # 리스트에 [1]*n 추가
    # 아닐때
        # 임시 리스트 생성
        # m은 0부터 n-2까지
            # nCm는 n-1Cm+n-1Cm+1로 임시 리스트에 추가
            # 만약 n번째 줄이고 m이 k와 같을 경우 
                # break
        # 임시 리스트[0] = 0, 임시 리스트[-1] = 0 추가
# 리스트[n][k] 출력

## 배운점
# 이항계수 nCk는 n+1의 줄, k+1개의 행이 필요함

## 걸린 시간

import sys

n, k = map(int,sys.stdin.readline().split())
tmp = list()
for i in range(n+1): # [0, n] -> n+1줄
    if i <= 1:
        tmp.append([1]*(i+1))
        continue
    tmp_ = [1]
    for j in range(i-1): # [0, n-2] -> n+1 행
        tmp_.append(tmp[i-1][j]+tmp[i-1][j+1])
        if i == n and j-1 == k:
            tmp.append(tmp_)
            print(tmp[n][k]%10007)
            exit(0)
    tmp_.append(1)
    tmp.append(tmp_)