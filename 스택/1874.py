## 코드 참고 여부
# 틀려서 반례 참고함

## 문제 풀이 방식
# 입력
# [push, push, push, push, pop, pop, push, push, pop, push, push, pop, pop, pop, pop, pop] 
# [1, 2, 3, 4, 5, 6, 7, 8]
# [4, 3, 6, 8, 7, 5, 2, 1]

# 과정
# push, push, push, push [1, 2, 3, 4] []
# pop, pop [1, 2] [4, 3]
# push, push [1, 2, 5, 6] [4, 3]
# pop [1, 2, 5] [4, 3, 6]
# push, push [1, 2, 5, 7, 8] [4, 3, 6]

# 입력
# [1, 2, 5, 3, 4]

# 과정
# push push push push push [1, 2, 3, 4, 5] []
# pop [1, 2, 3, 4] [5]

# -> 스택의 마지막값과 현재 입력리스트에서 비교중인 값이 같으면 pop 아니면 push

## 슈도 코드
# 생략

## 배운점 
# push, pop 하는 반복문의 종료 조건을 stack의 길이가 0일때로 하면 안됨. 그럼 정렬된 리스트가 입력으로 들어왔을 때 
# 무조건 NO로 출력됨
# stack[-1]을 할 땐 stack의 길이가 1 이상인지 항상 확인

## 걸린 시간

import sys

n = int(sys.stdin.readline())
arr = []
res = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))
arrSorted = sorted(arr)

i = 0
j = 1
stack = [arrSorted[0]]
res.append('+')
while i < n:
    if len(stack) > 0 and stack[-1] == arr[i]:
        # pop
        i += 1
        res.append('-')
        del stack[-1]
        continue
    # push
    if j > n-1:
        res = ['NO']
        break
    stack.append(arrSorted[j])
    j += 1
    res.append('+')

print(*res, sep = '\n')