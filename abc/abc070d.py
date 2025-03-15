from collections import defaultdict
import heapq
def djk(g,s):
    dist=[float('inf')]*(len(g)+1)
    dist[s]=0
    q=[(0,s)]
    heapq.heapify(q)
    while q:
        pre_dist,now=heapq.heappop(q)
        for nxt,to_dist in g[now]:
            if dist[nxt]>pre_dist+to_dist:
                dist[nxt]=pre_dist+to_dist
                heapq.heappush(q,(pre_dist+to_dist,nxt))
    return dist
                

n=int(input())
d=defaultdict(list)
for _ in range(n-1):
    a,b,c=map(int,input().split())
    d[a].append((b,c))
    d[b].append((a,c))

q,k=map(int,input().split())

r=djk(d,k)
for _ in range(q):
    x,y=map(int,input().split())
    print(r[x]+r[y])

