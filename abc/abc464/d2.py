t = int(input())
for _ in range(t):
    N = int(input())
    weather = list(input())
    X = list(map(int,input().split()))
    Y = list(map(int,input().split()))
    costS = 0 if weather[0] == 'S' else X[0]
    costR = 0 if weather[0] == 'R' else X[0]
    dpS = -costS
    dpR = -costR
    for i in range(1, N):
        costS = 0 if weather[i] == 'S' else X[i]
        costR = 0 if weather[i] == 'R' else X[i]
        ndpS = max(dpS,dpR + Y[i - 1]) - costS
        ndpR = max(dpS,dpR) - costR
        dpS, dpR = ndpS, ndpR
    print(max(dpS, dpR))