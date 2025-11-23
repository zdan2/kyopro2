n,k=map(int,input().split())
a=list(map(int,input().split()))
dp=[0]*(k+1)
dp[0]=1
for e in a:
    for i in range(k+1,-1,-1):
        if i+e<=k and dp[i]>0:
            dp[i+e]+=dp[i]
            dp[i+e]%=10**9
print(dp[-1])