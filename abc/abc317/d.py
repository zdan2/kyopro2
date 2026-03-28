n=int(input())
r=[]
c=0
for _ in range(n):
    x,y,z=map(int,input().split())
    c+=z
    r.append((x,y,z))
dp=[float('inf')]*(c+1)
dp[0]=0
for x,y,z in r:
    for i in range(c,-1,-1):
        if dp[i]!=float('inf'):
            if x>y:
                dp[i+z]=dp[i]
            else:
                dp[i+z]=min(dp[i+z],dp[i]+(y-x+1)//2)
    if x>y:
        dp[z]=0
print(min(dp[c//2+1:]))