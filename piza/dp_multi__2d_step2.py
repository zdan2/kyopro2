n,m=map(int,input().split())
a=[list(map(int,input().split())),list(map(int,input().split()))]
k=min(sum(a[0]),sum(a[1]))
dp=[[0]*(k+1) for _ in range(2)]
dp[0][0]=1
dp[1][0]=1
for i in range(2):
    for e in a[i]:
        for j in range(k+1,-1,-1):
            if e+j<=k and dp[i][j]>0:
                dp[i][j+e]+=dp[i][j]
                dp[i][j+e]%=10**9
r=sum(dp[0][i]*dp[1][i] for i in range(k+1) )
print(r%10**9)