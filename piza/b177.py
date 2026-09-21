N = int(input())
M = 3 * N
A = [[list(map(int, input().split())) for _ in range(M)] for _ in range(M)]
best = 0
for i in range(N):
    for j in range(N):
        for k in range(N):
            s = 0
            for dz in range(3):
                for dx in range(3):
                    for dy in range(3):
                        s += A[3*k+dz][3*i+dx][3*j+dy]
            best = max(best, s)
print(best)