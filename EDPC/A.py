n=int(input())
h=[0]+list(map(int,input().split()))
dp=[float('inf')]*(n+1)
dp[0]=0
dp[1]=abs(h[1]-h[0])
for i in range(2,n+1):
    dp[i]=min(dp[i-2]+abs(h[i]-h[i-2]),dp[i-1]+abs(h[i]-h[i-1]))
print(dp)