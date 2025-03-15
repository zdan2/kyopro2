from collections import defaultdict

n,m,q=map(int,input().split())
d=defaultdict(list)

for _ in range(m):
    u,v=map(int,input().split())
    d[u].append(v)
    d[v].append(u)

color=[0]+list(map(int,input().split()))

for _ in range(q):
    s=list(map(int,input().split()))
    if s[0]==1:
        print(color[s[1]])
        for nxt in d[s[1]]:
            color[nxt]=color[s[1]]
    else:
        print(color[s[1]])
        color[s[1]]=s[2]



