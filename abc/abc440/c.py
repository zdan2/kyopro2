t=int(input())
for _ in range(t):
    n,w=map(int,input().split())
    c=list(map(int,input().split()))
    cc=[0]
    for e in c:
        cc.append(cc[-1]+e)
    res=float('inf')
    t=cc[-1]
    for i in range(min(n,w)+1):
        r=cc[i]
        j=i+2*w
        while j<=n:
            r+=cc[j]-cc[j-w]
            j+=2*w
        s=j-w
        if s<n:
            r+=cc[n]-cc[s]
        res = min(res,r,t-r)
    print(res)