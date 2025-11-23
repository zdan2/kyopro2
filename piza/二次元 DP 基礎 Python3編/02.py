n, t = map(int, input().split())
x = list(map(int, input().split()))
INF = -10**18
dp = [INF] * (n + 1)
dp[1] = 0 
for i in range(t):
    point = x[i] 
    for j in range(n, 1, -1):
        dp[j] = max(dp[j], dp[j - 1])
    if dp[point] > INF // 2:
        dp[point] += 1
print(max(dp))