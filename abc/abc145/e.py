n,t=map(int,input().split())
dp=[-1]*(t+2)
dp[0]=0
menu=[]
for _ in range(n):
    a,b=map(int,input().split())
    menu.append((a,b))
for a,b in menu:
    for i in range(t,-1,-1):
        if dp[i]<0:
            continue
        if i<=t:
            f=i+a
            if f<t:
                dp[f]=max(dp[i]+b,dp[f])
            else:
                dp[t+1]=max(dp[i]+b,dp[t+1])
print(max(dp))