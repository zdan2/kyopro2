n=int(input())
tw=0
p=[]
ch=0
cw=0
for _ in range(n):
    w,h,b=map(int,input().split())
    tw+=w
    if h>=b:
        p.append((w,h,b))
    else:
        ch+=b
        cw+=w
dp=[-1]*(tw//2+1)
dp[0]=ch
for w,h,b in p:
    for i in range(tw//2,-1,-1):
        if dp[i]>=0 and i+w<=tw//2:
            dp[i+w]=max(dp[i+w],dp[i]+h)
        dp[i]+=b
print(max(dp))