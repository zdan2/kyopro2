n=int(input())
s=list(input())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
dp=[[-float('inf')]*n for _ in range(2)]
if s[0]=='S':
    dp[0][0]=0
    dp[1][0]=-x[0]
else:
    dp[0][0]=-x[0]
    dp[1][0]=0
for i in range(1,n):
    if s[i]=='S':
        dp[0][i]=max(dp[0][i-1],dp[1][i-1]+y[i-1])
        dp[1][i]=max(dp[0][i-1],dp[1][i-1])-x[i]
    else:
        dp[1][i]=max(dp[0][i-1],dp[1][i-1])
        dp[0][i]=dp[1][i]-x[i]
    print(dp)