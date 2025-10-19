from collections import defaultdict, deque
n,m=map(int,input().split())
d=defaultdict(list)
for _ in range(m):
    u,v=map(int,input().split())
    d[u].append(v)
    d[v].append(u)
res=float('inf')
for i in range(2**n):
    color=[0]*(n+1)
    for j in range(n):
        if i>>j&1:
            color[j+1]=1
    c=0
    for u in range(1,n+1):
        for v in d[u]:
            if color[u]==color[v]:
                c+=1
    res=min(res,c)
print(res//2)