d=int(input())
mod=10**9+7
dp=[[0]*2 for _ in range(d)]
dp[0][0]=0
dp[0][1]=9
for i in range(1,d):
    dp[i][0]=(dp[i-1][1]+dp[i-1][0]*10)%mod
    dp[i][1]=((pow(10,i+1,mod)-1)-dp[i][0])%mod
print(dp[-1][0])