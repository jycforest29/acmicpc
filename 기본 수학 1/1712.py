# n*c > a+n*b -> n의 존재 여부 확인
# n(c-b)>a n>a/(c-b)
a, b, c = map(int, input().split(' '))

if c <= b:
    print(-1)
else:
    print(int(a/(c-b)+1))