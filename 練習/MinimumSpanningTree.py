from collections import defaultdict
import heapq
n,m=map(int,input().split())
d=defaultdict(list)
for _ in range(m):
    a,b,c=map(int,input().split())
    d[a].append((b,c))
    d[b].append((a,c))
hq=[]
for nxt,cost in d[0]:
    heapq.heappush(hq,(cost,nxt))
used=[float('inf')]*n
used[0]=0 
while hq:
    cc,now=heapq.heappop(hq)
    if used[now]!=float('inf'):
        continue
    used[now]=cc
    for nxt,cost in d[now]:
        heapq.heappush(hq,(cost,nxt))
print(sum(used)) 