n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
dp=[[0]*(m+1) for _ in range(n+1)]
for i in range(n+1):
    dp[i][0]=1
for i in range(1,n+1):
    for j in range(1,m+1):
        if a[i-1]==b[j-1]:
            dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
        else:
            dp[i][j]=dp[i-1][j]
print('Yes' if dp[n][m]>1 else 'No')