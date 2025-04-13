n,mw=map(int,input().split())
item=[]
vs=0
for _ in range(n):
    v,w=map(int,input().split())
    vs+=v
    item.append((v,w))
dp=[float('inf')]*(vs+1)
dp[0]=0
for v,w in item:
    for i in range(vs,-1,-1):
        if dp[i]!=float('inf'):
            if dp[i]+w<=mw and dp[i+v]>dp[i]+w:
                dp[i+v]=dp[i]+w
for i in range(vs,-1,-1):
    if dp[i]!=float('inf'):
        print(i)
        exit()