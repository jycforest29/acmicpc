## 코드 참고 여부
# 반례 참고

## 문제 풀이 방식
# 입력받은 수들을 각각 문자열로 변환해 자리수별로 더해줘야 할듯

## 슈도 코드
# a, b 입력받음
# a, b를 각각 문자열로 변환
# 문자열 a, b의 -1번째 인덱스부터 0번째 인덱스까지 a[인덱스]+b[인덱스]를 한 후 결과를 리스트에 저장
    # 만약 합한 결과가 9보다 클 경우 합한결과 - 10을 리스트[인덱스+1]에 미리 저장
# 리스트의 값을 모두 문자열로 바뀐뒤 더하고 출력

## 어려웠던 부분
# a, b의 자리수가 다를 수 있다는 점 간과
# tmp 리스트에서는 타입이 int로 일정해야

## 걸린시간
# 1시간

import sys

a, b = sys.stdin.readline().split()

maxTmp = list(str(max(int(a), int(b))))
minTmp = list(str(min(int(a), int(b))))
tmp = list(map(int, [0]+maxTmp))

for i in range(len(minTmp)): # [0, len(minTmp)-1]
    tmpSum = tmp[-i-1]+int(minTmp[-i-1]) #[-1, -len(minTmp)]
    if tmpSum > 9:
        tmp[-i-1] = tmpSum - 10 #[-1, -len(minTmp)]
        tmp[-i-2] += 1 #[-2, -len(minTmp)-1]
        # 1999 1같은 경우들
        if tmp[-i-2] > 9:
            j = 0
            while tmp[-i-2-j] > 9:
                tmp[-i-2-j] = tmp[-i-2-j] - 10
                tmp[-i-3-j] += 1
                j += 1
        continue
    tmp[-i-1] = tmpSum

sum = ''
for i in range(len(tmp)):
    sum += str(tmp[i])
if tmp[0] == 0:
    print(sum[1:])
else:
    print(sum)