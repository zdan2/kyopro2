n,q=map(int,input().split())
s=[i for i in range(n-1,-1,-1)]
d={i:1 for i in range(n)}
for _ in range(q):
    x,y=map(int,input().split())
    x-=1
    y-=1
    c=0
    while s[-1]<=x:
        c+=d[s.pop()]
    print(c)
    d[y]+=c