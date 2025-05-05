from collections import defaultdict

d = defaultdict(list)
n, k = map(int, input().split())

# 行=色(3行)、列=n+1
dp = [[0]*(n+1) for _ in range(3)]

for _ in range(k):
    a, b = map(int, input().split())
    d[a] = b

# 1日目
if 1 in d:
    dp[d[1]-1][0] = 1
else:
    for color in range(3):
        dp[color][0] = 1

# 2日目
if 2 in d:
    for color in range(3):
        dp[d[2]-1][1] += dp[color][0]
else:
    s = sum(dp[color][0] for color in range(3))
    for color in range(3):
        dp[color][1] = s

# 3日目以降
for day in range(2, n):
    if day in d:
        color_fixed = d[day] - 1
        dp[color_fixed][day] = (
            dp[0][day-1] + dp[1][day-1] + dp[2][day-1]
            - dp[color_fixed][day-2]
        )
    else:
        s = dp[0][day-1] + dp[1][day-1] + dp[2][day-1]
        for color in range(3):
            dp[color][day] = s - dp[color][day-2]

ans = dp[0][n-1] + dp[1][n-1] + dp[2][n-1]
print(dp)
