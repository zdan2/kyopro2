n,w=map(int,input().split())
dp=[-float('inf')]*(w+1)
jewels=[tuple(map(int,input().split())) for _ in range(n)]
dp[0]=(0)
mx=0
for jewel in jewels:
    for i in range(w,-1,-1):
        if dp[i]>=0 and i+jewel[0]<=w:
            dp[i+jewel[0]]=max(dp[i+jewel[0]],dp[i]+jewel[1])
            mx=max(mx,dp[i+jewel[0]])

print(mx)


