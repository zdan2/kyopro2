n,m=map(int,input().split())
k=int(input())
g=[[False]*m for _ in range(n)]
for _ in range(k):
    a,b=map(int,input().split())
    g[a-1][b-1]=True
    le,up=max(0,a-2),max(0,b-2)
    ri,bt=min(n,a+1),min(n,b+1)
    for i in range(le,ri):
        for j in range(up,bt):
            g[i][j]=True
print(sum(sum(r) for r in g))    