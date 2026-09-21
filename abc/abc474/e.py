n=int(input())
for _ in range(n):
    m=int(input())
    r=[list(map(int,input().split())) for _ in range(m)]
    rs=sorted([a-b for a,b in r])
    crs=[0]
    for e in rs:
        crs.append(crs[-1]+e)
    ans=float('inf')
    sb=sum(b for a,b in r)
    ma=min(a for a,b in r)
    for i in range(m+1):
        ans=min(ans,sb+crs[i]+ma*max(0,m-2*i))
    print(ans)
    