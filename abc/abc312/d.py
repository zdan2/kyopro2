s=input()
n=len(s)
dp=[[0]*(n+1) for _ in range(n+1)]
dp[0][0]=1
mod=998244353
for i in range(n):
    for j in range(n+1):
        if dp[i][j]==0:
            continue
        if s[i] in '(?':
            dp[i+1][j+1]+=dp[i][j]
            dp[i+1][j+1]%=mod
        if s[i] in ')?' and j>0:
            dp[i+1][j-1]+=dp[i][j]
            dp[i+1][j-1]%=mod
print(dp[-1][0])