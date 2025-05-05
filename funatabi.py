from collections import defaultdict 
import heapq
def djk(s,g,d,n):
    hq=[]
    heapq.heappush(hq,(0,s))
    dist=[float('inf')]*(n+1)
    dist[s]=0
    while hq:
        cost,now=heapq.heappop(hq)
        if now==g and cost==dist[g]:
            return cost
        if cost>dist[now]:
            continue
        for w,nxt in d[now]:
            if dist[nxt]>cost+w:
                dist[nxt]=cost+w
                heapq.heappush(hq,(cost+w,nxt))
    return -1
                
n,k=map(int,input().split())
d=defaultdict(list)
for _ in range(k):
    q=list(map(int,input().split()))
    if q[0]==0:
        r=djk(q[1],q[2],d,n)
        print(r)
    else:
        ci,di,pi=q[1],q[2],q[3]
        d[ci].append((pi,di))
        d[di].append((pi,ci))