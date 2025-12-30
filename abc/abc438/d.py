n=int(input())
a=[list(map(int,input().split())) for _ in range(3)]
dp=[[0]*n for _ in range(3)]
dp[0][0]=a[0][0]
for i in range(1,n):
    for j in range(3):
        if j==0 and i < n-2:
            dp[0][i]=dp[0][i-1]+a[0][i]
        elif j==1 and i < n-1:
            dp[j][i]=max(dp[j-1][i-1],dp[j][i-1])+a[j][i]
        elif j==2 and i>1:
            dp[j][i]=max(dp[j-1][i-1],dp[j][i-1])+a[j][i]
dp[2][-1]=max(dp[1][-2],dp[2][-2])+a[2][-1]
print(dp[-1][-1])