#ABC211 D

from collections import defaultdict,deque
n,m=map(int,input().split())
d=defaultdict(list)
mod=10**9+7

for _ in range(m):
  a,b=map(int,input().split())
  d[a].append(b)
  d[b].append(a)

def bfs(g,s,e):
  q=deque([s])
  distance=[float("inf")]*(n+1)
  distance[1]=0
  count=[0]*(n+1)
  count[1]=1
  v=set()
  while q:
    now=q.popleft()
    if now not in v:
      v.add(now)
      for nxt in g[now]:
        if distance[nxt]>distance[now]+1:
          distance[nxt]=distance[now]+1
        if distance[nxt]==distance[now]+1:
          count[nxt]+=count[now]
        q.append(nxt)
  return distance,count

r1,r2=bfs(d,1,n)
print(r2[-1]%mod)
        
  
  