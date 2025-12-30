n,k=map(int,input().split())
dp=[-1]*(k+1)
dp[0]=0
for _ in range(n):
    a,b=map(int,input().split())
    for i in range(k,-1,-1):
        if dp[i]>=0 and i+b<=k:
            dp[i+b]=max(dp[i+b],dp[i]+a)
print(max(dp))