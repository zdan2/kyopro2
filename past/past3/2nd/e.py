from collections import defaultdict
n,m,q=map(int,input().split())
d=defaultdict(list)
for _ in range(m):
    u,v=map(int,input().split())
    d[u].append(v)
    d[v].append(u)
color=[0]+list(map(int,input().split()))
for _ in range(q):
    x=list(map(int,input().split()))
    print(color[x[1]])
    if x[0]==1:
        for nxt in d[x[1]]:
            color[nxt]=color[x[1]]
    else:
        color[x[1]]=x[2]