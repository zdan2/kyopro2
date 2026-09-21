from sortedcontainers import SortedList
from collections import defaultdict
n,m=map(int,input().split())
d=defaultdict(list)
mod=10**9+7
for _ in range(m):
    u,v=map(int,input().split())
    d[u].append(v)
    d[v].append(u)
hq=SortedList()
hq.add((0,1))
dist=[float('inf')]*(n+1)
dist[1]=0
from_cur=[0]*(n+1)
from_cur[1]=1
while hq:
    l,cur=hq.pop(0)
    for nxt in d[cur]:
        if dist[nxt]>l+1:
            dist[nxt]=l+1
            from_cur[nxt]=from_cur[cur]
            hq.add((l+1,nxt))
        elif dist[nxt]==l+1:
            from_cur[nxt]+=from_cur[cur]
            from_cur[nxt]%=mod
print(from_cur[n]%mod)
            