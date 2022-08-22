print(5%1) # 0

n = 1
dp1 = [[0]*10 for _ in range(n+1)]
dp2 = [[0 for _ in range(10)] for _ in range(n+1)]
print(dp1) # 결과는 [[0, 0, ,,, 0, 0], [0, 0, ,,, 0, 0]]
print(dp2) # 결과는 [[0, 0, ,,, 0, 0], [0, 0, ,,, 0, 0]]
dp1[0] = 1
dp2[0] = 1
print(dp1) # 결과는 [1, [0, 0, ,,, 0, 0]]
print(dp2) # 결과는 [1, [0, 0, ,,, 0, 0]]