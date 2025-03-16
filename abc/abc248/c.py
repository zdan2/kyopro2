n,m,k=map(int,input().split())
mod=998244353
dp=[[0]*(n+1) for _ in range(k+1)]
dp[0][0]=1
for j in range(n):
    for i in range(k+1):
        for l in range(1,m+1):
            if i+l<=k:
                dp[i+l][j+1]+=dp[i][j]%mod
c=0
for r in dp:
    c+=r[-1]%mod
print(c%mod)