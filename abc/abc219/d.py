n=int(input())
x,y=map(int,input().split())
dp=[[-1]*(x+1) for _ in range(y+1)]
dp[0][0]=0
for _ in range(n):
    a,b=map(int,input().split())
    for i in range(y,-1,-1):
        for j in range(x,-1,-1):
            if dp[i][j]>=0:
                ny=min(i+b,y)
                nx=min(j+a,x)
                if dp[ny][nx]==-1:
                    dp[ny][nx]=dp[i][j]+1
                else:
                    dp[ny][nx]=min(dp[ny][nx],dp[i][j]+1)
print(dp[-1][-1])