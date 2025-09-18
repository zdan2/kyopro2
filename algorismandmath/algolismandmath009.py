n,s=map(int,input().split())
a=list(map(int,input().split()))
dp=[[False]*(s+1) for _ in range(n+1)]
dp[0][0]=True
for i in range(1,n+1):
    for j in range(s+1):
        if dp[i-1][j]==True:
            dp[i][j]=True
            if j+a[i-1]<s+1:
                dp[i][j+a[i-1]]=True

if dp[n][s]==True:
    print('Yes')
else:
    print('No')

