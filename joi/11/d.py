n,k=map(int,input().split())
dp=[[-1]*(n+1) for _ in range(3)]
for i in range(3):
    dp[i][0]=0
for _ in range(k):
    a,b=map(int,input().split())
    for i in range(3):
        dp[i][a]=0
    if a==1:
        dp[b-1][1]=1
    else:
        dp[b-1][a]=-1
for i in range(3):
    if dp[i][1]==-1:
        dp[i][1]=1
for j in range(2,n+1):
    for i in range(3):
        if dp[i][j]!=0:
            if dp[i][j-1]==0:
                dp[i][j]=dp[0][j-1]+dp[1][j-1]+dp[2][j-1]
            else:
                dp[i][j]=dp[0][j-1]+dp[1][j-1]+dp[2][j-1]-dp[i][j-2]
for r in dp:
    print(r)
print(dp[0][-1]+dp[1][-1]+dp[2][-1])