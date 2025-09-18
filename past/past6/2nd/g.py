from collections import defaultdict
import heapq
n,m,k=map(int,input().split())
d=defaultdict(list)
visited=[False]*(n+1)
for _ in range(m):
    a,b,c=map(int,input().split())
    d[a].append((b,c))
    d[b].append((a,c))
x=list(map(int,input().split()))
hq=[]
for nxt,cost in d[1]:
    heapq.heappush(hq,(cost,nxt))
visited[1]=True
r=1
for i in range(k):
    limit=x[i]
    nhq=[]
    while hq:
        nc,nxt=heapq.heappop(hq)
        if visited[nxt]:
            continue
        if nc<=limit:
            visited[nxt]=True
            r+=1
            for a,b in d[nxt]:
                if not visited[a]:
                    nhq.append((b,a))
        else:
            nhq.append((nc,nxt))
            break
    for e in nhq:
        heapq.heappush(hq,e)
    print(r)