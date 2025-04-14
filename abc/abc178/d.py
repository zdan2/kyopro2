s=int(input())
dp=[0]*(s+1)
for i in range(3,s+1):
    dp[i]=1
mod=10**9+7
for i in range(3,s+1):
    for j in range(3,s+1):
        if i+j<=s:
            dp[i+j]+=dp[i]%mod
print(dp[-1]%mod)