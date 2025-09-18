n,l=map(int,input().split())
hardle=set(map(int,input().split()))
t1,t2,t3=map(int,input().split())
dp=[float('inf')]*(l+4)
dp[0]=0
for i in range(l):
    cost = t1 + (t3 if i + 1 in hardle else 0)
    dp[i + 1] = min(dp[i + 1], dp[i] + cost)
    if i + 2 <= l:
        cost = t1 + t2 + (t3 if i + 2 in hardle else 0)
        dp[i + 2] = min(dp[i + 2], dp[i] + cost)
    else: 
        d = l - i
        dp[l] = min(dp[l], dp[i] + t1 // 2 + t2 * (d - 1) + t2 // 2)
    if i + 4 <= l:
        cost = t1 + 3 * t2 + (t3 if i + 4 in hardle else 0)
        dp[i + 4] = min(dp[i + 4], dp[i] + cost)
    else: 
        d = l - i
        dp[l] = min(dp[l], dp[i] + t1 // 2 + t2 * (d - 1) + t2 // 2)
print(dp[l])