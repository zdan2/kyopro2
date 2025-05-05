import heapq
from collections import defaultdict
n,x=map(int,input().split())
d=defaultdict(list)
for _ in range(n-1):
    a,b,c=map(int,input().split())
    d[a].append((c,b))
    d[b].append((c,a))
for i in range(1,n+1):
    hq=[]
    v=set()
    dist=[float('inf')]*(n+1)
    for cost,nxt in d[i]:
        heapq.heappush(hq,(cost,nxt))
    while hq:
        cost,nxt=heapq.heappop(hq)
        if cost>x:
            break
        if cost==x:
            print('Yes')
            exit()
        if cost==dist[nxt]:
            v.add(nxt)
        for weight,ne in d[nxt]:
            if ne not in v and dist[ne]>cost+weight and cost+weight<=x:
                dist[ne]=cost+weight
                heapq.heappush(hq,(cost+weight,ne))
print('No')